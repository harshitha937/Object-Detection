import streamlit as st
about_page = st.Page(
    page="main.py",
    title="Homepage",
    icon="🏡",
    default=True,
)
project_2_page = st.Page(
    page="pages/2_Upload.py",
    title="Upload",
    icon="🎫" ,
)
project_3_page = st.Page(
    page="pages/3_Contact.py",
    title="Contact Us", 
    icon="📞",
)

pg = st.navigation(
    {
        "HomePage":[about_page],
        "Upload":[project_2_page],
        "Contact":[project_3_page],
    }
)



#starts navigation 
pg.run()