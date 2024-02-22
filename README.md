## Chocolate Image Classifier
This is a Streamlit web application developed for classifying images of white and dark chocolate using a Convolutional Neural Network (CNN) model. Users can upload images of chocolates, and the application will predict whether the uploaded image contains white chocolate or dark chocolate.

## Features
Image Classification: Upload chocolate images in JPEG, JPG, PNG, or WEBP formats to get predictions.
Simple Interface: User-friendly interface for easy interaction.
Model Explanation: Brief introduction of the CNN model used for classification.
Error Handling: Proper error messages for invalid image formats or processing errors.
Installation
To run the application locally, follow these steps:

1. Clone this repository:
```
git clone https://github.com/your_username/chocolate-image-classifier.git
```

3. Navigate to the project directory:
```
cd chocolate-image-classifier
```

5. Install the required dependencies:
```
pip install -r requirements.txt
```

6. Run the Streamlit app:
```
streamlit run app.py
```

7. Access the application in your web browser at http://localhost:8501.

## Model Information
The underlying CNN model (model.h5) has been trained on a dataset containing images of white and dark chocolates. The model architecture, training procedure, and evaluation metrics are detailed in the model_training.ipynb notebook available in this repository.

## Usage
Upon running the application, you'll see a webpage titled "Chocolate Image Classification" with a brief introduction to the model.
Upload chocolate images using the file uploader provided.
After uploading an image, the application will display the uploaded image along with the predicted class label (white chocolate, dark chocolate, or an error message).

## Deployment
This application can be deployed using various platforms, including Streamlit Sharing, [here](https://t.co/N1EjNvqAnz)

## Contributing
Contributions to this project are welcome. Feel free to open issues for bug fixes, feature requests, or general improvements. Pull requests are also encouraged.
