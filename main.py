import streamlit as st
from keras.models import load_model
from PIL import Image
import numpy as np
import tensorflow as tf
import base64
import utils

# Set the webpage title
st.markdown("<h1 style='text-align: LEFT; color: #353839; font-weight: LIGHT; font-size: 37px;'>Chocolate Image Classification</h1>", unsafe_allow_html=True)

# Brief introduction of the model
st.markdown("<h1 style='text-align: LEFT; font-size: 14px;'>This is a simple neural network model that helps classify images of white and dark <br>chocolate. While this model is rudimentary, it serves as a valuable introduction to the <br>concepts of image classification and neural networks. </h1>", unsafe_allow_html=True)


# Set overall background color and center image
background_color = "#381A14"  # Set the desired background color
center_image_path = "testimage7.jpeg"  # set the background image
utils.set_app_style(background_color, center_image_path)

# Upload files
file = st.file_uploader('Upload chocolate images', type=['jpeg', 'jpg', 'png', 'webp'])

# Load the model
model = load_model('model.h5')

# Display image and predictions
if file is not None:
    image = Image.open(file)
    new_image = image.resize((700, 400))
    st.image(new_image, use_column_width=True)

    predictions = utils.read_img2(image, model)
    st.write("## {}".format(predictions))

