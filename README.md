# CNN-App

A web application for classifying organic vs recyclable waste using a Convolutional Neural Network (CNN) model.

## Overview

This project implements a custom CNN model based on the VGG16 architecture to classify images into "organic" or "recyclable" waste categories. The model achieves an accuracy of 85%. The machine learning backend is deployed using Flask, and the frontend is built with HTML/CSS. The entire application is containerized using Docker for easy deployment.

## Features

- **Custom CNN (CCNN) based on VGG16:**  
  High-accuracy image classification (85%).
- **Web Interface:**  
  User-friendly frontend for image upload and prediction.
- **REST API:**  
  Flask backend serves predictions.
- **Dockerized Deployment:**  
  Easy to run locally or on any cloud platform.

## Getting Started

### Prerequisites

- Python 3.7+
- Docker

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Hussain-Ali-Khan/CNN-App.git
   cd CNN-App
   ```

2. **Build and run using Docker**
   ```bash
   docker build -t cnn-app .
   docker run -p 5000:5000 cnn-app
   ```
   The app will be available at `http://localhost:5000`

### Manual Setup (without Docker)

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Flask server**
   ```bash
   python app.py
   ```

## Usage

- Open the web interface.
- Upload an image of waste.
- The model classifies the image as "organic" or "recyclable".

## Project Structure

```
CNN-App/
├── model/           # CCNN model files & weights (based on VGG16)
├── app.py           # Flask backend
├── static/          # HTML/CSS frontend files
├── Dockerfile
├── requirements.txt
└── README.md
```

## Model Details

- **Architecture:** Custom CNN (CCNN) using VGG16 as the base.
- **Accuracy:** 85% on validation data.
- **Classes:** Organic waste, Recyclable waste.

## Contributing

Contributions and suggestions are welcome!  
1. Fork the repo  
2. Make your changes  
3. Submit a pull request

## License

This project is licensed under the MIT License.

## Author

Developed by [Hussain Ali Khan](https://github.com/Hussain-Ali-Khan)