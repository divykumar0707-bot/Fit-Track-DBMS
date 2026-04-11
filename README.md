# 💪 FitTrack Pro - Fitness Tracker

A comprehensive console + web-based Fitness Tracking Application built for DBMS Lab. It allows users to register, login, log workouts, track progress, and manage fitness goals with a clean interface.

![FitTrack Pro](https://img.shields.io/badge/FitTrack_Pro-Fitness_Tracker-blue)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python)
![Flask](https://img.shields.io/badge/Flask-3.0+-000000?logo=flask)
![SQLite](https://img.shields.io/badge/SQLite-3.45+-003B57?logo=sqlite)


# Project Members
1. xxx --->      RAxxxxxxxxxx  
2. xxx --->      RAxxxxxxxxxx

## 📁 Project Documents

| Sr | Description                                  | Link |
|----|----------------------------------------------|------|
| 1  | Project Code                                | [View](#) |
| 2  | Project Report                              | [View](#) |
| 3  | Final PPT                                   | [View](#) |
| 4  | RAxxxxxxxxxx_Certificate                    | [View](#) |
| 5  | RAxxxxxxxxxx_Certificate                    | [View](#) |
| 6  | RAxxxxxxxxxx_CourseReport                   | [View](#) |
| 7  | RAxxxxxxxxxx_CourseReport                   | [View](#) |

## 📋 Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [Project Structure](#project-structure)
- [Screenshots](#screenshots)
- [DBMS Concepts Demonstrated](#dbms-concepts-demonstrated)
- [Future Enhancements](#future-enhancements)

## ✨ Features

### Core Features
- 🔐 **User Authentication** - Secure registration and login system
- 📝 **Workout Logging** - Log workouts with activity, duration, calories & notes
- 📋 **Workout History** - View all past workouts in a clean table
- 🎯 **Goal Management** - Set and track fitness goals
- 📊 **Dashboard** - Overview with workout count and active goals
- 🌐 **Web Interface** - Responsive Flask-based frontend

### Console Version
- Simple menu-driven interface
- Input validation and error handling
- Automatic date tracking

### Web Version
- Modern Bootstrap 5 UI
- Interactive forms and tables
- Real-time feedback with flash messages
- Responsive design for all devices

## 🛠 Tech Stack

### Backend & Core
- **Python 3** - Main programming language
- **SQLite3** - Lightweight relational database
- **Flask** - Web framework for the web version

### Frontend (Web)
- **HTML5 + Bootstrap 5** - Responsive UI
- **Font Awesome** - Icons
- **Jinja2** - Template engine

### Tools
- Modular Python architecture
- Parameterized SQL queries

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.10 or higher**
- **pip** (Python package manager)
- **Git**

### Verify Installation

```bash
python3 --version
pip --version
git --version

💻 Installation

Step 1: Clone the Repository:
  Bashgit clone https://github.com/divykumar0707-bot/Fit-Track-DBMS.git
  cd Fit-Track-DBMS
Step 2: Install Dependencies:
  Bashpip install flask
  🚀 Running the Application
 Console Version :
  Bashpython3 main.py
 Web Version :
  Bashpython3 app.py
Then open your browser and go to:
  http://127.0.0.1:5000

Fit-Track-DBMS/
├── app.py                    # Flask web application
├── main.py                   # Console version
├── database.py               # Database operations & schema
├── auth.py                   # User registration & login
├── workouts.py               # Workout logging & viewing
├── goals.py                  # Goal management
├── templates/                # HTML templates for web version
│   ├── base.html
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── log_workout.html
│   ├── workouts.html
│   └── goals.html
└── fittrack.db               # SQLite database file

📊 DBMS Concepts Demonstrated

Relational Database Design (3NF)
Primary Keys & Auto Increment
Foreign Keys with Referential Integrity
CRUD Operations (Create, Read)
Parameterized Queries (SQL Injection Prevention)
Data Validation & Constraints
Modular Code Architecture
Connection Management with row_factory

🔮 Future Enhancements

 Add workout deletion feature
 Implement basic calorie auto-calculation
 Add progress charts using Matplotlib/Plotly
 Monthly/Weekly summary reports
 Export data to CSV
 User profile management
 Dark mode in web version

🤝 Contributing

Fork the repository
Create your feature branch
Commit your changes
Push to the branch
Open a Pull Request


