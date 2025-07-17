import os
from flask import Flask, render_template, request
from textblob import TextBlob
import tweepy
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Twitter API V2 Credentials
BEARER_TOKEN = os.getenv('BEARER_TOKEN')

# Initialize Tweepy Client for V2
client = tweepy.Client(bearer_token=BEARER_TOKEN)


def analyze_sentiment(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    if polarity > 0:
        return 'Positive'
    elif polarity < 0:
        return 'Negative'
    else:
        return 'Neutral'


@app.route('/', methods=['GET', 'POST'])
def index():
    results = []
    keyword = ""

    if request.method == 'POST':
        keyword = request.form['keyword']
        try:
            response = client.search_recent_tweets(
                query=keyword, max_results=10, tweet_fields=['text', 'lang'])
            tweets = response.data or []

            for tweet in tweets:
                tweet_text = tweet.text
                sentiment = analyze_sentiment(tweet_text)
                results.append({'tweet': tweet_text, 'sentiment': sentiment})
        except Exception as e:
            print(f"Error fetching tweets: {e}")
            results.append(
                {'tweet': 'Error fetching tweets.', 'sentiment': 'N/A'})

    return render_template('index.html', results=results, keyword=keyword)


if __name__ == '__main__':
    app.run(debug=True)
