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
# Function to mask the image as a circle
def circle_mask(image, size):
    """Returns a circular mask for the given image"""
    mask = Image.new('L', size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + size, fill=255)
    mask = ImageOps.invert(mask)
    image.putalpha(mask)
    return image

# Get the image file from the user
image_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

# Display the circular image if an image file was uploaded
if image_file is not None:
    image = Image.open(image_file)
    image = image.convert("RGBA")  # convert the image to RGBA format to add an alpha channel
    image = circle_mask(image, image.size)  # apply the circular mask to the image
    st.image(image)

#]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]

# Add a navigation menu to the sidebar
selection = st.sidebar.radio("Go to", list(pages.keys()))
# Call the appropriate page based on the user's menu choice
pages[selection]()


