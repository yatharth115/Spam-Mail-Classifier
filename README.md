
# 📩 Spam Mail Classifier

A simple **machine learning project** that classifies text messages as **Spam** or **Ham (Not Spam)** using **Naive Bayes** and **TF-IDF vectorization**.  
The project also comes with an interactive **Streamlit web app** for real-time predictions.

---

## 🚀 Features
- Classify text messages as **Spam** or **Ham**.
- Interactive **Streamlit app** for testing.
- Pre-trained **Naive Bayes model** with TF-IDF features.
- Ability to test single messages or extend to batch (CSV) prediction.

---

## 📂 Project Structure
📦 Spam Mail Classifier
┣ 📜 app.py # Streamlit web app
┣ 📜 spam_model.pkl # Saved trained model
┣ 📜 vectorizer.pkl # Saved TF-IDF vectorizer
┣ 📜 requirements.txt # Required dependencies
┣ 📜 Spam_Mail_Classifier_Notebook.ipynb # Training notebook


---

## ⚙️ Installation & Setup

1. **Clone the repository** (or download files)
   ```bash
   git clone https://github.com/your-username/spam-mail-classifier.git
   cd spam-mail-classifier

2. **Create virtual environment** 
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows

3. **Install dependencies**
   pip install -r requirements.txt

4. **Run the Streamlit app**
   streamlit run app.py

## 🧠 Model Details
Algorithm: Multinomial Naive Bayes

Feature Extraction: TF-IDF (max_features = 3000, stop words = English)

Dataset: SMS Spam Collection Dataset (UCI ML Repository)

Evaluation Metrics: Accuracy, Precision, Recall, F1-score

## 📊 Example Predictions
Input: "Congratulations! You've won a $500 gift card."
Output: Spam 🚨

Input: "Hey, are we meeting tomorrow?"
Output: Ham ✅

## 📸 Screenshot
<img width="1919" height="908" alt="image" src="https://github.com/user-attachments/assets/374d9f2a-6dd4-4ebb-b44b-1d4e6ce31446" />

## 👨‍💻 Author
Yatharth Joshi
📧 Email: joshiyatharth7@gmail.com
🌐 GitHub: yatharth115





