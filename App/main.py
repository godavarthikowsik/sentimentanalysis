import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pickle

nltk.download('vader_lexicon')
sid = SentimentIntensityAnalyzer()

with open('vader_sentiment_analyzer.pkl', 'wb') as f:
    pickle.dump(sid, f)
