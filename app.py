import streamlit as st
import joblib
import numpy as np
import pandas as pd

dtc = joblib.load('crop_model.pkl')
sc = joblib.load('scaler.pkl')

st.title('Crop Recommendation System')
st.markdown('Enter the environmental conditions to get a crop recommendation.')

# Define min/max/mean values for input fields to make the app standalone
N_min, N_max, N_mean = 0, 140, 50
P_min, P_max, P_mean = 5, 145, 53
K_min, K_max, K_mean = 5, 205, 48
temp_min, temp_max, temp_mean = 8.8, 43.7, 25.6
humidity_min, humidity_max, humidity_mean = 14.2, 99.9, 71.5
ph_min, ph_max, ph_mean = 3.5, 9.9, 6.5
rainfall_min, rainfall_max, rainfall_mean = 20.2, 298.6, 103.5


N = st.slider('Nitrogen (N)', min_value=N_min, max_value=N_max, value=N_mean)
P = st.slider('Phosphorus (P)', min_value=P_min, max_value=P_max, value=P_mean)
K = st.slider('Potassium (K)', min_value=K_min, max_value=K_max, value=K_mean)
temperature = st.slider('Temperature', min_value=temp_min, max_value=temp_max, value=temp_mean)
humidity = st.slider('Humidity', min_value=humidity_min, max_value=humidity_max, value=humidity_mean)
ph = st.slider('pH', min_value=ph_min, max_value=ph_max, value=ph_mean)
rainfall = st.slider('Rainfall', min_value=rainfall_min, max_value=rainfall_max, value=rainfall_mean)

def predict_crop(N, P, K, temperature, humidity, ph, rainfall):
    features = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
    features_scale = sc.transform(features)
    prediction = dtc.predict(features_scale)
    return prediction[0]

if st.button('Recommend Crop'):
    prediction = predict_crop(N, P, K, temperature, humidity, ph, rainfall)
    crop_dict = {1: 'rice', 2: 'maize', 3: 'chickpea', 4: 'kidneybeans', 5: 'pigeonpeas', 6: 'mothbeans', 7: 'mungbean', 8: 'blackgram', 9: 'lentil', 10: 'pomegranate', 11: 'banana', 12: 'mango', 13: 'grapes', 14: 'watermelon', 15: 'muskmelon', 16: 'apple', 17: 'orange', 18: 'papaya', 19: 'coconut', 20: 'cotton', 21: 'jute', 22: 'coffee'}
    crop_name = crop_dict[prediction]
    st.success(f'The recommended crop is: {crop_name}')
