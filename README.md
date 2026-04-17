# 💪 FitTrack Pro - Fitness Tracker

A comprehensive console and web-based Fitness Tracking Application developed for DBMS Laboratory. It enables users to register, login, log workouts, view history, and manage fitness goals with a clean and responsive interface.

-[FitTrack Pro](https://img.shields.io/badge/FitTrack_Pro-Fitness_Tracker-blue)
-[Python](https://img.shields.io/badge/Python-3.12+-3776AB?logo=python)
-[Flask](https://img.shields.io/badge/Flask-3.0+-000000?logo=flask)
-[SQLite](https://img.shields.io/badge/SQLite-3.45+-003B57?logo=sqlite)

# Project Members
1. Divy Kumar              --->      RA2411030030066
2. Sudhanshu Singh Chauhan --->      RA2411030030074

## 📁 Project Documents

| Sr | Description                                  | Link |
|----|----------------------------------------------|------|
| 1  | Project Code                                | [View on GitHub](https://github.com/divykumar0707-bot/Fit-Track-DBMS?tab=readme-ov-file) |
| 2  | Project Report                              | [Download PDF](documents/projectreport.pdf) |
| 3  | Final PPT                                   | [view PPT](#) |
| 4  | RA2411030030066_Certificate                 | [Download Certificate](documents/divydbmscert.pdf) |
| 5  | RA2411030030074_Certificate                 | [Download Certificate](documents/sudhanshucoursecert.jpeg) |
| 6  | RA2411030030066_CourseReport                | [Download Course Report](dbmscoursereportdivy.pdf) |
| 7  | RA2411030030074_CourseReport                | [Download Course Report](dbmscoursereportsudhanshu.pdf) |

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

### User Features
- 🔐 Secure Authentication - Registration and login system
- 📝 Workout Logging - Log workouts with activity type, duration, calories & notes
- 📋 Workout History - View all logged workouts in a clean table
- 🎯 Goal Management - Set and track personal fitness goals
- 📊 Dashboard - Overview with workout statistics and active goals
- 🌐 Web Interface - Modern responsive web version using Flask

### Console Version
- Simple menu-driven interface
- Input validation and error handling
- Automatic date tracking for workouts

### Web Version
- Clean Bootstrap 5 UI with gradient navbar
- Interactive forms and responsive tables
- Flash messages for user feedback

## 🛠 Tech Stack

### Backend & Core
- Python 3.12 - Core programming language
- SQLite3 - Embedded relational database
- Flask - Lightweight web framework

### Frontend (Web Version)
- HTML5 + Bootstrap 5 - Responsive UI design
- Jinja2 - Template rendering
- Font Awesome - Icons

## 📋 Prerequisites

- Python 3.10 or higher
- pip (Python package manager)
- Git

### 💻 Installation
- Step 1: Clone the Repository
    Bashgit clone https://github.com/divykumar0707-bot/Fit-Track-DBMS.git
    cd Fit-Track-DBMS
- Step 2: Install Dependencies
    Bashpip install flask


## 🚀 Running the Application
- Console Version
    Bashpython3 main.py
- Web Version (Recommended for Demo)
    Bashpython3 app.py
    Then open your browser and go to:
        http://127.0.0.1:5000
### 📁 Project Structure
textFit-Track-DBMS/
├── app.py                    # Flask web application
├── main.py                   # Console version
├── database.py               # Database operations
├── auth.py                   # Authentication
├── workouts.py               # Workout features
├── goals.py                  # Goal features
├── templates/                # HTML templates
└── fittrack.db               # SQLite database

## 📊 DBMS Concepts Demonstrated

- Relational Database Design (3NF)
- Primary Keys, Foreign Keys & Referential Integrity
- CRUD Operations (Create & Read)
- Parameterized Queries (SQL Injection Prevention)
- Modular Code Architecture

## 🔮 Future Enhancements

- Delete workout and goal functionality
- Automatic calorie estimation
- Progress tracking with charts
- Export data to CSV
