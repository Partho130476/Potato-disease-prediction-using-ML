# Potato Disease Detection System

## Description

The **Potato Disease Detection System** is a machine learning–based web application that identifies potato leaf diseases using image classification.
The model is trained using a **Convolutional Neural Network (CNN)** and deployed through a **Python Flask web application** that allows users to upload an image of a potato leaf and receive a prediction of the disease type.

This system helps farmers and researchers quickly detect plant diseases and take early preventive measures.

---

## Features

* Upload potato leaf images
* Automatic disease detection using a trained deep learning model
* Web-based interface for easy interaction
* Fast prediction using a pre-trained CNN model
* Simple and user-friendly design

---

## Technologies Used

**Programming Language**

* Python

**Machine Learning / Deep Learning**

* TensorFlow / Keras
* Convolutional Neural Networks (CNN)

**Web Framework**

* Flask

**Frontend**

* HTML
* CSS

**Other Tools**

* Jupyter Notebook
* NumPy
* OpenCV (optional depending on preprocessing)

---

## Project Structure

```
potato_disease/
│
├── appp.py                     # Flask application
├── model1.h5                   # Trained CNN model
├── potato_disease.ipynb        # Model training notebook
│
├── templates/
│   └── index.html              # Web interface
│
└── .ipynb_checkpoints/         # Notebook checkpoints
```

---

## Installation

1. Clone the repository

```
git clone https://github.com/Partho130476/potato-disease-detection.git
```

2. Navigate to the project folder

```
cd potato-disease-detection
```

3. Install required dependencies

```
pip install flask tensorflow numpy
```

4. Run the Flask application

```
python appp.py
```

5. Open your browser and go to

```
http://127.0.0.1:5000
```

---

## How It Works

1. The user uploads an image of a potato leaf.
2. The image is preprocessed and passed to the trained CNN model.
3. The model predicts the disease category.
4. The result is displayed on the web interface.

---

## Future Improvements

* Improve model accuracy with a larger dataset
* Deploy the system on a cloud platform
* Add mobile support
* Include more plant diseases

---

## Author

**Partho Das**
B.Sc. in Computer Science & Engineering
North East University Bangladesh

