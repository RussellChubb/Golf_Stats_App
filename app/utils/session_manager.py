import streamlit as st

def login_user(username):
    st.session_state["user"] = username

def logout_user():
    st.session_state.pop("user", None)

def get_current_user():
    return st.session_state.get("user", None)

def is_logged_in():
    return "user" in st.session_state
