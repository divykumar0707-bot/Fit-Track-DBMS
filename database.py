import sqlite3
from datetime import datetime

DB_FILE = "/home/luffy/code/fittrack/fittrack.db"

def get_connection():
    """Returns a connection and cursor"""
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row   
    return conn, conn.cursor()

def initialize_database():
    """Create all tables if they don't exist"""
    conn, c = get_connection()
    
 
    c.execute('''
    CREATE TABLE IF NOT EXISTS Users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        age INTEGER,
        weight REAL,
        height REAL,
        goal_calories INTEGER DEFAULT 2000,
        created_at TEXT DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    
    c.execute('''
    CREATE TABLE IF NOT EXISTS Workouts (
        workout_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        workout_date TEXT NOT NULL,
        activity_type TEXT NOT NULL,
        duration_minutes INTEGER NOT NULL,
        calories_burned INTEGER,
        notes TEXT,
        created_at TEXT DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE
    )
    ''')
    
    c.execute('''
    CREATE TABLE IF NOT EXISTS Goals (
        goal_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        goal_type TEXT NOT NULL,
        target_value REAL,
        target_date TEXT,
        is_active INTEGER DEFAULT 1,
        created_at TEXT DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE
    )
    ''')
    
    conn.commit()
    conn.close()
    print("Database initialized.")

def add_user(username, password, age=None, weight=None, height=None):
    """Register new user - returns user_id or None if failed"""
    conn, c = get_connection()
    try:
        c.execute('''
        INSERT INTO Users (username, password, age, weight, height)
        VALUES (?, ?, ?, ?, ?)
        ''', (username, password, age, weight, height))
        conn.commit()
        return c.lastrowid
    except sqlite3.IntegrityError:
        return None
    finally:
        conn.close()

def get_user_by_username(username):
    """Return user row (as dict-like) or None"""
    conn, c = get_connection()
    c.execute("SELECT * FROM Users WHERE username = ?", (username,))
    user = c.fetchone()
    conn.close()
    return user

def add_workout(user_id, workout_date, activity_type, duration_minutes, notes=None, calories_burned=None):
    conn, c = get_connection()
    try:
        c.execute('''
            INSERT INTO Workouts 
            (user_id, workout_date, activity_type, duration_minutes, notes, calories_burned)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (user_id, workout_date, activity_type, duration_minutes, notes, calories_burned))
        
        conn.commit()
        return True, "Workout logged successfully!"
    except Exception as e:
        conn.rollback()
        return False, f"Error logging workout: {str(e)}"
    finally:
        conn.close()

def get_workouts(user_id):
    """Fetch all workouts for a user, newest first"""
    conn, c = get_connection()
    c.execute('''
        SELECT workout_date, activity_type, duration_minutes, calories_burned, notes
        FROM Workouts
        WHERE user_id = ?
        ORDER BY workout_date DESC
    ''', (user_id,))
    workouts = c.fetchall()
    conn.close()
    return workouts