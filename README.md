# AI Rover for Border Security

## Overview
The **AI Rover for Border Security** is an advanced surveillance system designed to monitor borders effectively. Utilizing AI technology, this rover ensures real-time detection of suspicious human activity, significantly enhancing border security operations.

## Table of Contents
- [Team Members](#team-members)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Code Structure](#code-structure)
- [Features](#features)
- [Future Work](#future-work)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)
- [Contact](#contact)

## Team Members
- **Eshank** - Robotics Specialist
- **Nandini** - AI Expert
- **Mohit** - Web Designer
- **Aayush** - Web Developer

## Technologies Used
- **Microcontroller**: Arduino (for data acquisition from the radar)
- **Camera Module**: ESP32 CAM (for live video streaming)
- **AI & Computer Vision**: 
  - Convolutional Neural Networks (CNN)
  - OpenCV
  - Keras
- **Web Development**: 
  - JavaScript
  - HTML
  - CSS
  - Node.js
  - Express.js
  - MongoDB
  - Streamlit (for data display)
  - Postman API (for testing)
  - MapTiger (for mapping)
  - GoDaddy (for domain hosting)
- **Programming Language**: Python

## Installation
To set up the project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/ai-rover-border-security.git
   
2. **Navigate to the project directory**:
    ```bash
   cd ai-rover-border-security
3. **Install necessary dependencies**:
   - **For Node.js**: npm install
   - **python**: pip install -r requirements.txt
4. **Configure environment variables: Create a .env file in the root directory with the following variables:**
    MONGODB_URI=your_mongo_uri
    SECRET_KEY=your_secret_key

## Code Structure

ai-rover-border-security/
│
├── backend/
│   ├── models/
│   │   └── roverModel.js   # Mongoose model for rover data
│   ├── routes/
│   │   └── roverRoutes.js   # API routes for rover operations
│   ├── controllers/
│   │   └── roverController.js # Logic for handling requests
│   ├── server.js            # Main server file
│   ├── .env                 # Environment variables
│   └── package.json         # Node.js dependencies
│
├── frontend/
│   ├── public/
│   │   └── index.html       # Main HTML file
│   ├── src/
│   │   ├── App.js           # Main React component
│   │   ├── index.js         # React entry point
│   │   └── components/      # React components for UI
│   └── package.json         # Frontend dependencies
│
└── requirements.txt         # Python dependencies

## License
**This project is licensed under the MIT License - see the LICENSE file for details.**

## Acknowledgements
**Special thanks to all resources, libraries, and individuals that helped in the development of this project.**
