import os
import sys
import time
import json
import datetime
import winsound  # Standard Windows library for system audio alerts
from pathlib import Path

# Configuration & Workspace Paths
DESKTOP_PATH = Path(r"C:\Users\Anthony Frazier\OneDrive\Desktop")
WORKSPACE_DIR = DESKTOP_PATH / "sd-workspace"
DATA_FILE = WORKSPACE_DIR / "pushup_state.json"

# Targets
TOTAL_SETS_TARGET = 100
REPS_PER_SET = 10
CALORIE_TARGET = 3500
PROTEIN_TARGET = 262
INTERVAL_MINUTES = 10

def clear_screen():
    # Safe terminal flush clear mechanism to prevent system crashing
    sys.stdout.write("\033[H\033[2J")
    sys.stdout.flush()

def play_alert_sound():
    # Triggers a sharp system sound alert (Frequency: 1000Hz, Duration: 800ms)
    try:
        winsound.Beep(1000, 800)
    except Exception:
        sys.stdout.write("\a")
        sys.stdout.flush()

def load_state():
    if not WORKSPACE_DIR.exists():
        try:
            WORKSPACE_DIR.mkdir(parents=True, exist_ok=True)
        except IOError as e:
            sys.stderr.write(f"Failed to create workspace directory: {e}\n")
            return get_default_state()
        
    if DATA_FILE.exists():
        try:
            with open(DATA_FILE, 'r') as f:
                state = json.load(f)
                if state.get("date") != str(datetime.date.today()):
                    return get_default_state()
                return state
        except (json.JSONDecodeError, IOError) as e:
            sys.stderr.write(f"Error loading state file: {e}. Recovering default state.\n")
            return get_default_state()
    return get_default_state()

def get_default_state():
    return {
        "date": str(datetime.date.today()),
        "sets_completed": 0,
        "total_reps": 0,
        "calories_consumed": 0,
        "protein_consumed": 0,
        "streak_days": 1,
        "history": []
    }

def save_state(state):
    try:
        with open(DATA_FILE, 'w') as f:
            json.dump(state, f, indent=4)
    except IOError as e:
        sys.stderr.write(f"Database write verification failed: {e}\n")

def generate_ascii_graph(completed, target):
    bars = int((completed / target) * 20) if target > 0 else 0
    graph = "[" + "=" * bars + " " * (20 - bars) + "]"
    return graph

def display_dashboard(state, message=""):
    clear_screen()
    completed_sets = state["sets_completed"]
    total_reps = state["total_reps"]
    cals = state["calories_consumed"]
    prot = state["protein_consumed"]
    
    # Active hardware clock calls to pull live local system parameters
    current_date_str = datetime.date.today().strftime("%A, %B %d, %Y")
    current_time_str = datetime.datetime.now().strftime("%I:%M %p")
    
    print("=" * 60)
    print("           NEXUS CITADEL PUSH-UP TIMER ENGINE v2.5          ")
    print("=" * 60)
    print(f" {current_date_str} | Live Time: {current_time_str}")
    print(f" Daily Streak: {state['streak_days']} Days")
    print("-" * 60)
    
    set_graph = generate_ascii_graph(completed_sets, TOTAL_SETS_TARGET)
    print(f" Sets Completed: {completed_sets}/{TOTAL_SETS_TARGET} {set_graph} ({total_reps} Reps)")
    
    cal_graph = generate_ascii_graph(cals, CALORIE_TARGET)
    print(f" Calories Fuel:  {cals}/{CALORIE_TARGET} kcal {cal_graph}")
    
    prot_graph = generate_ascii_graph(prot, PROTEIN_TARGET)
    print(f" Protein Intake: {prot}/{PROTEIN_TARGET}g      {prot_graph}")
    print("-" * 60)
    
    if message:
        print(f" STATUS: {message}")
        print("-" * 60)

def export_desktop_report(state):
    report_file = DESKTOP_PATH / f"Pushup_Progress_Report_{state['date']}.txt"
    try:
        with open(report_file, 'w') as f:
            f.write(f"NEXUS CITADEL PERFORMANCE REPORT - {state['date']}\n")
            f.write("=" * 50 + "\n")
            f.write(f"Total Sets Completed: {state['sets_completed']}/{TOTAL_SETS_TARGET}\n")
            f.write(f"Total Repetitions: {state['total_reps']} reps\n")
            f.write(f"Calorie Target Tracking: {state['calories_consumed']}/{CALORIE_TARGET} kcal\n")
            f.write(f"Protein Target Tracking: {state['protein_consumed']}/{PROTEIN_TARGET}g\n")
            f.write(f"Current Daily Streak: {state['streak_days']} days\n")
            f.write("=" * 50 + "\n")
            f.write("Status: Core Execution Matrix Stable.\n")
    except IOError as e:
        sys.stderr.write(f"Report generation interrupted by storage conflict: {e}\n")

def run_countdown(state, seconds_remaining):
    start_time = time.time()
    total_duration = seconds_remaining
    
    while seconds_remaining > 0:
        display_dashboard(state, f"Countdown Active. Next set in: {seconds_remaining // 60:02d}:{seconds_remaining % 60:02d}")
        print("\n [Ctrl+C] Pause Engine Matrix Loop")
        
        time.sleep(1)
        elapsed = int(time.time() - start_time)
        seconds_remaining = total_duration - elapsed
        
        if seconds_remaining <= 0:
            break

    return 0

def main():
    state = load_state()
    
    if len(sys.argv) > 1:
        flag = sys.argv[1]
        if flag in ["progress", "-v", "--verbose"]:
            display_dashboard(state, "System Summary Readout Only.")
            sys.exit(0)
            
    while state["sets_completed"] < TOTAL_SETS_TARGET:
        display_dashboard(state, "Ready to begin next interval block.")
        print("\n Matrix Controls:")
        print(" [1] Start Next 10-Minute Countdown Loop")
        print(" [2] Manual Log Completed Reps (Force Override)")
        print(" [3] Update Nutrition Ingestion Data (Calories/Protein)")
        print(" [4] Export Current Summary Progress to Desktop")
        print(" [5] Reset Daily Matrix and Benchmarks")
        print(" [6] Exit Engine Terminal")
        
        choice = input("\n Select Action Execution Number: ").strip()
        
        if choice == "1":
            interval_secs = INTERVAL_MINUTES * 60
            run_countdown(state, interval_secs)
            
            play_alert_sound()
            
            clear_screen()
            print("\n" + "!" * 50)
            print(" TIMER COMPLETE: EXECUTE 10 PUSH-UP REPS NOW!")
            print("!" * 50 + "\n")
            
            confirm = input("Did you execute the 10 reps successfully? (y/n): ").strip().lower()
            if confirm == 'y':
                state["sets_completed"] += 1
                state["total_reps"] += REPS_PER_SET
                save_state(state)
                print("\nSet successfully locked into system database storage.")
                time.sleep(1.5)
                
        elif choice == "2":
            try:
                sets = int(input("Enter number of standard completed sets to add manually: "))
                state["sets_completed"] += sets
                state["total_reps"] += (sets * REPS_PER_SET)
                save_state(state)
            except ValueError:
                print("Invalid integer count block input values.")
                time.sleep(1)
                
        elif choice == "3":
            try:
                added_cals = int(input("Enter Calories (kcal) consumed: "))
                added_prot = int(input("Enter Protein mass (grams) consumed: "))
                state["calories_consumed"] += added_cals
                state["protein_consumed"] += added_prot
                save_state(state)
            except ValueError:
                print("Invalid nutrition numeric variables.")
                time.sleep(1)
                
        elif choice == "4":
            export_desktop_report(state)
            print(f"\nReport successfully exported directly to {DESKTOP_PATH}")
            time.sleep(2)
            
        elif choice == "5":
            confirm = input("Are you sure you want to clear completely? (y/n): ").strip().lower()
            if confirm == 'y':
                state = get_default_state()
                save_state(state)
                
        elif choice == "6":
            save_state(state)
            print("\nSaving configuration matrices... Shutting down core engine scripts safely.")
            sys.exit(0)
            
    display_dashboard(state, "CRITICAL OBJECTIVE ACHIEVED: 1000 PUSH-UPS LOGGED!")
    export_desktop_report(state)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nEngine processing suspended manually.")
        sys.exit(0)

