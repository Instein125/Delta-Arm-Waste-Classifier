import streamlit as st
import cv2
import os
import numpy as np

# def draw_polygon(frame):
#     # Get frame dimensions
#     height, width, _ = frame.shape
    
#     # Define vertices of the polygon
#     vertices = np.array([[(width // 4, height // 4), 
#                           (3 * width // 4, height // 4), 
#                           (3 * width // 4, 3 * height // 4), 
#                           (width // 4, 3 * height // 4)]], dtype=np.int32)
    
#     # Create a mask of zeros with the same dimensions as the frame
#     mask = np.zeros_like(frame)
    
#     # Fill the polygon defined by vertices with white color
#     cv2.fillPoly(mask, vertices, (255, 255, 255))
    
#     # Bitwise AND operation between the mask and the frame
#     masked_frame = cv2.bitwise_and(frame, mask)
    
#     # Draw the polygon on the frame
#     cv2.polylines(frame, [vertices], isClosed=True, color=(0, 255, 0), thickness=2)
    
#     return frame

def draw_polygon(frame):
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
