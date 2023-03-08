import streamlit as st

# Set page title
st.set_page_config(page_title="My Portfolio")

# Add title with pink color
st.write(
    f'<h1 style="color:#ff69b4;">My Portfolio</h1>',
    unsafe_allow_html=True
)
