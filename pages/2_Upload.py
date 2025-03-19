import streamlit as st
import cv2
#Read in the image file
import numpy as np
from PIL import Image
# Inject custom CSS to set a gradient background
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


    # Main title with emoji
st.markdown("<h1>Upload</h1>", unsafe_allow_html=True)
#Import relevant modules




# File uploader widget to accept an image file
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

# Check if an image file is uploaded
if uploaded_file is not None:
    # Read the image u`sing PIL, convert to OpenCV format
    image = Image.open(uploaded_file)
    
    # Convert the PIL image to an OpenCV-compatible format (numpy array)
    image = np.array(image)
    image = cv2.resize(image, (0, 0), fx=2.0, fy=2.0)


    #Import the class names
    classNames = []
    classFile = 'ob3/testing/config_files/coco.names'
    #### Extracts the classes into a list
    #rt = open file for read
    # rstrip('\n') removing white space
    # split seperates each word at each line into a string
    with open(classFile, 'rt') as f:
        classNames = f.read().rstrip('\n').split('\n') 

    #Import the config and weights file
    configPath = 'ob3/testing/config_files/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
    weightsPath = 'ob3/testing/config_files/frozen_inference_graph.pb'

    #Set relevant parameters and initiate model
    net = cv2.dnn_DetectionModel(weightsPath,configPath)
    net.setInputSize(320,320)
    net.setInputScale(1.0/127.5)
    net.setInputMean((127.5,127.5,127.5))
    net.setInputSwapRB(True)

    #Extract, ClassIds, confidence and bounding box info
    classIds, confs, bbox = net.detect(image, confThreshold = 0.5) #if 50% confident, predict
    print(classIds, confs,bbox)

    #For loop for three different list led to the use of list
    #The output from clasids.flatten, confs.flatten and bbox is [1] [0.6724][[60 40 373 461]]
    #If you had multiple objects, the first object and list of box coordinates are all in line.
    #The object, confidence and co-ordinates can know all be used in the opencv packages

    for classId, confidence, box in zip(classIds.flatten(),confs.flatten(),bbox):
        cv2.rectangle(image,box,color=(255,255,0), thickness=2)
        # cv2.putText(image,classNames[classId-1],(box[0]+10,box[1]+30), 
        #             cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
        cv2.putText(image, classNames[classId - 1], (box[0] + 10, box[1] + 30),
                    cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2)  # Adjusted font scale and thickness

    #Open
    cv2.waitKey(0)


    # Display the uploaded image using Streamlit
    st.image(image, caption="Uploaded Image", use_column_width=True)
    st.success("Image processed successfully!")
else:
    st.info("Please upload an image to see it displayed and processed here.")

