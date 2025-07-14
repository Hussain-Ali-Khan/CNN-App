
from flask import Flask, request, jsonify, render_template
import tensorflow as tf
from tensorflow.keras.applications.vgg16 import preprocess_input
import numpy as np
from tensorflow.keras.utils import load_img, img_to_array
import os

app = Flask(__name__)

# Load the saved model
model = tf.keras.models.load_model('vgg16_model.keras')  # Adjust filename as needed

# Define class labels
class_labels = ['Organic', 'Recyclable']  # Modify based on your dataset

# Define a prediction function
def predict_image(image_path):
    # Load and preprocess the image
    image = load_img(image_path, target_size=(150, 150))  # VGG16 requires 150x150 images
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    image = preprocess_input(image)       # Preprocess the image for VGG16

    # Predict using the loaded model
    predictions = model.predict(image)

    # Binary classification with argmax
    predicted_class = np.argmax(predictions, axis=1)[0]

    return class_labels[predicted_class]

# Routes
@app.route('/')
def index():
    return render_template('index.html')  # Show the main page

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    # Save the uploaded file locally
    os.makedirs('uploads', exist_ok=True)
    filepath = os.path.join('uploads', file.filename)
    file.save(filepath)

    # Make a prediction
    prediction = predict_image(filepath)

    # Render result page
    return render_template('result.html', prediction=prediction, filename=file.filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)