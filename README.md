# Real-Estate-Decision  

RandomForestRegressor model with a Streamlit UI for price prediction.
Files:
- data/housing_200.csv
- train.py (trains and saves model to src/)
- src/real_estate_model.joblib (created after running train.py)
- app.py (Streamlit demo)
- requirements.txt

How to use:
1. pip install -r requirements.txt
2. python train.py  # creates model artifact in src/
3. streamlit run app.py
