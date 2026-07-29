import os
import streamlit as st
import numpy as np
from PIL import Image

st.set_page_config(
    page_title="Potato Leaf Disease Classifier",
    page_icon="🌱",
    layout="centered"
)
st.markdown("""
    <style>
    .stApp {
        background-color: #f8f9fa;
    }
    .header-card {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        padding: 2.2rem;
        border-radius: 12px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 4px 6px rgba(0,0,0,0.08);
    }
    .header-card h1 {
        color: #ffffff !important;
        font-weight: 700;
        margin-bottom: 0.4rem;
    }
    .header-card p {
        color: #e0e6ed;
        font-size: 1.05rem;
        margin: 0;
    }
    .footer {
        text-align: center;
        color: #6c757d;
        font-size: 0.85rem;
        margin-top: 3rem;
        padding-top: 1rem;
        border-top: 1px solid #dee2e6;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="header-card">
        <h1>Potato Leaf Disease Classifier</h1>
        <p>Upload a clear photo of a potato leaf to analyze its health status</p>
    </div>
""", unsafe_allow_html=True)

@st.cache_resource
def loadvalidationnetwork():
    import tensorflow as tf
    mobilenet = tf.keras.applications.mobilenet_v2.MobileNetV2
    return mobilenet(weights='imagenet')

@st.cache_resource
def loadclassifier():
    import tensorflow as tf
    currentfolder = os.path.dirname(__file__)
    modelpath = os.path.join(currentfolder, "model.keras")
    if not os.path.exists(modelpath):
        return None
    return tf.keras.models.load_model(modelpath)

uploadedfile = st.file_uploader("Choose a leaf image", type=["jpg", "png", "jpeg"])

if uploadedfile is not None:
    leftcolumn, rightcolumn = st.columns([1, 1.1])

    with leftcolumn:
        uploadedimage = Image.open(uploadedfile).convert('RGB')
        st.image(uploadedimage, caption='Uploaded Image', use_container_width=True)

    with rightcolumn:
        st.markdown("### Analysis Options")
        st.write("Click below to run image validation")
        analyzebutton = st.button("Analyze Leaf", type="primary", use_container_width=True)

    if analyzebutton:
        with st.spinner("Validating image and analyzing..."):
            import tensorflow as tf
            preprocessinput = tf.keras.applications.mobilenet_v2.preprocess_input
            decodepredictions = tf.keras.applications.mobilenet_v2.decode_predictions

            validationnetwork = loadvalidationnetwork()
            resizedforvalidation = uploadedimage.resize((224, 224))
            validationarray = np.array(resizedforvalidation)
            expandedarray = np.expand_dims(validationarray, axis=0)
            preppedarray = preprocessinput(expandedarray.copy())
            validationresult = validationnetwork.predict(preppedarray, verbose=0)
            decodedpredictions = decodepredictions(validationresult, top=10)[0]

            validtags = ['leaf', 'plant', 'potato', 'croton', 'cabbage', 'herb', 'vegetable', 'foliage']
            isvalidleaf = any(
                any(tag in label.lower() for tag in validtags) and confidence > 0.01
                for (code, label, confidence) in decodedpredictions
            )

            st.write("---")

            if not isvalidleaf:
                st.error("The EE04 project cannot confidently classify this image. Please provide a closer, clearer photo of the potato leaf")
            else:
                classifier = loadclassifier()
                if classifier is None:
                    st.error("Model file was not found. Place model.keras in the app directory and reload.")
                else:
                    resizedforprediction = uploadedimage.resize((224, 224))
                    predictionarray = np.array(resizedforprediction) / 255.0
                    predictionarray = np.expand_dims(predictionarray, axis=0)
                    predictionscore = float(classifier.predict(predictionarray, verbose=0)[0][0])

                    if predictionscore > 0.60:
                        st.success(f"Prediction: Healthy Leaf (Confidence: {predictionscore*100:.1f}%)")
                    elif predictionscore < 0.40:
                        st.error(f"Prediction: Early Blight Detected (Confidence: {(1-predictionscore)*100:.1f}%)")
                    else:
                        st.warning("Uncertain Prediction: The EE04 project cannot confidently classify this image. Please provide a clearer leaf picture or single photo of the leaf for better results")

st.markdown("""
    <div class="footer">
        Potato Leaf Disease Classifier | EE04 Project
    </div>
""", unsafe_allow_html=True)