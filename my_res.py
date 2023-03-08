import streamlit as st
# Set page config
st.set_page_config(page_title="My Portfolio", page_icon=":guardsman:", layout="wide")

# Set background color
bgcolor = "skyblue"
page_bg = f"style='background-color:{bgcolor};'"
st.markdown(f'<body {page_bg}></body>', unsafe_allow_html=True)

# Create a function to display the homepage
def homepage():
    st.title("Welcome to my portfolio")
    st.write(
    f'<h1 style="color:#ff69b4;">MY PORTFOLIO</h1>',
    unsafe_allow_html=True
)

# Create a function to display the about page
def about():
    st.title("About Me")

# Create a function to display the contact page
def contact():
    st.title("Contact Me")

# Define the pages dictionary
pages = {
    "Homepage": homepage,
    "About": about,
    "Contact": contact
}

# Add a navigation menu to the sidebar
selection = st.sidebar.radio("Go to", list(pages.keys()))

# Call the appropriate page based on the user's menu choice
pages[selection]()


