from flask import Flask, request, jsonify
from textblob import TextBlob
import tweepy
import os

app = Flask(__name__)

# Twitter API credentials from environment variables
API_KEY = os.environ.get("API_KEY")
API_SECRET = os.environ.get("API_SECRET")
ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.environ.get("ACCESS_TOKEN_SECRET")

auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

def get_tweet_sentiment(tweet):
    analysis = TextBlob(tweet)
    if analysis.sentiment.polarity > 0:
        return "positive"
    elif analysis.sentiment.polarity == 0:
        return "neutral"
    else:
        return "negative"

@app.route("/")
def home():
    return "Twitter Sentiment Analysis API"

@app.route("/analyze", methods=["GET"])
def analyze():
    username = request.args.get("username")
    count = int(request.args.get("count", 10))
    try:
        tweets = api.user_timeline(screen_name=username, count=count, tweet_mode="extended")
        result = []
        for tweet in tweets:
            sentiment = get_tweet_sentiment(tweet.full_text)
            result.append({
                "tweet": tweet.full_text,
                "sentiment": sentiment
            })
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, request, jsonify, render_template

@app.route("/")
def home():
    return render_template("index.html")

