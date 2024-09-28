# # import cv2
# # import requests
# # import time

# # # Your Roboflow API key and model details
# # API_KEY = "mDNDGcJvWw9SUfrZYyGu"  # Replace with your API key
# # MODEL_ENDPOINT = "https://detect.roboflow.com/human-detection-e45xq"  # Replace with your model endpoint
# # VERSION = 1

# # # Set the IP address of the ESP32-CAM
# # ESP32_CAM_URL = "http://192.168.186.199"  # Replace with your ESP32-CAM IP address

# # # Start the video capture using the IP stream from ESP32-CAM
# # cap = cv2.VideoCapture(ESP32_CAM_URL)

# # # Function to detect objects from a frame
# # def detect(frame):
# #     # Convert the frame to JPEG for the API request
# #     _, img_encoded = cv2.imencode('.jpg', frame)

# #     # Prepare the image payload for the Roboflow API
# #     files = {
# #         "file": ("image.jpg", img_encoded.tobytes(), "image/jpeg")
# #     }
# #     params = {
# #         "api_key": API_KEY
# #     }

# #     # Make the API request
# #     for attempt in range(3):  # Retry up to 3 times
# #         response = requests.post(
# #             f"{MODEL_ENDPOINT}/{VERSION}",
# #             params=params,
# #             files=files
# #         )

# #         if response.status_code == 200:
# #             predictions = response.json()
# #             return predictions['predictions']
# #         else:
# #             print(f"Error on attempt {attempt + 1}: {response.status_code} - {response.text}")
# #             time.sleep(1)  # Wait before retrying

# #     return None

# # # Function to draw bounding boxes on the detected objects
# # def draw_boxes(frame, predictions):
# #     for obj in predictions:
# #         # Get the bounding box coordinates
# #         x, y, width, height = obj['x'], obj['y'], obj['width'], obj['height']
# #         label = obj['class']

# #         # Draw the rectangle
# #         start_point = (int(x - width / 2), int(y - height / 2))
# #         end_point = (int(x + width / 2), int(y + height / 2))
# #         color = (0, 255, 0)  # Green color for the box
# #         thickness = 2

# #         # Draw the bounding box
# #         cv2.rectangle(frame, start_point, end_point, color, thickness)

# #         # Add label
# #         cv2.putText(frame, f'{label}', (start_point[0], start_point[1] - 10),
# #                     cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)

# # # Main loop to capture webcam feed and perform detection
# # while True:
# #     ret, frame = cap.read()

# #     if not ret:
# #         print("Failed to capture frame.")
# #         break

# #     # Optionally resize the frame for faster processing
# #     resized_frame = cv2.resize(frame, (640, 480))

# #     # Detect objects in the frame
# #     start_time = time.time()
# #     predictions = detect(resized_frame)
# #     end_time = time.time()

# #     # Print inference time for debugging
# #     print(f"Inference Time: {end_time - start_time:.2f} seconds")

# #     # If predictions were made, draw boxes
# #     if predictions:
# #         draw_boxes(resized_frame, predictions)

# #     # Display the frame
# #     cv2.imshow('ESP32-CAM - Real-time Detection', resized_frame)

# #     # Break the loop if the user presses 'q'
# #     if cv2.waitKey(1) & 0xFF == ord('q'):
# #         break

# # # Release the capture and close OpenCV windows
# # cap.release()
# # cv2.destroyAllWindows()

# import cv2
# import requests
# import numpy as np

# # Roboflow API key and model details
# API_KEY = "mDNDGcJvWw9SUfrZYyGu"
# MODEL_ENDPOINT = "https://detect.roboflow.com/human-detection-e45xq"
# VERSION = 1

# # ESP32-CAM stream URL (ensure your ESP32 is streaming on this IP)
# # Replace <ESP32_IP> with your actual ESP32 IP address
# esp32_stream_url = "http://<ESP32_IP>/stream"

# # Open the video stream from ESP32 camera
# cap = cv2.VideoCapture(esp32_stream_url)

# # Check if the ESP32 stream is opened correctly
# if not cap.isOpened():
#     print("Error: Could not open video stream from ESP32.")
#     exit()

# # Function to send a frame to the Roboflow API for detection
# def detect(frame):
#     _, img_encoded = cv2.imencode('.jpg', frame)
#     files = {"file": ("image.jpg", img_encoded.tobytes(), "image/jpeg")}
#     params = {"api_key": API_KEY}

#     # Send the request to Roboflow model
#     response = requests.post(f"{MODEL_ENDPOINT}/{VERSION}", params=params, files=files)

#     if response.status_code == 200:
#         return response.json()['predictions']
#     else:
#         print("Error: Roboflow API request failed.")
#         return []

# # Loop to continuously capture frames from the ESP32 stream
# while True:
#     ret, frame = cap.read()

#     if not ret:
#         print("Failed to capture frame from ESP32.")
#         break

#     # Convert frame to grayscale for thermal effect and Roboflow input
#     gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     # Apply a colormap for better visualization (thermal-like effect)
#     thermal_colored = cv2.applyColorMap(gray_frame, cv2.COLORMAP_JET)

#     # Detect humans using the Roboflow model
#     predictions = detect(frame)

#     # Draw bounding boxes around detected humans from Roboflow predictions
#     for pred in predictions:
#         x, y, width, height = pred['x'], pred['y'], pred['width'], pred['height']
#         label = pred['class']

#         # Calculate bounding box corners
#         start_point = (int(x - width / 2), int(y - height / 2))
#         end_point = (int(x + width / 2), int(y + height / 2))

#         # Draw rectangle and label on the original frame
#         cv2.rectangle(frame, start_point, end_point, (0, 255, 0), 2)
#         cv2.putText(frame, label, (start_point[0], start_point[1] - 10),
#                     cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

#     # Display the frame with bounding boxes (Roboflow detection)
#     cv2.imshow("Human Detection - Roboflow Model", frame)

#     # Display the raw grayscale image
#     cv2.imshow("Thermal Camera - Grayscale", gray_frame)

#     # Display the color-mapped frame (thermal effect)
#     cv2.imshow("Thermal Camera - Colormap", thermal_colored)

#     # Break the loop if 'q' is pressed
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Release the video capture and close all OpenCV windows
# cap.release()
# cv2.destroyAllWindows()

import cv2
import requests
import base64

# Roboflow API key and model details
API_KEY = "mDNDGcJvWw9SUfrZYyGu"
MODEL_ENDPOINT = "https://detect.roboflow.com/human-detection-e45xq"
VERSION = 1

# Open the video stream from the webcam (thermal camera)
cap = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not cap.isOpened():
    print("Error: Could not open video stream from thermal camera.")
    exit()

# Function to send a frame to the Roboflow API for detection
def detect(frame):
    _, img_encoded = cv2.imencode('.jpg', frame)
    files = {"file": ("image.jpg", img_encoded.tobytes(), "image/jpeg")}
    params = {"api_key": API_KEY}

    # Send the request to Roboflow model
    response = requests.post(f"{MODEL_ENDPOINT}/{VERSION}", params=params, files=files)

    if response.status_code == 200:
        return response.json()['predictions']
    else:
        print("Error: Roboflow API request failed.")
        return []

# Loop to continuously capture frames from the webcam
while True:
    ret, frame = cap.read()

    if not ret:
        print("Failed to capture frame from webcam.")
        break

    # Convert frame to grayscale for thermal effect and Roboflow input
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply a colormap for better visualization (thermal-like effect)
    thermal_colored = cv2.applyColorMap(gray_frame, cv2.COLORMAP_JET)

    # Detect humans using the Roboflow model
    predictions = detect(frame)

    # Draw bounding boxes around detected humans from Roboflow predictions
    for pred in predictions:
        x, y, width, height = pred['x'], pred['y'], pred['width'], pred['height']
        label = pred['class']
        
        # Calculate bounding box corners
        start_point = (int(x - width / 2), int(y - height / 2))
        end_point = (int(x + width / 2), int(y + height / 2))

        # Draw rectangle and label on the original frame
        cv2.rectangle(frame, start_point, end_point, (0, 255, 0), 2)
        cv2.putText(frame, label, (start_point[0], start_point[1] - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Display the frame with bounding boxes (Roboflow detection)
    cv2.imshow("Human Detection - Roboflow Model", frame)

    # Display the raw grayscale image
    cv2.imshow("Thermal Camera - Grayscale", gray_frame)

    # Display the color-mapped frame (thermal effect)
    cv2.imshow("Thermal Camera - Colormap", thermal_colored)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close all OpenCV windows
cap.release()
cv2.destroyAllWindows() 