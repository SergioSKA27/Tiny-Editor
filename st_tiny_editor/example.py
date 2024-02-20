from st_tiny_editor import tiny_editor
import streamlit as st


d = tiny_editor(st.secrets["TINY_API_KEY"],
height=1000,
initialValue="<p>Hello World</p>",
toolbar = 'undo redo | blocks fontfamily fontsize | bold italic underline strikethrough | link image media table | align lineheight | numlist bullist indent outdent | emoticons charmap | removeformat')

st.write(d,unsafe_allow_html=True)
