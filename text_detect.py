from textblob import TextBlob

def detect_text_emotion(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity

    if polarity > 0:
        return "happy"
    elif polarity < 0:
        return "sad"
    else:
        return "neutral"