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
st.sidebar.image("data-scientist.jpeg", width=200)

# Apply rounded shape to the image
st.markdown("""
    <style>
        .sidebar .sidebar-content .stImage img {
            border-radius: 50%;
        }
    </style>
""", unsafe_allow_html=True)

#]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]
# Add image to sidebar
st.sidebar.markdown("""
<div class="sidebar-image-container">
    <img src="https://drive.google.com/file/d/1M0IQHQ00zSb8MQtUJBaUs6y4jRiz7Eym/view?usp=share_link" alt="profile image" class="sidebar-image">
</div>
""", unsafe_allow_html=True)

# Add styles to sidebar image
st.markdown("""
<style>
    .sidebar-image-container {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-top: 20px;
    }
    .sidebar-image {
        border-radius: 50%;
        width: 80%;
        height: auto;
        margin-bottom: 10px;
    }
</style>
""", unsafe_allow_html=True)
#]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]

# Add a navigation menu to the sidebar
selection = st.sidebar.radio("Go to", list(pages.keys()))
# Call the appropriate page based on the user's menu choice
pages[selection]()


