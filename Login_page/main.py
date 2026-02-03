import streamlit as st
from auth import login_page
from admin_page import admin_dashboard
from user_page import user_dashboard

st.set_page_config(page_title="Login System", layout="centered")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    login_page()
else:
    if st.session_state.role == "admin":
        admin_dashboard()
    else:
        user_dashboard()