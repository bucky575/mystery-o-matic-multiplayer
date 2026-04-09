import json, hashlib, subprocess
from datetime import date

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
    print("⚙️  Running puzzle generator...")
    subprocess.run(
        ["mystery-o-matic", "scenarios/simple.template.sol", "static", "out"],
        check=True
    )
    with open("out/data.js", "r") as f:
        content = f.read().strip()
    if content.startswith("data ="):
        content = content[6:].strip().rstrip(";")
    return json.loads(content)

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