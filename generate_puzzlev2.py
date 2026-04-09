import json, hashlib, subprocess
from datetime import date
from supabase import create_client

# ── Your Supabase credentials ──────────────────────────────
SUPABASE_URL = "https://atjnnkqzwynurhfxtswq.supabase.co"   # ← replace
SUPABASE_KEY = "sb_publishable_KHrysbPNgaYneARmgznUXw_bCNSjAZT"                 # ← replace (anon key)
# ───────────────────────────────────────────────────────────

def seconds_to_time(s):
    return f'{s // 3600}:{(s % 3600) // 60:02d}'

def normalize_weapon(key):
    return key.replace('$', '').replace('_', ' ').lower()

def crack_solution(d):
    target = d['correctAnswer']
    victim = d['victim']
    suspects = [c for c in d['characterNames'] if c != victim]
    for suspect in suspects:
        for weapon_key in d['weaponMap'].keys():
            weapon = normalize_weapon(weapon_key)
            for i in range(d['numIntervals'] + 1):
                time_str = seconds_to_time(d['timeOffset'] + i * 900)
                combo = f'{suspect}-{weapon}-{time_str}'
                if hashlib.sha256(combo.encode()).hexdigest() == target:
                    return {
                        "killer": suspect,
                        "weapon": weapon,
                        "weapon_key": weapon_key,
                        "time": time_str
                    }
    return None

def generate_puzzle(mode="standard"):
    """
    mode = "simple"   → 3 chars, 4 rooms (easier)
    mode = "standard" → 4 chars, 4 rooms (default)
    """
    configs = {
        "simple":   {"nchars": 3, "nplaces": 4},
        "standard": {"nchars": 4, "nplaces": 4},
    }

    cfg = configs.get(mode, configs["standard"])
    print(f"⚙️  Running puzzle generator (mode={mode}, chars={cfg['nchars']}, rooms={cfg['nplaces']})...")

    subprocess.run(
        [
            "mystery-o-matic",
            "scenarios/simple.template.sol",
            "static",
            "out",
            "--nchars",  str(cfg["nchars"]),
            "--nplaces", str(cfg["nplaces"]),
        ],
        check=True
    )

    with open("out/data.js", "r") as f:
        content = f.read().strip()
    if content.startswith("data ="):
        content = content[6:].strip().rstrip(";")
    return json.loads(content)

def push_to_supabase():
    today = str(date.today())
    supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

    # Check if today's room already exists
    existing = supabase.table("rooms").select("id").eq("puzzle_date", today).execute()
    if existing.data:
        print(f"✅ Room for {today} already exists. ID: {existing.data[0]['id']}")
        return

    # Generate puzzle (still needed to produce data.js + static files)
    # Switch between "simple" and "standard" here
    d = generate_puzzle(mode="standard")

    # Just insert the date — puzzle content served from static files
    result = supabase.table("rooms").insert({
        "puzzle_date": today
    }).execute()

    print(f"✅ Room created for {today}")
    print(f"   Room ID: {result.data[0]['id']}")

if __name__ == "__main__":
    d = generate_puzzle()
    print(f"✅ Puzzle generated — {date.today()}")
    print(f"   Victim   : {d['victim']}")
    print(f"   Suspects : {[c for c in d['characterNames'] if c != d['victim']]}")

    solution = crack_solution(d)
    if solution:
        print(f"   Killer   : {solution['killer']}")
        print(f"   Weapon   : {solution['weapon']}")
        print(f"   Time     : {solution['time']}")
    else:
        print("   ⚠️  Could not crack solution — check correctAnswer hash")

    print()
    print("📁 out/data.js written. Now run:")
    print('   git add out/data.js && git commit -m "Puzzle ' + str(date.today()) + '" && git push')
