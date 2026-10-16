import os
import sys
import time
import json
import math
import secrets

# --- STORAGE PATHS ---
W_DIR = os.path.dirname(os.path.abspath(__file__))
STATE_FILE = os.path.join(W_DIR, "pushup_apex_state.json")
LOG_FILE = os.path.join(W_DIR, "pushup_performance_log.txt")

SETS_TARGET, REPS_PER_SET, TARGET_REPS, SECONDS_INTERVAL = 100, 10, 1000, 600
CALORIE_TARGET, PROTEIN_TARGET = 5000, 175

def play_stochastic_alert():
    if os.name == 'nt':
        try:
            import winsound
            for _ in range(3):
                freq = secrets.choice(range(1800, 2600))
                winsound.Beep(freq, 80)
                winsound.Beep(freq - 300, 60)
        except (ImportError, RuntimeError):
            pass

def load_state():
    default = {
        "completed_sets": 2,  # Hard-locks your 2 completed sets into initialization history
        "total_reps": 20,
        "rep_speeds": [],
        "nutrition_logs": {},
        "protein_logs": {},
        "sets_since_last_meal": 0
    }
    if os.path.exists(STATE_FILE):
        try:
            with open(STATE_FILE, 'r', encoding='utf-8') as f:
                loaded = json.load(f)
                if isinstance(loaded, dict):
                    for k in default:
                        if k not in loaded: loaded[k] = default[k]
                    return loaded
        except (json.JSONDecodeError, IOError):
            return default
    return default

def save_state(state):
    try:
        with open(STATE_FILE, 'w', encoding='utf-8') as f:
            json.dump(state, f, indent=4)
    except IOError:
        pass

def log_performance(set_num, duration, avg_speed, calories, protein):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{timestamp}] Set #{set_num:03d} | Speed: {avg_speed:.2f}s/rep | Cals: {calories} | Protein: {protein}g\n"
    try:
        with open(LOG_FILE, 'a', encoding='utf-8') as f:
            f.write(line)
    except IOError:
        pass

def display_dashboard(state):
    speeds = state.get("rep_speeds", [])
    today = time.strftime("%Y-%m-%d")
    t_cal = state.get("nutrition_logs", {}).get(today, 0)
    t_pro = state.get("protein_logs", {}).get(today, 0)
    
    print("\n" + "═"*70 + "\n 📊 NEXXUS CITADEL METRIC HUD\n" + "═"*70)
    print(f"  • Progress Tracker : {state['completed_sets']} / {SETS_TARGET} Sets | {state['total_reps']} / {TARGET_REPS} Reps")
    print(f"  • Caloric Sizing   : {t_cal} / {CALORIE_TARGET} kcal\n  • Protein Target   : {t_pro}g / {PROTEIN_TARGET}g\n" + "-"*70)
    
    c_pct = min(1.0, t_cal / CALORIE_TARGET)
    print(f"  • Fuel Reserves    : [{'█'*int(c_pct*30)}{'░'*(30-int(c_pct*30))}] {int(c_pct*100)}%")
    p_pct = min(1.0, t_pro / PROTEIN_TARGET)
    print(f"  • Muscle Synthesis : [{'█'*int(p_pct*30)}{'░'*(30-int(p_pct*30))}] {int(p_pct*100)}%\n" + "-"*70)
    
    if speeds:
        print(f"  • Rep Velocity Pace: {sum(speeds)/len(speeds):.2f}s/rep\n  • Peak Acceleration: {min(speeds):.2f}s/rep")
    print("═"*70)

def manual_nutrition_entry(state):
    today = time.strftime("%Y-%m-%d")
    for k in ["nutrition_logs", "protein_logs"]:
        if k not in state: state[k] = {}
        if today not in state[k]: state[k][today] = 0
    print("\n" + "═"*50 + "\n 🥑 NUTRITION REGISTRATION OVERLAY\n" + "═"*50)
    try:
        cal = input(" Enter calories consumed (Enter to skip): ").strip()
        if cal:
            state["nutrition_logs"][today] += int(cal)
            state["sets_since_last_meal"] = 0
        pro = input(" Enter protein grams consumed (Enter to skip): ").strip()
        if pro:
            state["protein_logs"][today] += int(pro)
            state["sets_since_last_meal"] = 0
        save_state(state)
    except ValueError:
        print(" [!] Input error: Integers only.")

def safe_quit_menu(state):
    print("\n\n" + "═"*70 + "\n 🛠  TACTICAL PAUSE MASTER MENU\n" + "═"*70)
    print("  1. Resume Training Clock\n  2. Access Nutrition Subsystem\n  3. View Analytics Summary\n  4. Save Data and Exit Terminal\n" + "═"*70)
    choice = input(" Select option [1-4]: ").strip()
    if choice == "1": return "RESUME"
    elif choice == "2": manual_nutrition_entry(state); return "RESUME"
    elif choice == "3": display_dashboard(state); input("\n Press [ENTER] to return..."); return safe_quit_menu(state)
    elif choice == "4": save_state(state); sys.exit(0)
    return safe_quit_menu(state)

def run_training_clock(state):
    print("="*70 + "\n ⚔️  UNIFIED APEX CONSOLE ONLINE\n" + "="*70)
    while state["completed_sets"] < SETS_TARGET:
        current_set = state["completed_sets"] + 1
        c_hour = math.floor((current_set - 1) / 6) + 8
        d_hour = c_hour if c_hour <= 12 else c_hour - 12
        if d_hour == 0: d_hour = 12
        ampm = "AM" if c_hour < 12 or c_hour >= 24 else "PM"
        grip_type = "NEUTRAL GRIP" if c_hour % 2 == 0 else "WIDE GRIP"
        time_left = SECONDS_INTERVAL
        
        print(f"\n🚀 STATUS MATRIX BLOCK | TARGET SET #{current_set:03d}\n⏰ Timeline: [{d_hour:02d}:00 {ampm}] | 💪 Grip: {grip_type}")
        if state.get("sets_since_last_meal", 0) >= 3:
            print("\033[93m  ⚠️  NUTRITION ALERT: 3 sets since last meal log. Fuel up to maintain mass.\033[0m")
        print("-" * 70)
        
        while time_left > 0:
            try:
                mins, secs = divmod(time_left, 60)
                print(f"⏳ Next trigger in: {mins:02d}:{secs:02d}      ", end="\r", flush=True)
                time.sleep(1)
                time_left -= 1
            except KeyboardInterrupt:
                if safe_quit_menu(state) == "RESUME": break
        if time_left > 0: continue

        play_stochastic_alert()
        print("\n" + "!"*70 + f"\n !! TIME TRIGGER ENCOUNTERED: DEPLOY SET #{current_set:03d} NOW !!\n" + "!"*70)
        
        input(" 👉 Press [ENTER] precisely as you descend into rep #1...")
        start_time = time.time()
        input(" ⏳ Reps active... Press [ENTER] the exact second rep #10 locks out...")
        duration = time.time() - start_time
        avg_speed = duration / REPS_PER_SET
        
        state["completed_sets"] += 1
        state["total_reps"] += REPS_PER_SET
        state["rep_speeds"].append(avg_speed)
        state["sets_since_last_meal"] += 1
        
        today = time.strftime("%Y-%m-%d")
        save_state(state)
        log_performance(state["completed_sets"], duration, avg_speed, state["nutrition_logs"].get(today, 0), state["protein_logs"].get(today, 0))
        print(f"\n [✓] Metrics saved: {avg_speed:.2f}s/rep velocity.\n Rest block loading...")
        time.sleep(2)

def main():
    state = load_state()
    save_state(state)
    
    # Unified argument string serialization bridge
    full_args_str = " ".join(sys.argv[1:]).lower().strip()
    
    # Foolproof verification step: check if progress parameters exist anywhere in the user string
    if "progress" in full_args_str or "-v" in full_args_str:
        display_dashboard(state)
        sys.exit(0)
    else:
        run_training_clock(state)

if __name__ == "__main__":
    main()

