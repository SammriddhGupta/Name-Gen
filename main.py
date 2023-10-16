from langchain_helper import generate_team_name
import streamlit as st

page_bg_img = '''
<style>
[ data-testid="stAppViewContainer"] {
    background-image: url('https://images.unsplash.com/photo-1488998427799-e3362cec87c3?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=3540&q=80');
    background-size: cover; 
    background-position: center center;
    background-repeat: no-repeat; 
    background-attachment: fixed;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)

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


