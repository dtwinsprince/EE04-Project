<h1>EE04 Project</h1>
Machine learning web application built with **Streamlit** and **TensorFlow** for identifying potato leaf diseases.

*Engineering Project — EE04

**Contributors:**
- 23/EG/EE/071
- 24/EG/EE/371
- 23/EG/EE/061
- 23/EG/EE/001
## 📋 Overview

This project uses a deep learning model to classify potato leaf images into disease categories, helping farmers and agronomists quickly identify plant health issues through a simple web interface.

## ✨ Features

- Upload a potato leaf image and get an instant disease prediction
- TensorFlow/Keras-based image classification model
- Simple, interactive Streamlit web interface
- Displays prediction confidence for each class

## 🦠 Disease Classes

- Early Blight
- Late Blight
- Healthy

*(Update this list to match your actual model's output classes.)*

## 🛠️ Tech Stack

- **Python 3**
- **TensorFlow / Keras** — model training and inference
- **Streamlit** — web application frontend
- **NumPy / Pillow** — image preprocessing

## 📦 Installation

1. Clone the repository
   ```bash
   git clone https://github.com/<your-username>/EE04-Project.git
   cd EE04-Project
   ```

2. Create a virtual environment (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Usage

Run the Streamlit app:
```bash
streamlit run app.py
```

Then open the local URL shown in your terminal (typically `http://localhost:8501`), upload a potato leaf image, and view the predicted disease class along with confidence scores.

## 📁 Project Structure

```
EE04-Project/
├── app.py                # Streamlit application entry point
├── model/                 # Trained model files (.h5 / SavedModel)
├── requirements.txt       # Python dependencies
├── data/                  # Sample or training dataset (if included)
└── README.md
```

*(Update this structure to match your actual repo layout.)*

## 🧠 Model

The classification model was trained on a dataset of potato leaf images labeled by disease type. Update this section with details such as:
- Dataset source (e.g., PlantVillage)
- Model architecture (e.g., CNN, MobileNet, ResNet)
- Training accuracy / validation accuracy
- Number of epochs, image size, etc.

## 👥 Contributors

| Name | Roll Number |
|------|--------------|
| —    | 23/EG/EE/071 |
| —    | 24/EG/EE/371 |
| —    | 23/EG/EE/061 |
| —    | 23/EG/EE/001 |
## 📄 License

Specify a license here (e.g., MIT) or note that this is an academic project submitted as part of the EE04 Engineering curriculum.
Machine learning web application built with Streamlit and TensorFlow for identifying potato leaf diseases (EE04 Engineering Project)</p>
<p>23/EG/EE/071</p>
<p>24/EG/EE/371</p>


<p>23/EG/EE/101</p>
=======
<p>23/EG/EE/061</p>

<p>23/EG/EE/081</p>
<p>23/EG/EE/001</p>

# Potato & Banana Disease / Ripeness Classifier (EE04 Project)

This repository contains my **EE04 Project**, focused on building lightweight computer vision web applications to classify agricultural images using Convolutional Neural Networks (CNNs) and Streamlit.

---

## 📌 Project Overview

As part of my EE04 coursework, I developed interactive classification models to evaluate leaf health and fruit status:
1. **Potato Leaf Disease Classifier:** Classifies potato leaf images into *Healthy* vs. *Early Blight*.
2. **Banana Ripeness Analyzer:** Evaluates banana images into *Ripe* vs. *Unripe* states.

The main objective was to create a functional end-to-end pipeline—from dataset sourcing and transfer learning to a mobile-responsive web app deployment.

---

## 🛠️ Technical Stack & Architecture

* **Framework:** Python, TensorFlow / Keras
* **Model Architecture:** MobileNetV2 (Transfer Learning with custom binary classification heads)
* **Frontend UI:** Streamlit
* **Image Processing:** OpenCV / PIL, MobileNetV2 preprocessing utilities

---

## 📂 Repository Structure

EE04-Project/
├── EE04/
│   ├── app.py                 # Streamlit application interface
│   ├── train_banana.ipynb     # Model training notebook for Banana Ripeness
│   ├── banana_model.keras     # Saved TensorFlow Keras model
│   └── dataset/               # Sourced image classes (Ripe vs. Unripe)
├── .gitignore
└── README.md

---

## 🔍 Key Insights & Observed Limitations

Developing and testing these models highlighted important real-world computer vision behaviors:

### 1. Studio vs. Field Image Generalization (Domain Shift)
* The leaf disease classifier was trained primarily on studio-style dataset images (single leaf, isolated plain background, controlled lighting).
* **Observed Behavior:** When tested on real field photos (natural garden environments, outdoor sunlight, background soil, or multi-leaf clusters), the model can produce high-confidence false predictions due to background interference.
* **Takeaway:** Model confidence scores do not inherently measure out-of-distribution input validity. High accuracy on studio validation sets does not automatically translate to complex field settings without field-sampled training data.

### 2. Preprocessing Dependencies
* Using standard pixel normalization (`/ 255.0`) vs. model-specific preprocessing functions (`tf.keras.applications.mobilenet_v2.preprocess_input`) directly impacts feature extraction accuracy when using transfer learning backbones.

---

## 🚀 How to Run Locally

### 1. Clone the Repository
git clone https://github.com/eseobodom/EE04-Project.git
cd EE04-Project/EE04

### 2. Install Dependencies
pip install -r requirements.txt

### 3. Launch Streamlit Application
streamlit run app.py

---

## 👤 Author

Akpan, Success Aniefiok
23/EG/EE/031
Electrical & Electronics Engineering



# Potato Disease & Citrus Quality Classifier (EE04 Project)

This repository contains my **EE04 Project**, focusing on lightweight deep learning web applications designed for automated agricultural vision tasks using Convolutional Neural Networks (CNNs) and Streamlit.

---

## 📌 Project Overview

Developed as part of the EE04 engineering coursework, this project implements interactive computer vision models to evaluate crop health and fruit condition:

1. **Potato Leaf Disease Classifier:** Identifies and classifies leaf health into *Healthy* vs. *Early Blight*.
2. **Citrus Quality & Ripeness Evaluator:** Analyzes citrus fruit conditions into *Fresh/Ripe* vs. *Defective/Rotten*.

The project demonstrates an end-to-end Machine Learning pipeline—covering custom dataset sourcing, transfer learning fine-tuning, model optimization, and a responsive web interface.

---

## 🛠️ Technical Stack & Architecture

* **Core Engine:** Python 3.10+, TensorFlow / Keras
* **Model Backbone:** EfficientNetB0 (Transfer Learning with custom binary head)
* **Frontend UI:** Streamlit (Custom Responsive Layout)
* **Data Processing:** OpenCV, PIL, NumPy
* **Evaluation Metrics:** Confusion Matrix, Precision, Recall, Loss/Accuracy Curves

---

## 📂 Repository Structure

```text
EE04-Project/
├── EE04/
│   ├── app.py                      # Main Streamlit web app interface
│   ├── train_potato.ipynb          # Training notebook for Potato Leaf Disease
│   ├── train_citrus.ipynb          # Training notebook for Citrus Quality
│   ├── models/
│   │   ├── potato_model.keras      # Saved Keras model for potato leaf classifier
│   │   └── citrus_model.keras      # Saved Keras model for fruit quality evaluator
│   └── dataset/                    # Evaluation image directories
├── .gitignore
├── requirements.txt
└── README.md

```

---

## 🔍 Key Insights & Technical Observations

Building and deploying these lightweight vision pipelines provided critical engineering takeaways regarding model behavior in practical settings:

### 1. Robustness Against Visual Noise & Background Clutter

* Models trained exclusively on studio-style images (single leaf on a plain background) struggle when deployed in natural field conditions (soil, multi-leaf clusters, direct sunlight).
* **Observation:** Incorporating aggressive Data Augmentation (random rotation, shear, brightness variation, and zoom) significantly reduced false positive rates under real field conditions.

### 2. Fine-Tuning vs. Feature Extraction

* Unfreezing the top layer blocks of the pre-trained EfficientNetB0 backbone allowed the network to adapt better to localized biological patterns (e.g., small early blight lesions on potato leaves) compared to completely frozen feature extractors.

### 3. Preprocessing Dependencies & Deployment Latency

* Ensuring exact alignment between training preprocessing and inference pipelines (e.g., matching normalizations) was crucial for maintaining classification accuracy during live Streamlit deployment.

---

## 🚀 How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/johnsongideon/EE04-Project.git
cd EE04-Project/EE04

```

### 2. Set Up Environment & Dependencies

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt

```

### 3. Launch the Streamlit Web App

```bash
streamlit run app.py

```

---

## 👤 Author

* **Name:** Johnson Gideon Mfon
* **Reg No:** 23/EG/EE/121
* **Department:** Electrical & Electronics
