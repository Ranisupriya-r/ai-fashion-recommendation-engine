import tensorflow as tf
from PIL import Image
import numpy as np

def preprocess_image(image_path):
    """Prepare an image for MobileNetV2 and CLIP processing."""
    img = Image.open(image_path).resize((224, 224))
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = tf.keras.applications.mobilenet_v2.preprocess_input(img_array)
    return np.expand_dims(img_array, axis=0)

