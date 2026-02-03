# admin_page.py

import streamlit as st
import json
import pandas as pd
import os

FILE = "data/user_activity.json"

class AdminDashboard:
    def __init__(self):
        self.file = FILE

    def load_data(self):
        if not os.path.exists(self.file):
            return pd.DataFrame()

        records = []
        with open(self.file, "r") as f:
            for line in f:
                records.append(json.loads(line))

        return pd.DataFrame(records)

    def render(self):
        st.title("🛠 Admin Dashboard")

        df = self.load_data()

        if df.empty:
            st.info("No user activity available")
            return

        st.subheader("User Activity Log")
        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )


def admin_dashboard():
    dashboard = AdminDashboard()
    dashboard.render()