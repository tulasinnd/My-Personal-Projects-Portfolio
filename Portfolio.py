import streamlit as st
from PIL import Image, ImageDraw, ImageOps
import streamlit as st
import numpy as np
import pandas as pd
# Set page config
st.set_page_config(layout="wide")

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
    st.write( f'<h1 style="color:#228B22;">TECHNICAL SKILLS</h1>', unsafe_allow_html=True )    
    st.write("<div style='color:#3CB371; font-size:24px'>Python:</div>", unsafe_allow_html=True)
    st.write("<div style='color:#66d9ff'>- I have developed varuius web applications, and machine learning models using libraries such as pandas, NumPy, and scikit-learn in python</div>", unsafe_allow_html=True)
    st.write("<div style='color:#3CB371; font-size:24px'>Descriptive Statistics:</div>", unsafe_allow_html=True)
    st.write("<div style='color:#66d9ff'>- Knowledge of descriptive statistics and probability theory, with experience in analyzing and summarizing data using statistical measures such as mean, median, mode, and standard deviation.</div>", unsafe_allow_html=True)
    st.write("<div style='color:#3CB371; font-size:24px'>Data Visualization:</div>", unsafe_allow_html=True)
    st.write("<div style='color:#66d9ff'>- Skilled in data visualization using libraries such as Matplotlib and Seaborn, with experience creating visualizations that effectively communicate insights and trends in data.</div>", unsafe_allow_html=True)
    st.write("<div style='color:#3CB371; font-size:24px'>Database Management:</div>", unsafe_allow_html=True)
    st.write("<div style='color:#66d9ff'>- Experience working with both SQL and NoSQL databases, including MongoDB and MySQL, with knowledge of database design and optimization.</div>", unsafe_allow_html=True)
    st.write("<div style='color:#3CB371; font-size:24px'>Deployment:</div>", unsafe_allow_html=True)
    st.write("<div style='color:#66d9ff'>- Experience deploying applications to the cloud using services such as AWS RDS and Streamlit Cloud, with knowledge of serverless architecture and continuous integration/continuous deployment (CI/CD) pipelines.</div>", unsafe_allow_html=True)
    st.write("<div style='color:#3CB371; font-size:24px'>Machine Learning:</div>", unsafe_allow_html=True)
    st.write("<div style='color:#66d9ff'>- Strong understanding of machine learning concepts and algorithms, with experience building and evaluating models for classification, regression, and clustering tasks.</div>", unsafe_allow_html=True)
    st.write("<div style='color:#3CB371; font-size:24px'>Deep Learning:</div>", unsafe_allow_html=True)
    st.write("<div style='color:#66d9ff'>- Familiarity with deep learning techniques such as convolutional neural networks and recurrent neural networks, with experience applying these techniques to tasks such as image classification and natural language processing.</div>", unsafe_allow_html=True)
    st.write("<div style='color:#3CB371; font-size:24px'>Streamlit:</div>", unsafe_allow_html=True)
    st.write("<div style='color:#66d9ff'>- Knowledge of Streamlit for building interactive web applications, with experience developing applications that showcase data visualizations and machine learning models.</div>", unsafe_allow_html=True)
    st.write("<div style='color:#3CB371; font-size:24px'>Exploratory Data Analysis:</div>", unsafe_allow_html=True)
    st.write("<div style='color:#66d9ff'>- Skilled in exploratory data analysis, with experience using tools such as pandas and NumPy to clean and preprocess data, and to identify patterns and relationships in data.</div>", unsafe_allow_html=True)
    st.write("<div style='color:#3CB371; font-size:24px'>Feature Engineering:</div>", unsafe_allow_html=True)
  
  
def Projects():
    st.write( f'<h1 style="color:#228B22;">PROJECTS</h1>', unsafe_allow_html=True ) 

    with st.expander("1 POPULATION PREDICTION SYSTEM"):
        # Set font size
        font_size1 = "19px"
        font_size = "15px"

        # Set colors for paragraphs and unordered lists
        highlight_color = "#00e6e6"
        paragraph_color = "#00b3b3"

        # Set application link
        st.markdown(f"<p style='font-size: {font_size1}; color: {highlight_color}; font-weight: bold;'>Application Link:</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='font-size: {font_size}; color: {paragraph_color};'> <a href='https://tulasinnd-population-prediction-system-population-app-x6rrby.streamlit.app/' style='color: {paragraph_color};'>https://tulasinnd-population-prediction-system-population-app-x6rrby.streamlit.app/</a></p>", unsafe_allow_html=True)

        # Set source code link
        st.markdown(f"<p style='font-size: {font_size1}; color: {highlight_color}; font-weight: bold;'>Source Code Link:</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='font-size: {font_size}; color: {paragraph_color};'><a href='https://github.com/tulasinnd/Population-Prediction-System.git' style='color: {paragraph_color};'>https://github.com/tulasinnd/Population-Prediction-System.git</a></p>", unsafe_allow_html=True)

        # Set project overview
        st.markdown(f"<p style='font-size: {font_size1}; color: {highlight_color}; font-weight: bold;'>Project Overview:</p>", unsafe_allow_html=True)
        st.markdown(f"<ul style='font-size: {font_size}; color: {paragraph_color};'><li>This project uses polynomial regression to predict the population of a country for a given year.</li><li>The user can select a country and input a year for which they want to predict the population.</li><li>The system uses a dataset containing population information for various countries and years.</li></ul>", unsafe_allow_html=True)

        # Set skills required
        st.markdown(f"<p style='font-size: {font_size1}; color: {highlight_color}; font-weight: bold;'>Skills Required:</p>", unsafe_allow_html=True)
        st.markdown(f"<ul style='font-size: {font_size}; color: {paragraph_color};'><li>Knowledge of Python programming language</li><li>Familiarity with data cleaning, preprocessing, and analysis</li><li>Understanding of machine learning algorithms, particularly polynomial regression</li><li>Experience with data visualization libraries such as Plotly and Streamlit</li></ul>", unsafe_allow_html=True)

        # Set advantages
        st.markdown(f"<p style='font-size: {font_size1}; color: {highlight_color}; font-weight: bold;'>Advantages:</p>", unsafe_allow_html=True)
        st.markdown(f"<ul style='font-size: {font_size}; color: {paragraph_color};'><li>Provides accurate population predictions based on a country and year input</li><li>Offers a simple user interface through a Streamlit dashboard</li><li>Uses a machine learning algorithm to predict population, which can be more accurate than traditional statistical methods</li></ul>", unsafe_allow_html=True)

        # Set limitations
        st.markdown(f"<p style='font-size: {font_size1}; color: {highlight_color}; font-weight: bold;'>Limitations:</p>", unsafe_allow_html=True)
        st.markdown(f"<ul style='font-size: {font_size}; color: {paragraph_color};'><li>The accuracy of the predictions may vary depending on the quality of the input data</li><li>The model is based on historical population trends, which may not reflect future changes in population</li><li>The model may not account for external factors that could impact a country's population, such as natural disasters or political events</li></ul>", unsafe_allow_html=True)

      
    with st.expander("2 DATA EXTRACTION FROM BUSINESS CARDS USING OCR"):

        # Set heading style
        st.markdown("<h2 style=color: #26547C;'>Population Prediction System</h1>", unsafe_allow_html=True)
        
    with st.expander("3 PHONEPE PULSE DATA (2018-2022) VISUALIZATION & ANALYSIS"):

        # Set heading style
        st.markdown("<h2 style=color: #26547C;'>Population Prediction System</h1>", unsafe_allow_html=True)
        
    with st.expander("4 TWITTER SCRAPING USING SNSCRAPE"):

        # Set heading style
        st.markdown("<h2 style=color: #26547C;'>TWITTER SCRAPING USING SNSCRAPE</h1>", unsafe_allow_html=True)
    
    
def Certifications():
    st.title("Certifications")
        
      
# Define the pages dictionary
pages = {

    "Contact Information": Contact,
    "Education": Education,
    "Skills": Skills,
    "Projects": Projects,
    "Certifications": Certifications,

}

#********************************** ROUND IMAGE***************************************************************************************
img_url ="assets/My_DS_Image.JPG"
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
