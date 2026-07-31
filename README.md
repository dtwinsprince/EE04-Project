<h1>EE04 Project</h1>
Machine learning web application built with **Streamlit** and **TensorFlow** for identifying potato leaf diseases.

*Engineering Project — EE04

**Contributors:**
- 23/EG/EE/071
- 24/EG/EE/371
- 23/EG/EE/061

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

## 📄 License

Specify a license here (e.g., MIT) or note that this is an academic project submitted as part of the EE04 Engineering curriculum.
Machine learning web application built with Streamlit and TensorFlow for identifying potato leaf diseases (EE04 Engineering Project)</p>
<p>23/EG/EE/071</p>
<p>24/EG/EE/371</p>
<p>23/EG/EE/061</p>
