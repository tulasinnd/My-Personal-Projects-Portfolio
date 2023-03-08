import streamlit as st

# Set page config
st.set_page_config(page_title="My Portfolio", page_icon=":guardsman:", layout="wide")

# Define styles
st.markdown("""
    <style>
        body {
            background-color: #F5F5F5;
            font-family: 'Helvetica', sans-serif;
        }

        h1 {
            color: #1E90FF;
            text-align: center;
            font-size: 50px;
            margin-top: 50px;
        }

        h2 {
            color: #1E90FF;
            font-size: 30px;
            margin-top: 30px;
            margin-bottom: 20px;
        }

        p {
            font-size: 20px;
            line-height: 1.5;
            margin-bottom: 20px;
        }

        a {
            color: #1E90FF;
        }
    </style>
""", unsafe_allow_html=True)

# Add content
st.write("<h1>My Portfolio</h1>", unsafe_allow_html=True)
st.write("<h2>About Me</h2>", unsafe_allow_html=True)
st.write("<p>I am a web developer with experience in Python, Django, and Flask.</p>", unsafe_allow_html=True)
st.write("<p>Check out my <a href='https://github.com/myusername'>GitHub</a> for more projects.</p>", unsafe_allow_html=True)
