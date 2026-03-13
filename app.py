import gradio as gr
import tensorflow as tf
import numpy as np
from PIL import Image
from tensorflow.keras.applications import EfficientNetB0
from tensorflow.keras.layers import (
    GlobalAveragePooling2D,
    Dense,
    BatchNormalization,
    Dropout,
)
from tensorflow.keras.models import Sequential

IMG_SIZE = 224

base_model = EfficientNetB0(weights=None, include_top=False, input_shape=(224, 224, 3))

model = Sequential(
    [
        base_model,
        GlobalAveragePooling2D(),
        BatchNormalization(),
        Dense(256, activation="relu"),
        Dropout(0.5),
        Dense(1, activation="sigmoid"),
    ]
)


model.load_weights("cat_dog.weights.h5")


def predict(img):

    img = img.resize((IMG_SIZE, IMG_SIZE))
    img = np.array(img) / 255.0
    img = np.expand_dims(img, axis=0)

    pred = model.predict(img)[0][0]

    if pred > 0.5:
        return "Dog 🐶"
    else:
        return "Cat 🐱"


demo = gr.Interface(
    fn=predict,
    inputs=gr.Image(type="pil"),
    outputs="text",
    title="Cat vs Dog Classifier",
)

demo.launch()
