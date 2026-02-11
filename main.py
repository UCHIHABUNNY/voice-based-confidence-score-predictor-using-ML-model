

from textblob import TextBlob


text = input("Enter your speech text: ")

blob = TextBlob(text)
polarity = blob.sentiment.polarity

confidence_score = (polarity + 1) * 50  # scale 0–100

print("Confidence Score:", round(confidence_score, 2))

