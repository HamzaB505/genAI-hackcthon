import streamlit as st
from st_pages import Page, show_pages, add_page_title
from tahseenai import AImodels_loader

st.set_page_config(page_title="Tahseen AI --- تحسين",
                   page_icon="robot_face",
                   layout="wide",
                   initial_sidebar_state="expanded")

# Setup of page names, just add a page path and it's name and icon
show_pages(
            [
                Page("app.py", "Home", ":house:"),
                Page("pages/about.py", "About Us", ":books:"),
                Page("pages/models.py", "Models", ":robot_face:"),
            ]
        )
st.title('TahseenAI')


with st.expander('Purpose of the app'):
    st.write("Insert a small descritpion")

#@st.cache_resource to cache methods instead of loading them each time


# st.session_state["someobject"] = someobject

st.divider()

st.subheader("Welcome to TahseenAI ! you all in one platform for AI course creation")



# add tahseenAI desciption here


st.write("description of service")


ai_loader = AImodels_loader()






