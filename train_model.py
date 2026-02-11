import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

# 1. Load dataset
data = pd.read_csv("confidence_data.csv")

X = data["text"]
y = data["label"]

# 2. Convert text to numbers (TF-IDF with n-grams)
vectorizer = TfidfVectorizer(
    ngram_range=(1, 3),     # unigrams + bigrams + trigrams
    stop_words="english"
)

X_vec = vectorizer.fit_transform(X)

# 3. Train Logistic Regression model
model = LogisticRegression()
model.fit(X_vec, y)

# 4. Save model and vectorizer
joblib.dump(model, "confidence_model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("Model training completed and saved successfully.")
