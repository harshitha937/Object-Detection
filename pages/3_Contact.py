import streamlit as st

# Page title and introduction
st.title("Contact Us")
st.write("We'd love to hear from you! Please fill out the form below, and we'll get back to you as soon as possible.")

page_bg = """
<style>
.stApp {
    background: linear-gradient(90deg, #bfd4bf, #ddd6e1);
    padding: 10px;
    transition: all 0.3s ease-in-out;
}
h1 {
    color: black;
    font-size: 3.5em;
    text-align: center;
    font-weight: bold;
    margin-bottom: 20px;
    font-family:  "Lucida Handwriting", cursive;
    animation: fadeIn 2s ease-in-out;
}
h2, h3, p {
    color: #333;
    text-align: center;
    font-family: 'Verdana', sans-serif;
    animation: slideIn 1.5s ease-in-out;
}

/* Center the button and add hover effect */
div.stButton > button {
    background-color: #00aaff;
    color: white;
    font-size: 1.3em;
    font-weight: bold;
    padding: 12px 25px;
    border-radius: 12px;
    border: 2px solid #0077cc;
    margin: 0 auto;
    display: block;
    box-shadow: 3px 3px 8px rgba(0, 0, 0, 0.2);
    transition: background-color 0.3s ease-in-out, box-shadow 0.3s ease-in-out;
}

/* Button hover effect */
div.stButton > button:hover {
    background-color: #0077cc;
    color: #fff;
    box-shadow: 5px 5px 12px rgba(0, 0, 0, 0.3);
    cursor: pointer;
}


/* Animations */
@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}

@keyframes slideIn {
    from { transform: translateY(30px); opacity: 0; }
    to { transform: translateY(0); opacity: 1; }
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)


# Form inputs
with st.form("contact_form"):
    name = st.text_input("Name", placeholder="Your full name")
    email = st.text_input("Email", placeholder="Your email address")
    message = st.text_area("Message", placeholder="Your message here")
    
    # Submit button
    submitted = st.form_submit_button("Submit")
    
    # When the form is submitted, display a success message
    if submitted:
        if name and email and message:
            st.success("Thank you for your message! We'll get back to you soon.")
        else:
            st.error("Please fill out all fields before submitting.")

# Optional contact info or footer
st.write("---")
st.write("📧 Email us at [valluruharshitha2005@gmail.com](mailto:valluruharshitha2005@gmail.com)")
st.write("📞 Call us at +91 7075056370")