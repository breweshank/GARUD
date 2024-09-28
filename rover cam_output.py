import cv2
import requests
import time
import base64
from flask import Flask, render_template, Response, jsonify
from flask_cors import CORS
from pymongo import MongoClient
import logging

# MongoDB connection setup
client = MongoClient('mongodb://localhost:27017/')
db = client['human_detection']
collection = db['detections']

# Roboflow API key and model details
API_KEY = "mDNDGcJvWw9SUfrZYyGu"
MODEL_ENDPOINT = "https://detect.roboflow.com/human-detection-e45xq"
VERSION = 1

app = Flask(__name__)
CORS(app)

# OpenCV Video Capture (webcam)
cap = cv2.VideoCapture(0)

# Setup logging
logging.basicConfig(level=logging.DEBUG)

# Function to detect objects from a frame
def detect(frame):
    _, img_encoded = cv2.imencode('.jpg', frame)
    files = {"file": ("image.jpg", img_encoded.tobytes(), "image/jpeg")}
    params = {"api_key": API_KEY}

    response = requests.post(f"{MODEL_ENDPOINT}/{VERSION}", params=params, files=files)

    if response.status_code == 200:
        return response.json()['predictions']
    else:
        logging.error(f"Detection error: {response.status_code} - {response.text}")
        return None

# Function to store detection results in MongoDB
def store_in_mongodb(frame, predictions):
    _, buffer = cv2.imencode('.jpg', frame)
    frame_base64 = base64.b64encode(buffer).decode('utf-8')
    document = {
        "timestamp": time.time(),
        "image": frame_base64,
        "predictions": predictions
    }
    collection.insert_one(document)
    logging.debug("Frame and predictions stored in MongoDB.")

# Video streaming generator
def generate_frames():
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        resized_frame = cv2.resize(frame, (640, 480))

        # Perform detection
        predictions = detect(resized_frame)

        # Draw bounding boxes if predictions are made
        if predictions:
            for obj in predictions:
                x, y, width, height = obj['x'], obj['y'], obj['width'], obj['height']
                label = obj['class']
                start_point = (int(x - width / 2), int(y - height / 2))
                end_point = (int(x + width / 2), int(y + height / 2))
                color = (0, 255, 0)
                thickness = 2
                cv2.rectangle(resized_frame, start_point, end_point, color, thickness)
                cv2.putText(resized_frame, label, (start_point[0], start_point[1] - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)

            # Store detected frames and predictions in MongoDB
            store_in_mongodb(resized_frame, predictions)

        # Encode the frame for web display
        ret, buffer = cv2.imencode('.jpg', resized_frame)
        frame = buffer.tobytes()

        # Yield the frame in byte format to the web page
        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

# Route to stream the video
@app.route('/video_feed')
def video_feed():
    logging.debug("Accessed /video_feed route.")
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

# Route to get saved detections from MongoDB
@app.route('/detections', methods=['GET'])
def get_detections():
    logging.debug("Accessed /detections route.")
    results = collection.find().sort("timestamp", -1).limit(10)
    detections = []
    for result in results:
        detections.append({
            "timestamp": result['timestamp'],
            "image": result['image'],
            "predictions": result['predictions']
        })
    return jsonify(detections)

# HTML for the index page
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
