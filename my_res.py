import streamlit as st

st.markdown("""
    <style>
        .big-font {
            font-size: 48px !important;
        }
        .title {
            background: linear-gradient(to right, #f6d365, #fda085);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="big-font title">My Portfolio</h1>', unsafe_allow_html=True)
