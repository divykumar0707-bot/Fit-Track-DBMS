from database import initialize_database
from auth import register, login
from workouts import log_workout, view_workouts
from goals import set_goal , view_goals

def main():
    print("=====================================")
    print("      FitTrack Pro - Fitness Tracker")
    print("=====================================\n")

    initialize_database()
    
    current_user_id = None
    current_username = None
    
    while True:
        if current_user_id is None:
            print("\n1. Login")
            print("2. Register")
            print("0. Exit")
            choice = input("\nEnter choice: ").strip()
            
            if choice == "1":
                current_user_id, current_username = login()
            elif choice == "2":
                current_user_id, current_username = register()
            elif choice == "0":
                print("\nGoodbye!")
                break
            else:
                print("Invalid choice.")
                
        else:
            print(f"\nLogged in as: {current_username}")
            print("1. Log a workout")
            print("2. View my workouts")
            print("3. Set / view goals")
            print("4. Logout")
            choice = input("\nEnter choice: ").strip()
            
            if choice == "1":
                log_workout(current_user_id)
            elif choice == "2":
                view_workouts(current_user_id)
            elif choice == "3":
                
                while True:
                    print("\n--- Goals Menu ---")
                    print("1. Set new goal")
                    print("2. View my goals")
                    print("0. Back to main menu")
                    g_choice = input("\nEnter choice: ").strip()
                    
                    if g_choice == "1":
                        set_goal(current_user_id)
                    elif g_choice == "2":
                        view_goals(current_user_id)
                    elif g_choice == "0":
                        break
                    else:
                        print("Invalid choice. Please try again.")
            elif choice == "4":
                print(f"\nGoodbye, {current_username}!")
                current_user_id = None
                current_username = None
            else:
                print("Feature coming soon...")

if __name__ == "__main__":
    main()