Pocket Expense Tracker (CLI)

A lightweight, Python-based Command Line Interface (CLI) application for daily expense logging and management.

This project, developed for the Expense Management System, provides college students and individuals with a simple, distraction-free tool to track personal finances without the complexity of traditional financial apps.

Problem Statement

Students and individuals often struggle to maintain a consistent record of their daily spending due to the friction of using complex apps or procrastination. This lack of tracking leads to:

Overspending before the month ends.

Lack of awareness about specific spending habits (e.g., spending too much on food vs. travel).

Loss of data when relying on physical notebooks.

The Solution: The Pocket Expense Tracker offers a simple, terminal-based solution focused on speed, simplicity, and data persistence using local CSV files, ensuring the user stays in control of their financial data.

Features

The application is built around core command-line functionalities for easy daily use:

Add Expense Module:

Logs expense details (Category, Amount, optional Note).

Automatically captures the current date.

Validates numeric input for the amount.

View & Tracking Module:

View All: Displays a formatted table of all recorded expenses.

Category View: Filters expenses based on a user-provided category.

Total Calculation: Computes and displays the grand total of all expenses.

Management Module:

Delete Expense: Allows users to remove entries by index number.

Exit: Safely closes the application.

System Architecture & Technology

Platform: Command Line Interface (CLI)

Language: Python 3

Storage: Local CSV file (expenses.csv) for persistent data storage.

Structure: Modular script structure with separated functions (main, add_data, view_list, etc.).

Design Rationale (Non-Functional Requirements): Focuses on instant launch performance, simple menu-based navigation (1-6), auto-saving reliability, and portability using standard Python libraries.

How to Run

Prerequisites: Ensure you have Python 3 installed.

Clone the Repository:

git clone https://github.com/Roopeshsingh15/Budget-management-.git
cd expense-management-system





Future Enhancements

Visualization: Integrate matplotlib to generate and display a pie chart of expenses by category.

GUI Interface: Port the core logic to a desktop interface using Tkinter or PyQt for an improved user experience.

Project Information:

Name: Roopesh Singh

Registration No.: 25BAI11006

Department: BTECH CSE AIML

Institute: VIT Bhopal
