import streamlit as st
from streamlit_lottie import st_lottie
import requests
# Inject custom CSS to set a gradient background
page_bg = """
<style>
.stApp {
    background: linear-gradient(90deg, #bfd4bf, #ddd6e1);
    padding: 10px;
    transition: all 0.3s ease-in-out;
}
h1 {
    color:black;
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

# Initialize session state variable if it doesn't exist
if 'started' not in st.session_state:
    st.session_state.started = False

# Main content display logic for the initial page
if not st.session_state.started:
    # Main title with emoji
    st.markdown("<h1>Detection Dynamo</h1>", unsafe_allow_html=True)


# Function to load Lottie animation from a URL
def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# URL for Lottie animation (you can change the URL to any Lottie file of your choice)
lottie_url = "https://lottie.host/98c5c5c8-c81a-43f2-b237-9e8844be176c/1RR08K5GKU.json"
lottie_animation = load_lottie_url(lottie_url)

# Setting the layout for columns
left_column, right_column = st.columns(2)

with left_column:
    st.subheader("""
                 
                 Welcome to object detection website.
                 Simply upload an image and
                 let the model do the rest! 
                 Object detection is a technique that uses 
                 neural networks to localize and classify objects 
                 in images. This computer vision task has a wide range 
                 of applications, from medical imaging to self-driving cars.
                 Object detection is a computer vision task that aims to locate 
                 objects in digital images.""")

with right_column:
    if lottie_animation:
        st_lottie(lottie_animation, key="lottie_right", height=300)
    else:
        st.write("Lottie animation failed to load.")



