import tensorflow as tf
import base64
import streamlit as st 
import numpy as np

# Changing the webapp background
def set_app_style(background_color, center_image_path):
    # Read the image for centering
    with open(center_image_path, 'rb') as f:
        image_data = f.read()
        image_base64 = base64.b64encode(image_data).decode()

    # Apply custom CSS styles
    st.markdown(
        f"""
        <style>
        body {{
            background-color: {background_color};
        }}
        .stApp {{
            background: url(data:image/png;base64,{image_base64}) center center no-repeat;
            background-size: 750px 100%;
            display: flex;
            align-items: center;
            justify-content: center;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )


# Making Predictions
def read_img2(image, model):
    resize = tf.image.resize(image, (256, 256))
    yhat = model.predict(np.expand_dims(resize / 255, 0))

    if yhat > 0.5:
        return 'This is a White Chocolate'
    else:
        return 'This is a Dark Chocolate'