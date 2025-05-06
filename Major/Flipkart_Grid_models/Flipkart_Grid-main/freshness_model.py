import cv2
import numpy as np
from keras.models import load_model

# Load your model once when the script is executed
freshness_model= load_model('D:\Grid\Flipkart_Grid\model_fruitNet.keras')

def predict_freshness(fruit_image):
    # Resize the input image to match the model's expected input shape
    fruit_image = cv2.resize(fruit_image, (256, 256))  # Resize to match model input
    fruit_image = np.expand_dims(fruit_image, axis=0)  # Add batch dimension
    fruit_image = fruit_image / 255.0  # Normalize the image if required

    # Get the prediction
    prediction = freshness_model.predict(fruit_image)

    # Assuming your model returns a numeric score or category
    freshness_score = prediction[0][0]  # Modify according to your model's output

    return float(freshness_score)  # Ensure it's a float, could be formatted as needed
