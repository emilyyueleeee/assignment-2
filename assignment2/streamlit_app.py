# run it as streamlit file

import streamlit as st

# Function to recommend music based on score
def recommend_music(score):
    if score >= 9:
        return "Sugar by Maroon 5", r"music/Sugar.mp3"
    elif score >= 7:
        return "Peaches by Justin Bieber", r"music/Peaches-Justin Bieber.mp3"
    elif score >= 5:
        return "Someone Like You by Adele", r"music/Someone Like You-Adele.mp3"
    elif score >= 3:
        return "Love Yourself by Justin Bieber", r"music/Love Yourself-Justin Bieber.mp3"
    else:
        return "See You Again by Charlie Puth", r"music/See You Again-Charlie Puth.mp3"

# Title of the app
st.title("Mood-Based Music Recommendation")

# Input for user's mood score
score = st.number_input("Enter your mood score (0-10):", min_value=0, max_value=10, step=1)

# Button to get music recommendation
if st.button("Get Recommendation"):
    song, audio_file = recommend_music(score)
    
     # Use st.markdown to make the song title prettier with larger font and bold text
    st.markdown(f"<h3 style='text-align: center; color: hotpink;'>Recommended music: <em>{song}</em></h3>", unsafe_allow_html=True)
    
    # Use st.audio for playing local files
    st.audio(audio_file)