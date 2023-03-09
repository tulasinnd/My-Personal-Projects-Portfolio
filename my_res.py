import streamlit as st
from PIL import Image, ImageDraw, ImageOps
import streamlit as st
import numpy as np
import pandas as pd
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
    st.write(f"<h1 style='color:#cc33ff;font-weight:bold;'>EDUCATION DETAILS</h1>", unsafe_allow_html=True)
    data = {
        'PERIOD': ['2022-2023', '2014-2018', '2012-2014', '2011-2012'],
        'COURSE': ["Master's degree in Data Science", 'B.Tech (Information Technology)', 'Intermediate', 'SSC'],
        'INSTITUTE': ['IITM with GUVI', 'Aditya Engineering College', 'Aditya Junior College', 'Mary Immaculate High School'],
        'PERCENTAGE': [80, 78, 92, 93],
    }

    df = pd.DataFrame(data)
    table = df.to_html(index=False, justify='center')
    # add some CSS rules to the HTML code
    table = table.replace('<table', '<table style="font-size: 24px; color: #ff33cc;"')
    st.markdown(table, unsafe_allow_html=True)


    
def Skills():
    st.write( f'<h1 style="color:#ff69b4;">TECHNICAL SKILLS</h1>', unsafe_allow_html=True )
    # Define a CSS style for the text
    green_style = """
        <style>
            .green {
                color: green;
                font-size: 24px;
            }
        </style>
    """

    # Print the text using the CSS style
    st.write(f"<div class='green'>{green_style}Professional Skills</div>")
    st.write(f"<div class='green'>{green_style}{'-' * 20}</div>")

    st.write(f"<div class='green'>{green_style}Python:</div>")
    st.write(f"<div class='green'>{green_style}  - Proficient in Python programming, with experience developing data pipelines, web applications, and machine learning models using libraries such as pandas, NumPy, and scikit-learn.</div>")

    st.write(f"<div class='green'>{green_style}Descriptive Statistics:</div>")
    st.write(f"<div class='green'>{green_style}  - Knowledge of descriptive statistics and probability theory, with experience in analyzing and summarizing data using statistical measures such as mean, median, mode, and standard deviation.</div>")

    st.write(f"<div class='green'>{green_style}Data Visualization:</div>")
    st.write(f"<div class='green'>{green_style}  - Skilled in data visualization using libraries such as Matplotlib and Seaborn, with experience creating visualizations that effectively communicate insights and trends in data.</div>")

    st.write(f"<div class='green'>{green_style}Database Management:</div>")
    st.write(f"<div class='green'>{green_style}  - Experience working with both SQL and NoSQL databases, including MongoDB and MySQL, with knowledge of database design and optimization.</div>")

    st.write(f"<div class='green'>{green_style}Deployment:</div>")
    st.write(f"<div class='green'>{green_style}  - Experience deploying applications to the cloud using services such as AWS RDS and Streamlit Cloud, with knowledge of serverless architecture and continuous integration/continuous deployment (CI/CD) pipelines.</div>")

    st.write(f"<div class='green'>{green_style}Machine Learning:</div>")
    st.write(f"<div class='green'>{green_style}  - Strong understanding of machine learning concepts and algorithms, with experience building and evaluating models for classification, regression, and clustering tasks.</div>")

    st.write(f"<div class='green'>{green_style}Deep Learning:</div>")
    st.write(f"<div class='green'>{green_style}  - Familiarity with deep learning techniques such as convolutional neural networks and recurrent neural networks, with experience applying these techniques to tasks such as image classification and natural language processing.</div>")

    st.write(f"<div class='green'>{green_style}Streamlit:</div>")
    st.write(f"<div class='green'>{green_style}  - Knowledge of Streamlit for building interactive web applications, with experience developing applications that showcase data visualizations and machine learning models.</div>")

    st.write(f"<div class='green'>{green_style}Exploratory Data Analysis:</div>")
    st.write(f"<div class='green'>{green_style}  - Skilled in exploratory data analysis, with experience using tools such as pandas and NumPy to clean and preprocess data, and to identify patterns and relationships in data.</div>")

    st.write(f"<div class='green'>{green_style}Feature Engineering:</div>")
    st.write(f"<div class='green'>{green_style}  - Knowledge of feature engineering techniques, with experience selecting and transforming features to improve the performance of machine learning models.</div>")

    
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



