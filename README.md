

# AI Rover for Border Security

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE) [![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)](https://github.com/your-username/ai-rover-border-security/actions)

The **AI Rover for Border Security** is an advanced, AI-powered surveillance system designed to enhance border security operations. Utilizing cutting-edge technology, this rover is capable of real-time detection of suspicious human activity in border areas. This project aims to aid military personnel by reducing their time and effort in monitoring border zones.

---

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

---

## Team Members
- **Eshank** - Robotics Engineer
- **Nandini** - AI Engineer
- **Mohit** - Web Designer
- **Aayush** - Web Developer

---

## Technologies Used

### Here are the core technologies utilized in this project:

|                               |  |
| ------------------------------------ | ---- |
| Microcontroller for radar data       | <img src="https://img.shields.io/badge/Arduino-%23CC0000.svg?style=for-the-badge&logo=Arduino&logoColor=white" alt="Arduino Badge"> |
| Video streaming from the rover       | <img src="https://img.shields.io/badge/ESP32-CAM-CC00FF.svg?style=for-the-badge&logo=esp32" alt="ESP32 Badge"> |
| Image processing and computer vision | <img src="https://img.shields.io/badge/OpenCV-%23009639.svg?style=for-the-badge&logo=opencv&logoColor=white" alt="OpenCV Badge"> |
| Neural network API for AI            | <img src="https://img.shields.io/badge/Keras-%23FF6C37.svg?style=for-the-badge&logo=keras&logoColor=white" alt="Keras Badge"> |
| Data display for surveillance system | <img src="https://img.shields.io/badge/Streamlit-%23FF5C00.svg?style=for-the-badge&logo=streamlit" alt="Streamlit Badge"> |
| Database for storing data            | <img src="https://img.shields.io/badge/MongoDB-%2347A248.svg?style=for-the-badge&logo=mongodb&logoColor=white" alt="MongoDB Badge"> |
| Backend for handling requests        | <img src="https://img.shields.io/badge/Node.js-%23339933.svg?style=for-the-badge&logo=node.js&logoColor=white" alt="Node.js Badge"> |
| Frontend for user interface          | <img src="https://img.shields.io/badge/HTML5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white" alt="HTML Badge"> <img src="https://img.shields.io/badge/CSS3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white" alt="CSS Badge"> <img src="https://img.shields.io/badge/JavaScript-%23F7DF1E.svg?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript Badge"> |
| Core AI processing language          | <img src="https://img.shields.io/badge/Python-%233776AB.svg?style=for-the-badge&logo=python&logoColor=white" alt="Python Badge"> |
| API testing tool                     | <img src="https://img.shields.io/badge/Postman-%23FF6C37.svg?style=for-the-badge&logo=postman&logoColor=white" alt="Postman Badge"> |
| Domain hosting service               | <img src="https://img.shields.io/badge/GoDaddy-%231A6ED8.svg?style=for-the-badge&logo=godaddy&logoColor=white" alt="GoDaddy Badge"> |

---

## Installation

To set up the project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/ai-rover-border-security.git
   ```

2. **Navigate to the project directory**:
   ```bash
   cd ai-rover-border-security
   ```

3. **Install necessary dependencies**:
   - For **Node.js**:
     ```bash
     npm install
     ```
   - For **Python**:
     ```bash
     pip install -r requirements.txt
     ```

4. **Configure environment variables**:
   Create a `.env` file in the root directory with the following variables:
   ```bash
   MONGODB_URI=your_mongo_uri
   SECRET_KEY=your_secret_key
   ```

---

## Usage

To start the application:

1. **Start the backend server**:
   ```bash
   npm start
   ```

2. **Run the Python AI component**:
   ```bash
   python ai.py
   ```

3. **Access the frontend**:
   Navigate to `http://localhost:3000` in your browser.

---

## Code Structure

```plaintext
ai-rover-border-security
│
├── backend/
│   ├── models/
│   │   └── roverModel.js        # Mongoose model for rover data
│   ├── routes/
│   │   └── roverRoutes.js       # API routes for rover operations
│   ├── controllers/
│   │   └── roverController.js   # Logic for handling requests
│   ├── server.js                # Main server file
│   ├── .env                     # Environment variables
│   └── package.json             # Node.js dependencies
│
├── frontend/
│   ├── public/
│   │   └── index.html           # Main HTML file
│   ├── src/
│   │   ├── App.js               # Main React component
│   │   ├── index.js             # React entry point
│   │   └── components/          # React components for UI
│   └── package.json             # Frontend dependencies
│
└── requirements.txt             # Python dependencies
```

---

## Features

- **Real-time Human Detection**: Using CNN for detecting human activity.
- **Thermal Imaging**: Captures and analyzes thermal data.
- **GPS Tracking**: Monitors the rover's location with real-time updates.
- **Dashboard Interface**: A clean, responsive UI displaying the rover’s status, video feed, and map.
- **Object Detection**: Integrated object detection via the Roboflow API.

---

## Future Work

- **Drone Integration**: Expanding the project to integrate aerial surveillance via drones.
- **Improved AI Models**: Incorporating more sophisticated models to enhance detection accuracy.
- **Edge Computing**: Deploy AI capabilities directly on the rover for faster response times.

---

## Contributing

We welcome contributions! Please follow our [contributing guidelines](CONTRIBUTING.md) for details on submitting pull requests and issues.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

---

## Acknowledgements

- Thanks to the developers of OpenCV, Keras, and other open-source libraries that made this project possible.
- Special thanks to the military personnel whose feedback guided the development process.

---

## Contact

For any questions or suggestions, feel free to reach out:

- **Email**: contact@garudrover.co
- **Website**: [garudrover.co](http://garudrover.co)

---
