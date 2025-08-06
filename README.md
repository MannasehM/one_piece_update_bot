🏴‍☠️ One Piece Bot
This bot checks for new One Piece episodes and new manga chapters, and if it finds something new, it sends you an email!

🔍 What It Does
Looks at these websites:

Anime: aniwatchtv.to

Manga: viz.com

Remembers the last episode/chapter it saw.

Sends an email if a new one comes out.

Stays online 24/7 using Render + UptimeRobot.

🧠 How It Works (Simple Steps)
✅ Step 1: Web Scraping
Use Python with requests and BeautifulSoup to look at the websites and find the latest episode/chapter.

✅ Step 2: Send Email
Use Gmail + Python to send an email when something new comes out. Use an App Password (not your main password).

✅ Step 3: Schedule Checks
Use while True + time.sleep() to run the check every 5 minutes. Use Python’s date/time to check what day it is.

✅ Step 4: Tiny Web Server
Use Flask to create a small web server. This keeps the bot alive on Render.

✅ Step 5: Deploy on Render
Upload your code to GitHub, then connect it to Render.com. This runs your bot in the cloud.

✅ Step 6: Keep Bot Awake
Use UptimeRobot to ping your bot every 5 minutes so it doesn't fall asleep.

