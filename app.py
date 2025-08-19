import streamlit as st
import joblib

# Load model and vectorizer
model = joblib.load("spam_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

st.title("📧 Spam Mail Classifier")

user_input = st.text_area("Enter a message:")

if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("Please enter a message.")
    else:
        vec = vectorizer.transform([user_input])
        prediction = model.predict(vec)[0]
        label = "🚨 Spam" if prediction == 1 else "✅ Ham (Not Spam)"
        st.success(f"Prediction: {label}")
