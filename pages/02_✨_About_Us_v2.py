import streamlit as st

images_dir = "./images"
favicon_path = f"{images_dir}/favicon.ico"

col1, col2, col3 = st.columns([2,4,2])

with col1:
    st.markdown("## Me ##")
    st.image("./images/favicon.png")#, width=200)
    st.markdown("Lead Plasma Research Physicist")
    st.write("/ Senior Director of Nuclear Power and Artificial Intelligence")


with col2:
    st.markdown("## MiniMe ##")
    st.image("./images/tommy_boi.webp", width=200)
    st.write("Plasma Research Non-Physicist")

with col3:
    st.write("## MiniMe-MiniMe / MiniYou ##")
    st.image("./images/slack.png")#, width=200)
    st.text("Plasma Research Physicist **Intern**")
