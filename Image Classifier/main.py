import cv2
import numpy as np

from tensorflow.keras.applications.mobilenet_v2 import (
    MobileNetV2,
    preprocess_input,
    decode_predictions
)
import streamlit as st
from PIL import Image

def load_model():
    model=MobileNetV2(weights="imagenet")
    return model

def preprocess_image(image):
    img=np.array(image)
    img=cv2.resize(img,(224,224))
    img=preprocess_input(img)
    img=np.expand_dims(img,axis=0)
    return img

def classify_image(model,image):
    try:
        processed_image=preprocess_image(image)
        predictions=model.predict(processed_image)
        decoded_predictions=decode_predictions(predictions,top=3)[0]
        
        return decoded_predictions
    except Exception as e:
        st.error(f"Error while classifying image:{str(e)}")
        return None
    
    
def main():
    st.set_page_config(page_title="AI IMAGE CLASSIFIER", page_icon="📕", layout="centered")
    st.title("AI IMAGE CLASSIFIER")
    st.write("Upload an Image And Let AI classify what is in it!")

    @st.cache_resource
    def load_cached_model():
        return load_model()

    model = load_cached_model()

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file).convert("RGB")  # Correctly open image
        st.image(image, caption="Uploaded Image", use_container_width=True)
        
        if st.button("Classify Image"):
            with st.spinner("Analyzing Image..."):
                predictions = classify_image(model, image)  # Pass model

                if predictions:
                    st.subheader("Predictions")
                    for _, label, score in predictions:
                        st.write(f"**{label}**: {score:.2%}")

    
if __name__=="__main__":
    main()
        