import streamlit as st
import cv2
import os
import numpy as np 
import shutil
from ultralytics import YOLO

MODEL = YOLO("New model/waste model/train6/weights/best.pt")




def draw_polygon(frame):

    """Draw a polygon zone on the live video frame"""
    # Get frame dimensions
    height, width, _ = frame.shape
    
    # Define vertices of the polygon
    vertices = np.array([[(width // 4, height // 4), 
                          (3 * width // 4, height // 4), 
                          (3 * width // 4, 3 * height // 4), 
                          (width // 4, 3 * height // 4)]], dtype=np.int32)
    
    # Draw the polygon on the frame
    frame_with_polygon = cv2.polylines(frame.copy(), [vertices], isClosed=True, color=(0, 255, 0), thickness=2)
    
    return frame_with_polygon

def make_prediction(img_path, confidence):
    """Make prediction on the given image and return prediction results"""
    

    if os.path.isdir("app/predict"):
        shutil.rmtree("app/predict")


    results = MODEL.predict(source=img_path, save = True, conf = confidence,save_txt = True, project = 'app/' )
    return results

def send_coordinates(coordinates):
    """Take the list of cordinates in list form and send to serial port"""
    st.write("Sending coordinates:", coordinates)
    pass

def return_to_home():
    """Send the coordiantes of home position to serial port of arduino"""
    st.write("Returning to home position...")

def capture_image(frame, confidence_level):
    """Capture the image from live feed and make prediction"""
    img_name = "capture_image.jpg"
    path = 'app'
    img_path = os.path.join(path , img_name)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    cv2.imwrite(img_path, frame)
    
    prediction = make_prediction(img_path, confidence_level)

    # show the predicted image with bounding box
    st.image("app/predict/capture_image.jpg", channels="RGB", caption="Captured Image", use_column_width=True)
    return False

def main():
    pass

if __name__ == "__main__":
    main()
