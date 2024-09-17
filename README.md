# 🚗 Driver Drowsiness Detection System 😴

This project detects driver drowsiness to help reduce the risk of accidents caused by fatigue. It uses real-time video streams to analyze eye movements and other facial landmarks to determine the driver's state of alertness.

---

## 🛠️ Features

- Real-time driver drowsiness detection using video input
- Alerts and warnings when drowsiness is detected
- Simple to run and integrate with any webcam

---

## 📸 Screenshots
![Screenshot 1](https://github.com/user-attachments/assets/47c7a22a-f0e8-4300-9601-6371b6974000)
![Screenshot 2](https://github.com/user-attachments/assets/58e1b1b2-f6e3-4ba6-b515-6251f1da9576)

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- OpenCV
- dlib
- imutils
- scipy
- Other dependencies listed in `requirements.txt`

### Steps to Run:

1. **Clone the Repository**  
   Download or clone this repository to your local machine:

   ```bash
   git clone https://github.com/Legend-Raj/Drowsiness-Detection.git
   ```
2.Install Dependencies
Navigate to the main folder and install the required packages:

```bash
pip install -r requirements.txt
```
Run the Application
3.Inside the main folder, open a terminal and run the following command:

```bash
python final-integration.py
```
4.Connect Your Webcam
The application will automatically detect your webcam and begin real-time drowsiness detection.


## 🧠 How It Works
Face Detection: The system detects the driver’s face using a pre-trained face detection model.
Eye Tracking: It tracks the eyes using facial landmarks to analyze the driver’s blink rate and eye closure duration.
Drowsiness Alert: If the system detects prolonged eye closure, it triggers an alert sound to wake the driver up.
## 🎯 Future Improvements
Add support for multiple cameras
Implement a more advanced alerting system (e.g., sending notifications to the driver’s phone)
Optimize the model for faster performance

