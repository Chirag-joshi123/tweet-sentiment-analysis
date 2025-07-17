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

## 🔑 How to Get Your Twitter API Bearer Token

1. Go to the [Twitter Developer Portal](https://developer.twitter.com/)
2. Log in with your Twitter account and click on **Developer Portal**
3. Click **Projects & Apps > Overview > + Create App**
4. After creating the app:

   * Go to your **App Settings**
   * Navigate to **Keys and Tokens**
   * Copy the **Bearer Token** and paste it into your `.env` file

Make sure to keep it **private** and never expose it in public repositories.

---

## 🚀 Running the App Locally

```bash
python app.py
```

Then open your browser and go to:
👉 [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🌍 Deploying on Render (Free Hosting)

Render makes it easy to deploy Flask apps.

### Step-by-step:

1. **Push your code to GitHub**

2. Go to [https://render.com](https://render.com) and sign in

3. Click on **"New Web Service"**

4. Connect your GitHub repo and select this project

5. Use the following settings:

   * **Build Command:**

     ```
     pip install -r requirements.txt
     ```
   * **Start Command:**

     ```
     gunicorn app:app
     ```
   * **Runtime:** Python 3.x
   * **Environment Variables:**
     Add your `BEARER_TOKEN` key here.

6. Click **"Create Web Service"**

Your app will be live at a Render-provided URL!

---

## 📄 File Structure

```
tweet-sentiment-analysis/
├── app.py               # Main Flask app
├── templates/
│   └── index.html       # HTML template for UI
├── .env                 # Environment variables (not to be shared)
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation
└── Procfile             # Optional (for deployment platforms like Heroku/Render)
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

**Chirag Joshi** – [@Chirag-joshi123](https://github.com/Chirag-joshi123)
Feel free to fork, contribute, or reach out with suggestions!
