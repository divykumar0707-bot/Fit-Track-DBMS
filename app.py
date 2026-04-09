from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3
from datetime import date

app = Flask(__name__)
app.secret_key = "fittrack_secret_key_123"   # Required for sessions (login)

DB_FILE = "/home/luffy/code/fittrack/fittrack.db"

# Helper to connect to database
def get_db():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn

# ==================== ROUTES ====================

# Home / Dashboard
@app.route("/")
def index():
    if "user_id" not in session:
        return redirect(url_for("login"))
    
    user_id = session["user_id"]
    username = session["username"]
    
    conn = get_db()
    workouts_count = conn.execute("SELECT COUNT(*) FROM Workouts WHERE user_id = ?", (user_id,)).fetchone()[0]
    goals_count = conn.execute("SELECT COUNT(*) FROM Goals WHERE user_id = ?", (user_id,)).fetchone()[0]
    conn.close()
    
    return render_template("dashboard.html", 
                           username=username, 
                           workouts_count=workouts_count, 
                           goals_count=goals_count)

# Login Page
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        
        conn = get_db()
        user = conn.execute("SELECT * FROM Users WHERE username = ?", (username,)).fetchone()
        conn.close()
        
        if user and user["password"] == password:
            session["user_id"] = user["user_id"]
            session["username"] = user["username"]
            flash("Welcome back!", "success")
            return redirect(url_for("index"))
        else:
            flash("Invalid username or password", "danger")
    
    return render_template("login.html")

# Register Page
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        
        conn = get_db()
        try:
            conn.execute("INSERT INTO Users (username, password) VALUES (?, ?)", 
                        (username, password))
            conn.commit()
            flash("Registration successful! Please login.", "success")
            return redirect(url_for("login"))
        except sqlite3.IntegrityError:
            flash("Username already taken. Try another.", "danger")
        finally:
            conn.close()
    
    return render_template("register.html")

# Logout
@app.route("/logout")
def logout():
    session.clear()
    flash("You have been logged out.", "info")
    return redirect(url_for("login"))

# Log Workout Page
@app.route("/log_workout", methods=["GET", "POST"])
def log_workout():
    if "user_id" not in session:
        return redirect(url_for("login"))
    
    if request.method == "POST":
        user_id = session["user_id"]
        activity_type = request.form.get("activity_type")
        try:
            duration_minutes = int(request.form.get("duration_minutes"))
        except:
            flash("Please enter a valid duration", "danger")
            return render_template("log_workout.html")
        
        calories_input = request.form.get("calories_burned")
        calories_burned = int(calories_input) if calories_input and calories_input.strip() else None
        
        notes = request.form.get("notes")
        today = str(date.today())
        
        conn = get_db()
        try:
            conn.execute('''
                INSERT INTO Workouts 
                (user_id, workout_date, activity_type, duration_minutes, calories_burned, notes)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (user_id, today, activity_type, duration_minutes, calories_burned, notes))
            conn.commit()
            flash("✅ Workout logged successfully!", "success")
            return redirect(url_for("index"))
        except Exception as e:
            flash(f"Error logging workout: {str(e)}", "danger")
        finally:
            conn.close()
    
    return render_template("log_workout.html")

# View My Workouts
@app.route("/workouts")
def view_workouts():
    if "user_id" not in session:
        return redirect(url_for("login"))
    
    user_id = session["user_id"]
    
    conn = get_db()
    workouts = conn.execute('''
        SELECT workout_id, workout_date, activity_type, duration_minutes, 
               calories_burned, notes, created_at 
        FROM Workouts 
        WHERE user_id = ? 
        ORDER BY workout_date DESC, created_at DESC
    ''', (user_id,)).fetchall()
    conn.close()
    
    return render_template("workouts.html", workouts=workouts)

# Goals Routes
@app.route("/goals", methods=["GET", "POST"])
def goals():
    if "user_id" not in session:
        return redirect(url_for("login"))
    
    user_id = session["user_id"]
    
    # Handle setting new goal (POST)
    if request.method == "POST":
        goal_type = request.form.get("goal_type")
        try:
            target_value = float(request.form.get("target_value"))
        except:
            flash("Please enter a valid target value", "danger")
            return redirect(url_for("goals"))
        
        target_date = request.form.get("target_date") or None
        
        conn = get_db()
        try:
            conn.execute('''
                INSERT INTO Goals (user_id, goal_type, target_value, target_date)
                VALUES (?, ?, ?, ?)
            ''', (user_id, goal_type, target_value, target_date))
            conn.commit()
            flash("✅ Goal set successfully!", "success")
        except Exception as e:
            flash(f"Error: {str(e)}", "danger")
        finally:
            conn.close()
    
    # Fetch all goals for display
    conn = get_db()
    goals_list = conn.execute('''
        SELECT goal_id, goal_type, target_value, target_date, is_active, created_at 
        FROM Goals 
        WHERE user_id = ? 
        ORDER BY created_at DESC
    ''', (user_id,)).fetchall()
    conn.close()
    
    return render_template("goals.html", goals=goals_list)


@app.route("/goals/delete/<int:goal_id>")
def delete_goal(goal_id):
    if "user_id" not in session:
        return redirect(url_for("login"))
    
    conn = get_db()
    conn.execute("DELETE FROM Goals WHERE goal_id = ? AND user_id = ?", 
                (goal_id, session["user_id"]))
    conn.commit()
    conn.close()
    flash("Goal deleted successfully", "info")
    return redirect(url_for("goals"))

if __name__ == "__main__":
    app.run(debug=True)