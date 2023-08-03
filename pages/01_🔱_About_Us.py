"""Streamlit tab example."""
import streamlit as st

st.set_page_config(
    page_title = "about_us_tabs",
    page_icon="🧊",
)

tab1, tab2, tab3 = st.tabs(["Me", "MiniMe", "MiniMe-MiniMe / MiniYou"])

with tab1:
   st.header("Senior Director of Nuclear Power and Artificial Intelligence")
   st.image("./images/favicon.png", width=200)
   st.markdown("The title kind of says it all...", unsafe_allow_html=True)

with tab2:
   st.header("Plasma Research Non-Physicist")
   st.image("./images/tommy_boi.webp", width=200)

with tab3:
   st.header("Plasma Research Physicist Intern")
   # st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
   st.image("./images/slack.png", width=200)

with tab3:
   st.markdown("maybe one day...", unsafe_allow_html=True)

with tab1:
   st.markdown('Recently promoted from "Lead Plasma Research Physicist"')
