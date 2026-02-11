# Note: Confidence score is based on sentiment polarity,
# not actual vocal confidence.
import speech_recognition as sr
import joblib

# Load trained model and vectorizer
model = joblib.load("confidence_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Speak now...")
    audio = r.listen(source)

try:
    text = r.recognize_google(audio)
    print("You said:", text)
except:
    print("Could not understand speech")
    exit()

# Convert speech text to vector
text_vector = vectorizer.transform([text])

# Predict confidence
probability = model.predict_proba(text_vector)[0][1]
confidence_score = round(probability * 100, 2)

# Confidence level
if confidence_score < 40:
    level = "Low Confidence"
elif confidence_score < 70:
    level = "Medium Confidence"
else:
    level = "High Confidence"

print("Confidence Level:", level)
print("Confidence Score:", confidence_score)

# Save result to file
with open("results.txt", "a") as file:
    file.write(f"Speech: {text}\n")
    file.write(f"Confidence Score: {confidence_score}\n")
    file.write(f"Confidence Level: {level}\n")
    file.write("-" * 30 + "\n")

