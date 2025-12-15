from models.model import load_mobilenet_model, load_clip_model
from utils.preprocessing import preprocess_image

def recommend_outfit(image_path):
    print("Loading models...")
    mobilenet = load_mobilenet_model()
    clip_model = load_clip_model()

    print("Preprocessing input image...")
    img = preprocess_image(image_path)

    print("Generating predictions...")
    mobilenet_pred = mobilenet.predict(img)

    print("Producing recommendations using CLIP...")
    # TODO: Add CLIP similarity code
    print("Recommendation pipeline executed successfully.")

if __name__ == "__main__":
    recommend_outfit("sample.jpg")
