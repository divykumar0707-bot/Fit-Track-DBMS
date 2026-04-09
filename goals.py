from datetime import date
from database import get_connection

def set_goal(user_id):
    """Allow user to set a new fitness goal"""
    print("\n--- Set New Goal ---")
    
    print("\nCommon goal types:")
    print("  lose_weight, build_muscle, improve_endurance, maintain_weight, other")
    
    while True:
        goal_type = input("\nEnter goal type: ").strip().lower()
        if goal_type:
            break
        print("Goal type cannot be empty.")
    
    while True:
        try:
            target_value = float(input("Target value (e.g. 75 for target weight in kg): "))
            break
        except ValueError:
            print("Please enter a valid number.")
    
    target_date = input("Target date (YYYY-MM-DD, or press Enter to skip): ").strip()
    if not target_date:
        target_date = None
    
    conn, c = get_connection()
    try:
        c.execute('''
            INSERT INTO Goals 
            (user_id, goal_type, target_value, target_date)
            VALUES (?, ?, ?, ?)
        ''', (user_id, goal_type, target_value, target_date))
        
        conn.commit()
        print("\n✅ Goal set successfully!")
    except Exception as e:
        print(f"❌ Error setting goal: {str(e)}")
    finally:
        conn.close()


def view_goals(user_id):
    """Display all goals for the logged-in user"""
    print("\n=== My Goals ===")
    
    conn, c = get_connection()
    try:
        c.execute('''
            SELECT goal_id, goal_type, target_value, target_date, 
                   is_active, created_at 
            FROM Goals 
            WHERE user_id = ? 
            ORDER BY created_at DESC
        ''', (user_id,))
        
        goals = c.fetchall()
        
        if not goals:
            print("No goals set yet. Let's set your first goal!")
            return
        
    
        print(f"{'Goal Type':<20} {'Target Value':<15} {'Target Date':<15} {'Status'}")
        print("-" * 65)
        
        for g in goals:
            gtype = g['goal_type'].replace("_", " ").title()
            target = g['target_value']
            tdate = g['target_date'] if g['target_date'] else "-"
            status = "Active" if g['is_active'] == 1 else "Inactive"
            
            print(f"{gtype:<20} {target:<15} {tdate:<15} {status}")
            
    except Exception as e:
        print(f"Error fetching goals: {str(e)}")
    finally:
        conn.close()
