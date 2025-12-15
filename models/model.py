import tensorflow as tf
import torch
import clip

def load_mobilenet_model():
    """Load MobileNetV2 pretrained model for outfit classification."""
    model = tf.keras.applications.MobileNetV2(weights="imagenet", include_top=True)
    print("MobileNetV2 model loaded.")
    return model

def load_clip_model():
    """Load CLIP (image + text embeddings) for similarity search."""
    model, preprocess = clip.load("ViT-B/32")
    print("CLIP model loaded.")
    return {"model": model, "preprocess": preprocess}

