# https://image-coordinates.streamlit.app/dynamic_update
# https://github.com/blackary/streamlit-image-coordinates

import streamlit as st

from streamlit_image_coordinates import streamlit_image_coordinates

value = streamlit_image_coordinates("https://placekitten.com/200/300")

st.write(value)
