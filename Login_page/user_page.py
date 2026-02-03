# user_page.py

import streamlit as st
import time
from activity_tracker import save_activity

class UserDashboard:
    def __init__(self):
        self.username = st.session_state.username
        self.role = st.session_state.role
        self.session_start = st.session_state.session_start
        self.dashboard_enter = st.session_state.dashboard_enter

    def render(self):
        st.title("👤 User Dashboard")
        st.write(f"Welcome, **{self.username}**")

        if st.button("Logout"):
            self.logout()

    def logout(self):
        dashboard_time = time.time() - self.dashboard_enter

        save_activity(
            self.username,
            self.role,
            self.session_start,
            dashboard_time
        )

        # Clear session safely
        for key in list(st.session_state.keys()):
            del st.session_state[key]

        st.success("Logged out successfully")
        st.stop()


def user_dashboard():
    dashboard = UserDashboard()
    dashboard.render()