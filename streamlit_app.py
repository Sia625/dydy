import streamlit as st
from page_content.home import home_page
from page_content.resume import resume_page
from page_content.contact import contact_page
from page_content.education import education_page
from page_content.experience import experience_page

st.set_page_config(page_title="Wu Siye's Portfolio", layout="wide")

pages = {
    "Home": home_page,
    "Resume": resume_page,
    "Contact": contact_page,
    "Education": education_page,
    "Experience": experience_page
}

selected_page = st.sidebar.selectbox("Navigation", list(pages.keys()))
pages[selected_page]()
