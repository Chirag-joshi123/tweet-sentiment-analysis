# 🐦 Tweet Sentiment Analysis Web App

This is a simple Flask-based web application that uses the Twitter API v2 to fetch recent tweets based on a keyword and performs sentiment analysis using **TextBlob**. It classifies each tweet as **Positive**, **Negative**, or **Neutral**.

---

## 🔧 Features

- Fetches **recent tweets** using Twitter API v2
- Performs **sentiment analysis** using `TextBlob`
- Displays results in a clean and responsive web interface
- Built with **Flask**, **Tweepy**, and **Jinja2**

---

## 🧰 Technologies Used

- Python 3.x
- Flask
- Tweepy (Twitter API v2)
- TextBlob
- dotenv (`python-dotenv`)
- HTML (Jinja2 templating)

---

## 📦 Installation

1. **Clone the repository**

```bash
git clone https://github.com/Chirag-joshi123/tweet-sentiment-analysis.git
cd tweet-sentiment-analysis
````

2. **Create a virtual environment and activate it (optional but recommended)**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Set up your environment variables**

Create a `.env` file in the root directory:

```bash
touch .env
```

Inside `.env`, add your Twitter Bearer Token:

```
BEARER_TOKEN=your_twitter_api_bearer_token_here
```

---

## 🚀 Running the App

```bash
python app.py
```

Then open your browser and go to:
👉 [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 📄 File Structure

```
tweet-sentiment-analysis/
├── app.py               # Main Flask app
├── templates/
│   └── index.html       # HTML template for UI
├── .env                 # Environment variables (not to be shared)
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

---

## 📌 Notes

* Only tweets in **English (`lang='en'`)** are analyzed.
* The app fetches a maximum of **10 tweets** per query to respect API rate limits.
* Twitter API v2 **Bearer Token** is required — you can get one by creating a project on the [Twitter Developer Portal](https://developer.twitter.com/).

---

## 💡 Future Improvements

* Support for analyzing tweet trends
* Graphical visualization of sentiment
* OAuth login for posting or interacting with tweets
* Support for multiple languages

---

## 📝 License

This project is open-source under the [MIT License](LICENSE).

---

## 🙋‍♂️ Author

**Your Name** – [@yourhandle](https://github.com/Chirag-joshi123)
Feel free to fork, contribute, or reach out with suggestions!
