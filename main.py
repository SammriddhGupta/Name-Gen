from langchain_helper import generate_team_name
import streamlit as st

st.title("Hackathon Team Name Generator")
st.subheader("Save precious time and get hacking faster!")

company_name = st.text_input("Company Name")
theme_name = st.text_input("Theme of the hack")
problem_name = st.text_input("Problem Statement")
idea_name = st.text_input("Your Idea (if any yet)")

if st.button("Generate 20 Team Names"):
    team_name = generate_team_name(company_name, theme_name, problem_name, idea_name)

    st.subheader("Here are some awesome team names:")
    st.write(team_name)