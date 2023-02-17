from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
# css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "pic.jpg"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "portfolio | Tulasi NND"
PAGE_ICON = ":wave:"
NAME = "Tulasi NND"
DESCRIPTION = """
I am a dedicated and aspiring individual with an objective of working in an organization that provides opportunities for technical and personal advancement

"""
EMAIL = "tulasinnd@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/tulasi-n-49b6111b0/",
    "GitHub": "https://github.com/tulasinnd",

}



st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
# with open(css_file) as f:
    #st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", "tulasinnd@gmail.com")
    for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
        st.write(f"[{platform}]({link})")





# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Education")
st.write(
    """
- ✔️ Present: Doing  Professional Master data science program at  IITM  with Guvi 
- ✔️ 2014-2018: B.Tech (Information Technology)

"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Technical Stack")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas), SQL
- 📊 Data Visulization: MS Excel, Plotly, Matplotlib, Seaborn 
- 📚 Modeling: Supervised ML Algorithms, Unsupervised ML Algorithms
- 🗄️ Databases: MongoDB, MySQL
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Projects")
st.write("---")

# --- JOB 1

st.write("🚧", "**Twitter Scraping**")
st.write(
    """
- Technologies used: 
Python, Streamlit, Snscrape\n
- Introduction:
Twitter Scraping web app basically searches tweets from twitter websites by taking any keyword or hashtag as input. It will populate all the tweets that are related to keyword/ hashtag dynamically.\n
- Basic Working:
Users have to give the following inputs to find tweets dynamically. keyword or Hashtag to be searched , starting date, ending date, Number of tweets needs to be scrapped. After scraping is done, User will be able to Download data as CSV/JSON or simply view Tweets\n
- Link for app:'https://tulasinnd-twitter-scraping-with-snscrape-twitter-scraper-sm39k5.streamlit.app/'
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**PhonePe Pulse Analysis**")
st.write(
    """
- Technologies used: 
Python, Streamlit, Plotly\n
- Introduction:
PhonePe pulse is a phonepe app data from 2018 to 2022 available in github repository(https://github.com/PhonePe/pulse ). I have created a dashboard to analyze and visualize Phonepe pulse data dynamically, this dashboard contains live maps, bar graphs, histograms, pie charts to analyze data in various aspects to extract facts\n
- Basic Components of dashboard:
Live Geo-Visualization,
Transactions Data Analysis,
User Data Analysis\n
- Link for app:'https://tulasinnd-phonepe-pulse-data-2018-2-phonepe-dashboard-df-sochbu.streamlit.app/'

"""
)




