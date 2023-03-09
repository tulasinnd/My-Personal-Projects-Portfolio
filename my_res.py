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
                    font-weight: bold;
                    font-size: 24px;
   
                }
            </style>
        """

    st.write(pink_style, unsafe_allow_html=True)
    st.write("""
                        
            Full Name:              NAGULAPALLI NAGA DURGA TULASI
            
            Location:               India, Andhra Pradesh, East Godavari District
            
            Phone Number:           91332255545
            
            Email Address:          tulasinnd@gmail.com          
                 
            LinkedIn Profile:       https://www.linkedin.com/in/tulasi-n-49b6111b0/

            GitHub Profile:         https://github.com/tulasinnd
            
            Personal Portfolio:     https://tulasinnd-my-personal-projects-portfolio-my-res-bk3xaw.streamlit.app/
            
           """)
    
def Education():
    st.write(f"<h1 style='color:#ad33ff;font-weight:bold;'>EDUCATION DETAILS</h1>", unsafe_allow_html=True)
    import tabulate

    data = [    ['2020-2023', "Master's degree in Data Science", 'IITM with GUVI', 80],
        ['2014-2018', 'B.Tech (Information Technology)', 'Aditya Engineering College', 78],
        ['2012-2014', 'Intermediate', 'Aditya Junior College', 92],
        ['2011-2012', 'SSC', 'Mary Immaculate High School', 93],
    ]

    headers = ['PERIOD', 'COURSE', 'INSTITUTE', 'PERCENTAGE']

    table = tabulate.tabulate(data, headers=headers, tablefmt='html')

    st.markdown(table, unsafe_allow_html=True)    
        
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



