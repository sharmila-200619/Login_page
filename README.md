![WhatsApp Image 2026-02-03 at 7 50 33 AM (1)](https://github.com/user-attachments/assets/d477e033-d3f6-411c-9ee3-e3e7792d4936)# Login_page
Basic login page with both admin and user dashboard

# Login System with User Time Tracking

## 📌 Project Overview
This project is a **simple Python-based login system**
The main goal of the project is to:

- Allow users to log in through a basic login page
- Calculate how much time a user spends after login
- Display the recorded session details in an admin dashboard

The project focuses on **session time calculation**, not on advanced authentication or frontend design.

---

## 🎯 Objectives
- Create a basic login interface using Python
- Track the time spent by a user after login
- Store session timing data when the user logs out
- Allow the admin to view user session information

---

## 🛠️ Technologies Used
- **Python**
- **Streamlit** (for UI)
- **JSON** (for simple data storage)

---

## 📂 Project Structure
login_project/ │ ├── main.py                # Application entry point ├── auth.py                # Login page logic ├── user_page.py           # User dashboard & logout ├── admin_page.py          # Admin dashboard ├── activity_tracker.py    # Session time calculation │ └── data/ └── user_activity.json # Stored user session data
Copy code

---

## 🔐 Login Functionality
- Users log in using a **username and password**
- Passwords are stored in **encoded (hashed) format**
- Based on the role, the user is redirected to:
  - **User Dashboard**
  - **Admin Dashboard**

> Note: This project does **not** include registration, password reset, or database integration.

---

## ⏱️ Time Tracking Logic
- Session start time is recorded at login
- Logout time is captured when the user clicks **Logout**
- Total session time is calculated using:
Total Time = Logout Time − Login Time
Copy code

- The calculated time is stored in a JSON file
- Admin can view all recorded session timings

---

## 📊 Admin Dashboard
- Displays user session data in **tabular format**
- Shows:
  - Username
  - Role
  - Date
  - Login Time
  - Logout Time
  - Total Session Time

This helps in monitoring how long users stay logged in.

---

## 🖼️ Screenshots

### 🔹 Login Page
(https://github.com/user-attachments/assets/cb6353b4-6885-44d1-955e-0a4ed0b847cb)

### 🔹 Admin Dashboard

(https://github.com/user-attachments/assets/92007663-6304-4613-a29c-ed71c24976c5)



## ▶️ How to Run the Project!

1. Install required package:
```bash
pip install streamlit
Run the application:
Copy code
Bash
streamlit run main.py
✅ Features Implemented

Basic login page
Role-based navigation (Admin / User)
Session time calculation
JSON-based data storage
Admin activity monitoring

❌ Features Not Included

User registration
Database (MySQL / MongoDB)
Advanced UI design
Multi-device session handling
 
✍️ Author
Sharmila.L

📌 Conclusion
This project demonstrates how a simple login system can be used to calculate and store user session time using Python.
It emphasizes clarity, simplicity, and easy explanation rather than complex functionality.
