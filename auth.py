from database import get_user_by_username, add_user

def register():
    print("\n--- Register New User ---")
    while True:
        username = input("Choose username: ").strip()
        if not username:
            print("Username cannot be empty.")
            continue
        if get_user_by_username(username):
            print("Username already taken. Try another.")
            continue
        break
    
    password = input("Choose password: ").strip()
    if not password:
        print("Password cannot be empty.")
        return None
    
    try:
        age = int(input("Age (optional, press Enter to skip): ") or 0)
        if age == 0: age = None
    except ValueError:
        age = None
    
    try:
        weight = float(input("Weight in kg (optional): ") or 0)
        if weight == 0: weight = None
    except ValueError:
        weight = None
    
    try:
        height = float(input("Height in cm (optional): ") or 0)
        if height == 0: height = None
    except ValueError:
        height = None
    
    user_id = add_user(username, password, age, weight, height)
    if user_id:
        print(f"\nWelcome, {username}! Registration successful.")
        return user_id, username
    else:
        print("Registration failed. Try again.")
        return None, None

def login():
    print("\n--- Login ---")
    username = input("Username: ").strip()
    password = input("Password: ").strip()
    
    user = get_user_by_username(username)
    if user and user['password'] == password:
        print(f"\nWelcome back, {username}!")
        return user['user_id'], username
    else:
        print("Invalid username or password.")
        return None, None