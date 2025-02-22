import streamlit as st
import cv2
from utils import *
import warnings 
warnings.filterwarnings('ignore')  


def main():
    st.title("Delta Arm Waste Classifier")
    
    # Sidebar panel for coordinates and actions
    st.sidebar.title("Control Panel")
    x_coord = st.sidebar.number_input("X Coordinate", value=0)
    y_coord = st.sidebar.number_input("Y Coordinate", value=0)
    z_coord = st.sidebar.number_input("Z Coordinate", value=-290)
    
    if st.sidebar.button("Send Coordinates"):
        send_coordinates([x_coord, y_coord, z_coord], "none")

    if st.sidebar.button("Return to Home Position"):
        send_coordinates([0, 0, -290,], "none")
    
    # Confidence level input
    confidence_level = st.slider("Confidence Level", min_value=0.0, max_value=1.0, value=0.5, step=0.01)
    # Live camera feed
    st.subheader("Live Feed")

    # use 1 to use iphone camera else 0 to use laptop camera
    capture = cv2.VideoCapture(1)

    frame_placeholder = st.empty()
    capture_button_pressed = st.button('Capture Image and Predict')

    while capture.isOpened():
        ret, frame = capture.read()
        
        if not ret:
            st.write("Video capture has ended.")
            break

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_with_polygon = draw_polygon(frame)
        frame_placeholder.image(frame_with_polygon, channels='RGB')

        if capture_button_pressed:
            capture_button_pressed, result = capture_image(frame, confidence_level)
            print(result)
            send_coordinates([0, 0, -380,] ,result)
            
    
    capture.release()



if __name__ == "__main__":
    main()