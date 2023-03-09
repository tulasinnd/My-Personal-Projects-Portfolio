import streamlit as st
from PIL import Image, ImageDraw, ImageOps
import streamlit as st
import numpy as np
# Set page config
st.set_page_config(layout="wide")

# Create a function to display the homepage
def Overview():
    st.write( f'<h1 style="color:#ff69b4;">MY PORTFOLIO</h1>', unsafe_allow_html=True )

# Create a function to display the contact page
def Contact():
    st.write( f'<h1 style="color:#ff69b4;">CONTACT INFORMATION</h1>', unsafe_allow_html=True )
    pink_style = """
            <style>
                p {
                    color: pink;
                }
            </style>
        """

        st.write(pink_style, unsafe_allow_html=True)
        st.write("""
            Here are some additional contact information you can consider including in your resume:

            6. Personal Website or Portfolio: If you have a personal website or portfolio showcasing your work, include the URL in your contact information.
            7. Social Media Handles: If you have professional social media accounts, such as Twitter or Instagram, you can include them in your contact information section. However, make sure that your profiles are appropriate for potential employers to view.
            8. Skype or Zoom: If you're open to conducting initial interviews via video conferencing, you can include your Skype or Zoom username.
            9. Availability: If you're currently employed or have other commitments, you can include your availability for interviews in your contact information section.
            10. Professional Headline: You can include a professional headline or tagline underneath your name to quickly summarize your experience or career objective.
        """)
    
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
      
# Define the pages dictionary
pages = {
    "Overview": Overview,
    "Contact Information": Contact,
    "Education": Education,
    "Skills": Skills,
    "Experience": Experience,
    "Projects": Projects,
    "Certifications": Certifications,
    "Interests": Interests,
}

#********************************** ROUND IMAGE***************************************************************************************
img_url ="assets/pic.jpg"
st.sidebar.image(img_url, caption='Your image caption', use_column_width=True, output_format='JPEG')
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

#*********************************************************************************************************************
# Add a navigation menu to the sidebar
selection = st.sidebar.radio("Go to", list(pages.keys()))
# Call the appropriate page based on the user's menu choice
pages[selection]()



