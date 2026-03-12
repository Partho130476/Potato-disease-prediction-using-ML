import streamlit as st
import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np

# Load the trained model
model = tf.keras.models.load_model('C:/Users/SaikotDasJoy/Desktop/potato_disease/potato_disease/model.h5')

# Define the class indices manually or using ImageDataGenerator
# This should match the class indices used during training
class_indices = {
    'Early Blight': 0,
    'Late Blight': 1,
    'Healthy': 2
    # Add more classes if needed
}

# Define a function to make predictions
def predict(image):
    # Preprocess the image
    image = image.resize((150, 150))  # Resize to match the input size of the model
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    image /= 255.0

    # Make predictions
    predictions = model.predict(image)
    return predictions

# Streamlit UI
st.title("Potato Disease Prediction")
st.write("Upload an image of a potato leaf to predict its disease.")

# Reset functionality
if 'reset' not in st.session_state:
    st.session_state.reset = False

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

# Reset button
if st.button("Reset"):
    st.session_state.reset = True
    uploaded_file = None
    st.experimental_rerun()  # This will re-run the app to clear previous states

if uploaded_file is not None and not st.session_state.reset:
    # Display the uploaded image
    image = load_img(uploaded_file)
    st.image(image, caption='Uploaded Image', use_container_width=True)
    
    # Predict and display the result
    st.write("Classifying...")
    predictions = predict(image)
    predicted_class = list(class_indices.keys())[np.argmax(predictions)]
    confidence = np.max(predictions)

    st.write(f"Prediction: {predicted_class}")
    st.write(f"Confidence: {confidence:.2f}")

if st.session_state.reset:
    st.write("Click 'Upload' to start fresh.")
