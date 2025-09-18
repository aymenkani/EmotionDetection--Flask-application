# Emotion Detection Web Application

This project is a Python-based web application built with Flask that analyzes text to detect the dominant emotion. The application leverages an underlying AI service to classify emotions such as joy, sadness, anger, disgust, and fear.

It is designed as a hands-on project to demonstrate skills in Python development, REST API creation, web deployment with Flask, unit testing, and static code analysis.

## 🚀 Core Features

* **Real-time Emotion Analysis:** Enter any text statement to get an instant emotion classification.
* **Simple Web Interface:** A clean and straightforward UI to interact with the model.
* **REST API Endpoint:** Provides a programmatic way to get emotion predictions via a simple API call.
* **Well-Tested:** Includes a suite of unit tests to ensure the core logic is reliable.
* **Easily Deployable:** Packaged as a standard Flask application.

---

## 🛠️ Technology Stack

* **Backend:** Python, Flask
* **AI/ML:** IBM Watson NLP Library (via an API)
* **Testing:** `unittest`
* **Code Analysis:** Pylint

---

## ⚙️ How It Works

The application is composed of two main parts:

1.  **Core Emotion Detection Logic (`emotion_detection.py`):** This module contains the `emotion_detector` function, which takes text as input, sends it to a backend emotion analysis service, and processes the JSON response to extract the dominant emotion.

2.  **Flask Web Server (`app.py`):** This script creates a web server with two primary routes:
    * A main route (`/`) that renders the web interface (`index.html`).
    * An API endpoint (`/emotionDetector`) that receives text from the web form, passes it to the `emotion_detector` function, and returns the formatted result.

---

## 🏁 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

* Python 3.8+
* `pip` for installing packages

###  Clone the Repository

First, clone the repository to your local machine using git:

    
    git clone https://github.com/aymenkani/EmotionDetection--Flask-application.git
    cd EmotionDetection--Flask-application



## How to Run the Application
1. Run the Flask Server
Execute the app.py script from the root directory of the project:
   ```bash
   python app.py

2. Use the Web Interface
Open your web browser and navigate to `http://127.0.0.1:5000`. You will see a simple form where you can enter text. Submit a sentence, and the application will display the detected emotions and the dominant one.


## ✅ Running Tests
The project includes a suite of unit tests for the core emotion detection logic. To run the tests, execute the test_emotion_detection.py module:
   ```bash
   python -m unittest emotion_detection.test_emotion_detection
