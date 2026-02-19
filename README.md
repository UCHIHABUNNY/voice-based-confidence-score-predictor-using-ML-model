                           🎙️ Voice-Based Confidence Score Predictor using Machine Learning
📌 Project Overview

This project predicts a speaker’s confidence level by converting speech into text and analyzing its sentiment.

The system was initially built using rule-based confidence scoring. It was later enhanced with a Machine Learning model (Logistic Regression) to enable data-driven binary classification.

Final Output:
1 → Confident
0 → Not Confident

🚀 How It Works
1️⃣ Speech to Text

Speech input is converted into text using Google Speech Recognition (Pre-trained Model) developed by Google.

2️⃣ Sentiment Analysis

The extracted text is analyzed using TextBlob (Pre-trained NLP Library) to calculate sentiment polarity.

Polarity Range:

-1 → Negative

0 → Neutral

+1 → Positive

3️⃣ Confidence Prediction
🔹 Initial Approach (Rule-Based)

Confidence was estimated directly from sentiment polarity using custom logic.

🔹 Enhanced Approach (Machine Learning)

A Logistic Regression classifier was trained on labeled speech text data to perform supervised binary classification.

Learning Type: Supervised ML

Classification Type: Binary

Model: Logistic Regression

Output: 1 (Confident) / 0 (Not Confident)

📊 Dataset Requirement

The project does NOT require a dataset for prediction (inference).

The project DOES require labeled data to train and improve the model.

Training data helps the system learn patterns that better represent confident and non-confident speech.

🏗️ System Architecture

Speech Input
↓
Speech Recognition (Google Pre-trained Model)
↓
Sentiment Analysis (TextBlob)
↓
Logistic Regression Model
↓
Confidence Prediction (0 / 1)

🛠 Technologies Used

Python

Google Speech Recognition

TextBlob

Scikit-learn

Natural Language Processing (NLP)

Machine Learning

⚠️ Limitations

Confidence is estimated only from text sentiment polarity.

Does not consider vocal features such as:

Tone

Pitch

Speech rate

Pauses

Sentiment does not always directly represent true confidence.

🔮 Future Improvements

Integrate audio feature analysis (prosody, pitch, tempo)

Use Deep Learning models (LSTM / Transformers)

Build real-time confidence detection system

Deploy as a web application or API

📁 Project Structure
├── main.py
├── model_training.py
├── dataset.csv
├── requirements.txt
└── README.md
👨‍💻 Author

G Murali Sandeep
Machine Learning & NLP Enthusiast
