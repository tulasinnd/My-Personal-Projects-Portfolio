# import streamlit as st
# st.set_page_config(layout="wide")

# # Create a function to display the homepage
# def homepage():
#     st.title("Welcome to my portfolio")
#     st.write(
#     f'<h1 style="color:#ff69b4;">MY PORTFOLIO</h1>',
#     unsafe_allow_html=True
# )

# # Create a function to display the about page
# def about():
#     st.title("About Me")

# # Create a function to display the contact page
# def contact():
#     st.title("Contact Me")

# # Define the pages dictionary
# pages = {
#     "Homepage": homepage,
#     "About": about,
#     "Contact": contact
# }

# # Add a navigation menu to the sidebar
# selection = st.sidebar.radio("Go to", list(pages.keys()))

# # Call the appropriate page based on the user's menu choice
# pages[selection]()


import streamlit as st

# Create a container for the navigation menu
nav_container = st.beta_container()

# Add items to the navigation menu
nav_container.write("Home")
nav_container.write("About")
nav_container.write("Contact")

# Create a separate container for the Streamlit content
content_container = st.beta_container()

# Add Streamlit content below the navigation menu
content_container.write("Welcome to my Streamlit app!")
content_container.write("This is the content area.")
