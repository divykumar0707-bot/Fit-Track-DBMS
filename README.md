# FitTrack Pro - Fitness Tracker

A complete **Fitness Tracking System** built as a DBMS Lab Project using Python and SQLite.

## Features

### Console Version
- User Registration & Login
- Log workouts with duration, calories & notes
- View workout history
- Set and view fitness goals
- Proper database relationships using Foreign Keys

### Web Version (Flask)
- Clean and responsive web interface
- Dashboard with statistics
- Log new workouts via web form
- View workouts in a beautiful table
- Set and manage goals
- Bootstrap 5 UI with modern design

## Technologies Used

- **Backend**: Python 3
- **Database**: SQLite3 (with proper schema design)
- **Web Framework**: Flask
- **Frontend**: HTML, Bootstrap 5, Font Awesome
- **Architecture**: Modular design (separation of concerns)

## Project Structure
fittrack/
├── app.py                 # Flask web application
├── database.py            # Database operations
├── auth.py                # User authentication
├── workouts.py            # Workout features
├── goals.py               # Goal features
├── main.py                # Console version
├── templates/             # HTML templates
└── fittrack.db            # SQLite database
text## How to Run

### Console Version
```bash
python3 main.py
Web Version
Bashpython3 app.py
Then open http://127.0.0.1:5000 in your browser.
