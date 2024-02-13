import streamlit as st
import cv2
import os
import numpy as np 
import shutil
from ultralytics import YOLO
import json
import serial

MODEL = YOLO("New model/waste model/train6/weights/best.pt")


def draw_polygon(frame):

    """Draw a polygon zone on the live video frame"""
    # Get frame dimensions
    height, width, _ = frame.shape
    
    # Define vertices of the polygon
    vertices = np.array([[(width // 3, height // 3), 
                          (2 * width // 3, height // 3), 
                          (2 * width // 3, 2 * height // 3), 
                          (width // 3, 2 * height // 3)]], dtype=np.int32)
    
    # Draw the polygon on the frame
    frame_with_polygon = cv2.polylines(frame.copy(), [vertices], isClosed=True, color=(0, 255, 0), thickness=2)
    
    return frame_with_polygon

def make_prediction(img_path, confidence):
    """Make prediction on the given image and return prediction results"""
    

    if os.path.isdir("app/predict"):
        shutil.rmtree("app/predict")


    results = MODEL.predict(source=img_path, save = True, conf = confidence,save_txt = True, project = 'app/' )
    return results

def send_coordinates(coordinates, color):
    """Take the list of cordinates in list form and send to serial port"""
    st.write("Sending coordinates:", coordinates)
    data = {
        'coordinates': {
            'x': coordinates[0],
            'y': coordinates[1],
            'z': coordinates[2]
        },
        'color': color
    }

    # Convert data to JSON format
    json_data = json.dumps(data)

    # Write JSON data to a file
    with open('app/coordinates.json', 'w') as json_file:
        json_file.write(json_data)

    print(json_data)

    # Send JSON data to Arduino via serial port
    # send_to_arduino(json_data)
    

def send_to_arduino(json_data):
    """Send JSON data to Arduino via serial port"""
    try:
        # Define serial port settings
        ser = serial.Serial('COM3', 9600)  # Change 'COM3' to the appropriate port
        ser.write(json_data.encode())  # Send the encoded JSON data to Arduino
        ser.close()  # Close the serial port
        st.write("Coordinates sent to Arduino successfully.")
    except Exception as e:
        st.write(f"Error: {str(e)}")



def capture_image(frame, confidence_level):
    """Capture the image from live feed and make prediction"""
    img_name = "capture_image.jpg"
    path = 'app'
    img_path = os.path.join(path , img_name)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    cv2.imwrite(img_path, frame)
    # results = make_prediction(img_path, confidence_level)
    # show the predicted image with bounding box
    # st.image("app/predict/capture_image.jpg", channels="RGB", caption="Captured Image", use_column_width=True)

    # Detect colors and draw bounding boxes
    detected_image, detected_colors = detect_colors(img_path)
    # Print list of detected colors
    print("Detected colors:", detected_colors)
    cv2.imwrite('app/detected_image.jpg', detected_image)
    st.image("app/detected_image.jpg", channels="RGB", caption="Captured Image", use_column_width=True)
    return False, detected_colors


def detect_colors(image_path):

    # Read the image
    image = cv2.imread(image_path)
    # Convert BGR to HSV
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    # Define range of colors in HSV
    colors = {
        'red': {'lower': np.array([0, 100, 100]), 'upper': np.array([10, 255, 255]), 'color': (0, 0, 255)},
        'yellow': {'lower': np.array([20, 100, 100]), 'upper': np.array([30, 255, 255]), 'color': (0, 255, 255)},
        'green': {'lower': np.array([60, 100, 100]), 'upper': np.array([90, 255, 255]), 'color': (0, 255, 0)},
        'blue': {'lower': np.array([100, 100, 100]), 'upper': np.array([140, 255, 255]), 'color': (255, 0, 0)}
    }

    # List to store detected colors
    detected_color_list = []

    # Iterate over each color
    for color_name, color_values in colors.items():
        # Threshold the HSV image to get only desired colors
        mask = cv2.inRange(hsv, color_values['lower'], color_values['upper'])

        # Find contours in the mask
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Initialize variables to store largest contour area and its index
        max_area = 0
        max_area_contour = None

        # Iterate over contours to find the largest area
        for contour in contours:
            # Calculate contour area
            area = cv2.contourArea(contour)

            # Update max area and contour if the current contour has larger area
            if area > max_area:
                max_area = area
                max_area_contour = contour

        # Draw bounding box around the largest contour if found
        if max_area_contour is not None:
            # Get bounding box coordinates
            x, y, w, h = cv2.boundingRect(max_area_contour)

            # Draw bounding box around the object
            cv2.rectangle(image, (x, y), (x + w, y + h), color_values['color'], 2)

            # Append detected color to list
            detected_color_list.append(color_name)

    return image, detected_color_list

def main():
    pass

if __name__ == "__main__":
    main()
