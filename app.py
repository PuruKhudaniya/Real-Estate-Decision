# Streamlit app for E-Career Consultation (app.py)
import streamlit as st
import joblib

st.title('E-Career Consultation — Advanced Demo')
st.write('Enter your skills (comma separated), e.g. python, sql, visualization')

model = joblib.load('src/ecareer_model.joblib') if Path('src/ecareer_model.joblib').exists() else None

skills = st.text_area('Skills', 'python, sql, visualization')
if st.button('Recommend'):
    if model is None:
        st.error('Model artifact not found. Run train.py first to create src/ecareer_model.joblib')
    else:
        probs = model.predict_proba([skills])[0]
        classes = model.named_steps['clf'].classes_
        res = sorted(zip(classes, probs), key=lambda x: x[1], reverse=True)
        for career, p in res[:5]:
            st.write(f'{career}: {p*100:.1f}%')
