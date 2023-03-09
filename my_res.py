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
  
def Experience():
    st.title("Experience")
    
def Projects():
    st.write( f'<h1 style="color:#228B22;">PROJECTS</h1>', unsafe_allow_html=True )    
    with st.expander("POPULATION PREDICTION SYSTEM"):
        st.write(\"\"\"
            The chart above shows some numbers I picked for you.
            I rolled actual dice for these, so they're *guaranteed* to
            be random.
        \"\"\")
    
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



