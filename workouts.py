from database import add_workout
from datetime import date

def log_workout(user_id):
    print("\n--- Log a Workout ---")

    print("\nWhat did you do today?")
    print("  e.g. Chest Day, Leg Day, Back & Biceps, Cardio, Full Body...")
    while True:
        activity = input("Workout name: ").strip()
        if activity:
            break
        print("Workout name cannot be empty.")

    while True:
        try:
            duration = int(input("How long did you workout? (in minutes): ").strip())
            if duration <= 0:
                print("Duration must be greater than 0.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    while True:
        try:
            calories_input = input("Calories burned (press Enter to skip): ").strip()
            if calories_input == "":
                calories = None
                break
            calories = int(calories_input)
            if calories < 0:
                print("Calories cannot be negative.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    notes = input("Any notes? e.g. 'Increased bench press to 60kg' (press Enter to skip): ").strip()
    if not notes:
        notes = None

    today = str(date.today())

    success, message = add_workout(user_id, today, activity, duration, notes, calories)
    print(f"\n{message}")


def view_workouts(user_id):
    """Display all workouts for the logged-in user in a nice table"""
    from database import get_connection
    
    print("\n=== My Workouts ===")
    
    conn, c = get_connection()
    try:
        c.execute('''
            SELECT workout_id, workout_date, activity_type, duration_minutes, 
                   calories_burned, notes, created_at 
            FROM Workouts 
            WHERE user_id = ? 
            ORDER BY workout_date DESC, created_at DESC
        ''', (user_id,))
        
        workouts = c.fetchall()
        
        if not workouts:
            print("No workouts logged yet. Let's log your first workout!")
            return
        
        print(f"{'Date':<12} {'Workout Name':<25} {'Duration':<12} {'Calories':<10} Notes")
        print("-" * 85)
        
        for w in workouts:
            date_str = w['workout_date']
            activity = w['activity_type']
            if len(activity) > 23:
                activity = activity[:20] + "..."
            duration_str = f"{w['duration_minutes']} min"
            calories_str = str(w['calories_burned']) if w['calories_burned'] is not None else "-"
            notes_str = w['notes'] if w['notes'] else "-"
            
            print(f"{date_str:<12} {activity:<25} {duration_str:<12} {calories_str:<10} {notes_str}")
            
    except Exception as e:
        print(f"Error fetching workouts: {str(e)}")
    finally:
        conn.close()