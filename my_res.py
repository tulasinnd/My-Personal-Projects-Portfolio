import streamlit as st
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
st.markdown(
    """
    <style>
        #image {
            border-radius: 50%;
            height: 150px;
            width: 150px;
            object-fit: cover;
            object-position: center;
        }
    </style>
    """,
    unsafe_allow_html=True
)

img_url = "data-scientist.jpeg"
st.sidebar.image(img_url, caption='Your image caption', use_column_width=True, output_format='JPEG')

#]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]
image = "data-scientist.jpeg"
st.sidebar.image(image, use_column_width=True, caption="Your Name")

st.sidebar.markdown(
    """
    <style>
    .sidebar .sidebar-content .stImage {
        max-width: 150px;
        border-radius: 50%;
        border: 2px solid #fff;
        box-shadow: 0px 0px 8px rgba(0, 0, 0, 0.3);
        margin-top: 20px;
        margin-bottom: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
#]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]

# Add a navigation menu to the sidebar
selection = st.sidebar.radio("Go to", list(pages.keys()))
# Call the appropriate page based on the user's menu choice
pages[selection]()


