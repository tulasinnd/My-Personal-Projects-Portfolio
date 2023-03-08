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
import base64

# Function to mask the image as a circle
def circle_mask(image, size):
    """Returns a circular mask for the given image"""
    mask = Image.new('L', size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + size, fill=255)
    mask = ImageOps.invert(mask)
    image.putalpha(mask)
    return image

# Define the border and background color
border_color = "#FFFFFF"
background_color = "#F4F4F4"

# Get the image file from the user
image_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

# Display the circular image with a border and a background color if an image file was uploaded
if image_file is not None:
    image = Image.open(image_file)
    image = image.convert("RGBA")  # convert the image to RGBA format to add an alpha channel
    image = circle_mask(image, image.size)  # apply the circular mask to the image

    # Convert the image to base64 and display it in a circular form with a border and a background color
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    image_str = base64.b64encode(buffered.getvalue()).decode()
    st.markdown(
        f'<div style="border-radius: 50%; background-color: {background_color}; padding: 5px; border: 5px solid {border_color}; width: 200px; height: 200px; display: flex; justify-content: center; align-items: center;"><img src="data:image/png;base64,{image_str}" style="width: 90%; height: 90%; object-fit: contain;"></div>',
        unsafe_allow_html=True
    )

#]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]

# Add a navigation menu to the sidebar
selection = st.sidebar.radio("Go to", list(pages.keys()))
# Call the appropriate page based on the user's menu choice
pages[selection]()


