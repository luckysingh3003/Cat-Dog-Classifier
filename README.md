# 🐶🐱 Cat vs Dog Image Classifier

This project is a deep learning application that identifies whether an uploaded image contains a **cat** or a **dog**.
The model is built using **EfficientNetB0** with transfer learning and is deployed as an interactive web application.

Users can upload an image through the web interface, and the system predicts the animal type along with a confidence score.

---

## 🌐 Live Application

You can try the model here:

https://huggingface.co/spaces/luckysingh30003/cat_dog_classifier

Upload any image of a cat or dog and the model will generate a prediction.

---

## 🧠 Model Overview

The classifier is based on **EfficientNetB0**, a convolutional neural network architecture known for high performance with relatively low computational cost.

The pretrained EfficientNet model was used as a feature extractor and additional layers were added for binary classification.

Model pipeline:

EfficientNetB0 (pretrained on ImageNet)

→ Global Average Pooling

→ Batch Normalization

→ Dense Layer (256 neurons, ReLU)

→ Dropout (0.5)

→ Output Layer (Sigmoid)

---

## 📊 Performance

After training and validation, the model achieved strong performance:

Training Accuracy: ~98–99%

Validation Accuracy: ~99%

Validation Loss: ~0.03

Dataset distribution:

Training images: ~23,000

Validation images: ~2,000

---

## 🖼 Input and Output

### Input

The model expects an image with the following properties:

* Size: 224 × 224 pixels
* 
* Color format: RGB
* 
* Pixel values scaled between 0 and 1

### Output

The model returns a probability indicating the predicted class:

0 → Cat

1 → Dog

Example result:

Dog 🐶 | Confidence: 0.94

---

## ⚙️ Technologies Used

This project was built using the following tools:

* Python
* 
* TensorFlow / Keras
* 
* EfficientNetB0
* 
* NumPy
* 
* Pillow
* 
* Gradio
* 
* Hugging Face Spaces

---

## 📁 Repository Structure

Cat-Dog-Classifier
│
├── app.py
├── cat_dog.weights.h5
├── requirements.txt
└── README.md

---

## ▶️ Running the Project Locally

Clone the repository:

git clone https://github.com/luckysingh3003/Cat-Dog-Classifier.git

Move into the project directory:

cd Cat-Dog-Classifier

Install required libraries:

pip install -r requirements.txt

Run the application:

python app.py

---

## 💡 Possible Applications

This project can be useful for:

* Learning computer vision concepts
* Demonstrating transfer learning
* Building simple image classification systems
* Educational AI projects

---

## 👤 Author

Lucky Singh
GitHub: https://github.com/luckysingh3003

