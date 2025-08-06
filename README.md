## 🏴‍☠️ One Piece Bot

This bot checks for **new One Piece episodes** and **new manga chapters**, and if it finds something new, it **sends you an email**!

## 🔍 What It Does

- 📺 Checks anime: [aniwatchtv.to](https://aniwatchtv.to/one-piece-100?ref=search)
- 📖 Checks manga: [viz.com](https://www.viz.com/shonenjump/chapters/one-piece)
- 💾 Remembers the last episode/chapter it saw
- 📬 Sends an email if a new one comes out
- ☁️ Stays online 24/7 using **Render + UptimeRobot**

## 🧠 How It Works (Simple Steps)

### ✅ Step 1: Web Scraping
Use Python with `requests` and `BeautifulSoup` to look at the websites and find the latest episode/chapter.

### ✅ Step 2: Send Email
Use **Gmail + Python** to send an email when something new comes out.  
> Use a **Gmail App Password** (not your main Gmail password).

### ✅ Step 3: Schedule Checks
Use `while True` + `time.sleep()` to run the check every 5 minutes.  
Use Python’s `datetime` module to check what day it is (runs more often on weekends and Mondays).

### ✅ Step 4: Tiny Web Server
Use **Flask** to create a small web server.  
This keeps the bot "alive" on Render (free web hosting).

### ✅ Step 5: Deploy on Render
1. Upload your code to **GitHub**
2. Connect it to [Render.com](https://render.com/)
3. Render runs your bot 24/7 in the cloud

### ✅ Step 6: Keep Bot Awake
Use [UptimeRobot](https://uptimerobot.com/) to ping your Flask app every 5 minutes  
so Render doesn't put it to sleep.

---

Made with ❤️ for One Piece fans.