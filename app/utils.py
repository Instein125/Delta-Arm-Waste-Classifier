import streamlit as st
import cv2
import os

def make_prediction(img_path):
    """Make prediction on the given image and return prediction results"""
    pass

def send_coordinates(coordinates):
    """Take the list of cordinates in list form and send to serial port"""
    st.write("Sending coordinates:", coordinates)
    pass

def return_to_home():
    """Send the coordiantes of home position to serial port of arduino"""
    st.write("Returning to home position...")

def capture_image(frame):
    """Capture the image from live feed and make prediction"""
    img_name = "capture_image.jpg"
    path = 'app'
    img_path = os.path.join(path , img_name)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    cv2.imwrite(img_path, frame)
    st.image(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB), channels="RGB", caption="Captured Image", use_column_width=True)
    prediction = make_prediction(img_path)
    return False

def main():
    pass

if __name__ == "__main__":
    main()
