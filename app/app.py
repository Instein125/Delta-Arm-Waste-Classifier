import streamlit as st
import cv2
from utils import *


def main():
    st.title("Delta Arm Waste Classifier")
    
    # Sidebar panel for coordinates and actions
    st.sidebar.title("Control Panel")
    x_coord = st.sidebar.number_input("X Coordinate", value=0)
    y_coord = st.sidebar.number_input("Y Coordinate", value=0)
    z_coord = st.sidebar.number_input("Z Coordinate", value=0)
    
    if st.sidebar.button("Send Coordinates"):
        print([x_coord, y_coord, z_coord])
        # send_coordinates([x_coord, y_coord, z_coord])

    if st.sidebar.button("Return to Home Position"):
        pass
        # return_to_home()
    
    # Live camera feed
    st.subheader("Live Feed")
    capture = cv2.VideoCapture(0)

    frame_placeholder = st.empty()
    capture_button_pressed = st.button('Capture Image and Predict')

    while capture.isOpened():
        ret, frame = capture.read()
        
        if not ret:
            st.write("Video capture has ended.")
            break

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_placeholder.image(frame, channels='RGB')

        if capture_button_pressed:
            capture_button_pressed = capture_image(frame)
    
    capture.release()
    cv2.destroyAllWindows()



if __name__ == "__main__":
    main()
