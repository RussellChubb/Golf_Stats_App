import streamlit as st
import pandas as pd
import bcrypt
import os
from utils.session_manager import login_user, logout_user, get_current_user

PROFILE_PATH = "data/PlayerProfiles.csv"
os.makedirs("data", exist_ok=True)

st.title("🔐 Login or Sign Up")

if os.path.exists(PROFILE_PATH):
    profiles_df = pd.read_csv(PROFILE_PATH)
else:
    profiles_df = pd.DataFrame(columns=["Player", "Username", "PasswordHash", "PhotoPath", "HandicapGoal", "ScoreGoal", "Notes"])

# Logout button
if get_current_user():
    st.info(f"Logged in as {get_current_user()}")
    if st.button("🚪 Log Out"):
        logout_user()
        st.success("Logged out successfully!")
    st.stop()

tabs = st.tabs(["Login", "Sign Up"])

# --- Login tab ---
with tabs[0]:
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        user_row = profiles_df.loc[profiles_df["Username"] == username]
        if not user_row.empty:
            stored_hash = user_row.iloc[0]["PasswordHash"].encode("utf-8")
            if bcrypt.checkpw(password.encode("utf-8"), stored_hash):
                login_user(username)
                st.success(f"Welcome back, {user_row.iloc[0]['Player']}!")
                st.rerun()
            else:
                st.error("Incorrect password.")
        else:
            st.error("Username not found.")

# --- Signup tab ---
with tabs[1]:
    new_username = st.text_input("Create Username")
    new_password = st.text_input("Create Password", type="password")
    display_name = st.text_input("Display Name")
    if st.button("Sign Up"):
        if new_username in profiles_df["Username"].values:
            st.error("That username is already taken.")
        elif len(new_password) < 4:
            st.error("Password too short.")
        else:
            hashed_pw = bcrypt.hashpw(new_password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
            new_user = pd.DataFrame([{
                "Player": display_name,
                "Username": new_username,
                "PasswordHash": hashed_pw,
                "PhotoPath": "",
                "HandicapGoal": "",
                "ScoreGoal": "",
                "Notes": ""
            }])
            profiles_df = pd.concat([profiles_df, new_user], ignore_index=True)
            profiles_df.to_csv(PROFILE_PATH, index=False)
            st.success("Account created! You can now log in.")
