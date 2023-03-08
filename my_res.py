import streamlit as st
from PIL import Image, ImageDraw, ImageOps
import streamlit as st
import numpy as np
# Set page config
st.set_page_config(layout="wide")

# Create a function to display the homepage
def Overview():
    st.write( f'<h1 style="color:#ff69b4;">MY PORTFOLIO</h1>', unsafe_allow_html=True )

# Create a function to display the about page
def Objective():
    st.title("Objective")

# Create a function to display the contact page
def Contact():
    st.title("Contact Info")
    
def Education():
    st.title("Education")
    
def Skills():
    st.title("Skills")
    
def Experience():
    st.title("Experience")
    
def Projects():
    st.title("Projects")
    
def Certifications():
    st.title("Certifications")
        
def Interests():
    st.title("Interests")
      
def Social():
    st.title("Social ")
    
def Hobbies():
    st.title("Hobbies")
    
def Others():
    st.title("Others")


# Define the pages dictionary
pages = {
    "Overview": Overview,
    "Objective": Objective,
    "Contact Information": Contact,
    "Education": Education,
    "Skills": Skills,
    "Experience": Experience,
    "Projects": Projects,
    "Certifications": Certifications,
    "Interests": Interests,
    "Social Media": Social,
    "Hobbies": Hobbies,
    "Others": Others,
}

# Add image to the sidebar
st.markdown("""
    <style>
        .sidebar .sidebar-content .stImage img {
            border-radius: 50% !important;
        }
    </style>
""", unsafe_allow_html=True)

img_url = "data-scientist.jpeg"
st.sidebar.image(img_url, caption='Your image caption', use_column_width=True, output_format='JPEG')

#nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
# import streamlit as st

# # Display image
# image =  "assets/pic.jpg"
# st.image(image, width=200, use_column_width=False, output_format='PNG')

# # Apply CSS styling and image masking
# st.markdown(
#     """
#     <style>
#     .profile-pic {
#         width: 200px;
#         height: 200px;
#         background-position: center;
#         background-size: cover;
#         border-radius: 50%;
#         overflow: hidden;
#         box-shadow: 0px 0px 5px 2px rgba(0, 0, 0, 0.2);
#     }
#     .profile-pic img {
#         display: none;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# # Wrap image in a div to apply CSS styling and image masking
# st.markdown(
#     f'<div class="profile-pic" style="background-image: url({image})"><img src="{image}"></div>',
#     unsafe_allow_html=True
# )
import streamlit as st

# Display image
image =  "assets/pic.jpg"
st.image(image, width=200, use_column_width=False, output_format='PNG')

# Apply CSS styling to create circular border
st.markdown(
    """
    <style>
    img {
        border-radius: 50%;
        border: 5px solid white;
        box-shadow: 0px 0px 5px 2px rgba(0, 0, 0, 0.2);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Wrap image in a div to apply CSS styling
st.markdown(
    f'<div style="border-radius: 50%; overflow: hidden; box-shadow: 0px 0px 5px 2px rgba(0, 0, 0, 0.2); width: 200px; height: 200px;"><img src="{image}" style="object-fit: cover; width: 100%; height: 100%;"></div>',
    unsafe_allow_html=True
)


#jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj
# Add a navigation menu to the sidebar
selection = st.sidebar.radio("Go to", list(pages.keys()))
# Call the appropriate page based on the user's menu choice
pages[selection]()


