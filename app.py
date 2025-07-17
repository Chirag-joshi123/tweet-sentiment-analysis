from flask import Flask, request, jsonify, render_template
from textblob import TextBlob
import tweepy
import os

# Load environment variables from .env file if present
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

# Twitter API credentials from environment
API_KEY = os.environ.get("API_KEY")
API_SECRET = os.environ.get("API_SECRET")
ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.environ.get("ACCESS_TOKEN_SECRET")

# Check for missing credentials
if not all([API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET]):
    raise ValueError("One or more Twitter API credentials are missing. Please check your environment variables.")

# Authenticate with Twitter
auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# Analyze sentiment using TextBlob
def get_tweet_sentiment(tweet):
    analysis = TextBlob(tweet)
    if analysis.sentiment.polarity > 0:
        return "positive"
    elif analysis.sentiment.polarity == 0:
        return "neutral"
    else:
        return "negative"

# Frontend route
@app.route("/")
def home():
    return render_template("index.html")

# Sentiment analysis API endpoint
@app.route("/analyze", methods=["GET"])
def analyze():
    username = request.args.get("username")
    count = int(request.args.get("count", 10))

    if not username:
        return jsonify({"error": "Missing Twitter username"}), 400

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
