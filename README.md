# 🌾 SmartCropAdvisor - AI-powered intelligent crop recommender

---

## 🎯 Project Goal

SmartCropAdvisor is designed to help farmers, agri-tech users, and researchers identify the most suitable crop to grow under given soil and environmental conditions. The goal is to improve productivity and sustainability by leveraging machine learning for smart agriculture.

---

## 📚 Project Overview

SmartCropAdvisor is a machine learning-powered web app built using Streamlit. It analyzes key input parameters like nitrogen, phosphorus, potassium levels, temperature, humidity, pH, and rainfall, and predicts the most suitable crop using a trained Decision Tree model.

The web interface provides a user-friendly experience where users can easily enter their environmental conditions and instantly get a crop recommendation.

---

## 🔁 Project Workflow

### 1. **Data Preprocessing**
- The dataset was loaded and checked for inconsistencies or missing values.
- Features were standardized using `StandardScaler` to normalize the input range and improve model performance.
- Inputs include:
  - Nitrogen (N), Phosphorus (P), Potassium (K)
  - Temperature, Humidity, pH, Rainfall

### 2. **Model Building**
- Used a **Decision Tree Classifier** from `scikit-learn`.
- Trained the model using 80% of the dataset and tested on the remaining 20%.
- Serialized the model (`crop_model.pkl`) and scaler (`scaler.pkl`) using `joblib` for integration with the Streamlit app.

### 3. **Evaluation Metrics**
- **Accuracy:** Achieved **99%** on test data.
- Chose Decision Tree for its interpretability and efficiency on this type of classification problem.

### 4. **Deployment**
- Built the frontend using **Streamlit**.
- Deployed locally as a standalone web app.
- Simple and interactive UI with sliders for inputs and real-time output display.

---

## 🧰 Tech Stack

- **Frontend/UI:** Streamlit
- **Backend & Logic:** Python
- **Libraries Used:**
  - `pandas`, `numpy` – Data processing
  - `scikit-learn` – ML model and preprocessing
  - `joblib` – Saving the model
  - `matplotlib` – For data visualization during EDA
  - `streamlit` – Web interface

---

## 📁 Project Structure

```plaintext
SmartCropAdvisor/
├── Dataset/                              # Folder containing the dataset
│   └── Crop_recommendation.csv           # Main dataset used for training the model
├── Crop_Recommendation_System.ipynb      # Jupyter notebook for data analysis and model training
├── README.md                             # Project documentation
├── app.py                                # Streamlit web application
├── crop_model.pkl                        # Trained Decision Tree Classifier model
├── requirements.txt                      # Python dependencies
└── scaler.pkl                            # StandardScaler object used for input scaling

```
---

## 📬 Contact

<p>
  <a href="mailto:aradhyaray99@gmail.com"><img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" /></a>
  <a href="www.linkedin.com/in/rayaradhya"><img src="https://img.shields.io/badge/LinkedIn-blue?style=for-the-badge&logo=linkedin&logoColor=white" /></a>
  <a href="https://github.com/AradhyaRay05"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" /></a>
</p>

---

Thanks for visiting ! Feel free to explore my other repositories and connect with me. 🚀 
