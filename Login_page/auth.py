import streamlit as st
import time
import hashlib

# HARDCODED USERS (ENCODED PASSWORDS)
USERS = {
    "admin1": {
        "password": hashlib.sha256("admin123".encode()).hexdigest(),
        "role": "admin"
    },
    "user1": {
        "password": hashlib.sha256("user123".encode()).hexdigest(),
        "role": "user"
    },
    "user2": {
        "password": hashlib.sha256("user456".encode()).hexdigest(),
        "role": "user"
    }
}

def login_page():
    st.title("🔐 Login")

    box = st.container()
    with box:
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        remember = st.checkbox("Remember me")
        login_btn = st.button("Login")

    if login_btn:
        encoded = hashlib.sha256(password.encode()).hexdigest()

        if username in USERS and USERS[username]["password"] == encoded:
            st.success("Login successful")

            st.session_state.logged_in = True
            st.session_state.username = username
            st.session_state.role = USERS[username]["role"]

            # Time tracking
            st.session_state.session_start = time.time()
            st.session_state.dashboard_enter = time.time()

        else:
            st.error("Invalid username or password")