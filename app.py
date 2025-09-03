# Streamlit app for Real Estate Price Prediction
import streamlit as st
import joblib
import pandas as pd

st.title('Real Estate Price Predictor — Advanced Demo')

try:
    model = joblib.load('src/real_estate_model.joblib')
except Exception as e:
    st.error('Model artifact not found. Run train.py first.\n' + str(e))
    st.stop()

area = st.number_input('Area (sqft)', min_value=300, max_value=10000, value=1500, step=50)
bedrooms = st.selectbox('Bedrooms', [1,2,3,4,5], index=2)
bathrooms = st.selectbox('Bathrooms', [1,2,3], index=1)
location = st.selectbox('Location', ['CityA','CityB','CityC','CityD'])
age = st.slider('Age of property (years)', 0, 50, 5)

if st.button('Predict'):
    X = pd.DataFrame([{'area_sqft':area,'bedrooms':bedrooms,'bathrooms':bathrooms,'location':location,'age_years':age}])
    pred = model.predict(X)[0]
    st.success(f'Predicted price (approx): {pred:.2f} (units)')
    st.write('This is a demo model built on synthetic data.')
