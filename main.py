from langchain_helper import generate_team_name
import streamlit as st


page_bg_img = '''
<style>

[ data-testid="stAppViewContainer"] {
background-image: url("https://img.freepik.com/free-photo/office-supplies-with-keyboard-gray-desk_23-2148052624.jpg?w=2000&t=st=1697123051~exp=1697123651~hmac=b1e4ef7975df9d6b938d1102f394f492a74c576b73b28d4ee7d8fd6e0b5966a6");

background-size: cover;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)

st.title("Hackathon Team Name Generator")

company_name = st.text_input("Company Name")
theme_name = st.text_input("Theme of the hack")
problem_name = st.text_input("Problem Statement")
idea_name = st.text_input("Idea(if any yet)")

if st.button("Generate Team Names"):
    team_name = generate_team_name(company_name, theme_name, problem_name, idea_name)

    st.subheader("Here are some awesome team names:")
    st.write(team_name)


