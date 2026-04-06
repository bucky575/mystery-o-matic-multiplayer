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

def generate_puzzle():
    print("⚙️  Running generator...")
    subprocess.run(
        ["mystery-o-matic", "scenarios/simple.template.sol", "static", "out"],
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
    d = generate_puzzle()

    # Just insert the date — puzzle content served from static files
    result = supabase.table("rooms").insert({
        "puzzle_date": today
    }).execute()

    print(f"✅ Room created for {today}")
    print(f"   Room ID: {result.data[0]['id']}")

if __name__ == "__main__":
    push_to_supabase()
