from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)

with open('vader_sentiment_analyzer.pkl', 'rb') as f:
    sid = pickle.load(f)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict_sentiment():
    data = request.json
    text = data['text']

    scores = sid.polarity_scores(text)

    if scores['compound'] >= 0.05:
        sentiment = 'Happy'
    elif scores['compound'] <= -0.05:
        sentiment = 'Sad'
    else:
        sentiment = 'neutral'


    return jsonify({'sentiment': sentiment})


if __name__ == '__main__':
    app.run(debug=True)
