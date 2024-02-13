import cv2
import numpy as np

def detect_colors(image):
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

        # Iterate over contours to draw bounding boxes
        for contour in contours:
            # Get bounding box coordinates
            x, y, w, h = cv2.boundingRect(contour)

            # Draw bounding box around the object
            cv2.rectangle(image, (x, y), (x + w, y + h), color_values['color'], 2)

            # Append detected color to list
            detected_color_list.append(color_name)

    return image, detected_color_list


if __name__ == "__main__":
    # Read the image
    image = cv2.imread('app/color_ball.jpg')

    # Detect colors and draw bounding boxes
    detected_image, detected_colors = detect_colors(image)

    # Print list of detected colors
    print("Detected colors:", detected_colors)
    # Display the original and detected colors
    cv2.imshow('Original Image', image)
    cv2.imshow('Detected Colors', detected_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

