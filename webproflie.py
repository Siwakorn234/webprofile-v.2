import streamlit as st

# Page configuration
st.set_page_config(page_title="Siwakorn Ruamlaph", page_icon="🔱")

# Title
st.title("🔱 Whoami")

# Introduction
st.subheader("I'm Siwakorn Ruamlaph (Pao)")
st.write("""
- 2023 - Recycle Fashion Science day 2023
- 2023 - RUMPHOEY MATH 
- 2024 - MUIC Open day 2024
- 2024 - First Aid and CPR Coure at Debsirin School
""")

# Current Activities
st.subheader("🧑‍💻 What I'm Doing Now")
st.write("""
- 💻 Studying In Math Science
- ⌨️ Pratice Html
""")

# Tech Stack & Skills
st.subheader("📚 Tech Stack & Skills")

# Programming Languages
with st.expander("👨‍💻 Programming Languages"):
    st.image("https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54", use_column_width=True)
    st.image("https://img.shields.io/badge/c++-%2300599C.svg?style=for-the-badge&logo=c%2B%2B&logoColor=white", use_column_width=True)
    st.image("https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E", use_column_width=True)

# Dev Tools
with st.expander("🐥 Dev Tools"):
    st.image("https://skillicons.dev/icons?i=git,github,gitlab,linux,ubuntu,neovim,raspberrypi,arduino", use_column_width=True)

# My Skills
st.subheader("🐥 My Skills")
st.image("https://skillicons.dev/icons?i=python,lcpp,java", use_column_width=True)

# Future Plans
st.subheader("🔮 What in Future")
st.write("""
- [ ] Study Computer Science 
- [ ] Have some game project
""")


