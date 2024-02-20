from st_tiny_editor import tiny_editor
import streamlit as st


d = tiny_editor('rbmpkoj5pz0ftietc5wnx0tei3dofocexwnxtrc9bvkl61aq',height=1000,initialValue="<p>Hello World</p>")




st.write(d,unsafe_allow_html=True)
