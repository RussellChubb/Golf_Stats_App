import streamlit as st
import pandas as pd
import os
from datetime import date
from utils.data_loader import load_user_data

PROFILE_PATH = "data/PlayerProfiles.csv"
IMAGE_DIR = "data/profile_images"

os.makedirs(IMAGE_DIR, exist_ok=True)

st.title("👤 Player Profile & Goals")

# Load or initialize profile data
if os.path.exists(PROFILE_PATH):
    profiles_df = pd.read_csv(PROFILE_PATH)
else:
    profiles_df = pd.DataFrame(columns=["Player", "PhotoPath", "HandicapGoal", "ScoreGoal", "Notes", "CreatedAt"])

players = profiles_df["Player"].unique().tolist() if not profiles_df.empty else []
player = st.selectbox("Select Player", players + ["➕ Add New Player"])

if player == "➕ Add New Player":
    new_name = st.text_input("Enter player name")
    uploaded_photo = st.file_uploader("Upload profile photo", type=["jpg", "png", "jpeg"])

    col1, col2 = st.columns(2)
    handicap_goal = col1.number_input("Handicap Goal", value=18.0)
    score_goal = col2.number_input("Score Goal", value=85)
    notes = st.text_area("Notes / Motivational Goal")

    if st.button("✅ Create Profile"):
        photo_path = ""
        if uploaded_photo:
            photo_path = os.path.join(IMAGE_DIR, f"{new_name}.jpg")
            with open(photo_path, "wb") as f:
                f.write(uploaded_photo.read())

        new_profile = pd.DataFrame([{
            "Player": new_name,
            "PhotoPath": photo_path,
            "HandicapGoal": handicap_goal,
            "ScoreGoal": score_goal,
            "Notes": notes,
            "CreatedAt": date.today()
        }])
        profiles_df = pd.concat([profiles_df, new_profile], ignore_index=True)
        profiles_df.to_csv(PROFILE_PATH, index=False)
        st.success(f"Profile created for {new_name}!")
else:
    profile = profiles_df.loc[profiles_df["Player"] == player].iloc[0]
    st.image(profile["PhotoPath"], width=150, caption=profile["Player"])
    st.write(f"**Handicap Goal:** {profile['HandicapGoal']}")
    st.write(f"**Score Goal:** {profile['ScoreGoal']}")
    st.write(f"**Motivation:** {profile['Notes']}")

    st.divider()
    st.subheader("🎯 Update Goals")

    new_handicap = st.number_input("Update Handicap Goal", value=float(profile["HandicapGoal"]))
    new_score = st.number_input("Update Score Goal", value=int(profile["ScoreGoal"]))
    new_notes = st.text_area("Update Notes", value=profile["Notes"])

    if st.button("💾 Save Changes"):
        profiles_df.loc[profiles_df["Player"] == player, ["HandicapGoal", "ScoreGoal", "Notes"]] = [
            new_handicap, new_score, new_notes
        ]
        profiles_df.to_csv(PROFILE_PATH, index=False)
        st.success("Profile updated successfully!")
