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

#]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]

# Define function to make image round
def make_round(im, size, fill_color=(0, 0, 0, 0)):
    # Create a square image
    im_square = ImageOps.fit(im, (size, size), Image.ANTIALIAS)
    
    # Create a mask
    mask = Image.new('L', (size, size), 0)
    draw = ImageDraw.Draw(mask) 
    draw.ellipse((0, 0, size, size), fill=255)
    
    # Apply the mask
    im_round = ImageOps.fit(im, (size, size), Image.ANTIALIAS)
    im_round.putalpha(mask)
    
    # Combine the square image and the round image
    result = Image.new('RGBA', (size, size), fill_color)
    result.paste(im_square, (0, 0), im_square)
    result.paste(im_round, (0, 0), im_round)
    
    return result
# Load and display image
im = Image.open("my_photo.jpg")
st.sidebar.image(make_round(im, 128), use_column_width=True)


#]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]

# Add a navigation menu to the sidebar
selection = st.sidebar.radio("Go to", list(pages.keys()))
# Call the appropriate page based on the user's menu choice
pages[selection]()


