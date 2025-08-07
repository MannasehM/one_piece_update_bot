import requests
from bs4 import BeautifulSoup as BS
import time
from datetime import datetime
import yagmail
import os
from dotenv import load_dotenv
from flask import Flask
import threading

# Load environment variables from .env
load_dotenv()

EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")
ANIME_URL = os.getenv("ANIME_URL")
MANGA_URL = os.getenv("MANGA_URL")

# Set up Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "One Piece Bot is running!"

# Email client
yag = yagmail.SMTP(EMAIL_USER, EMAIL_PASS)

# ---Scraper Helpers---

# Finding the Subbed Episode Number for One Piece Anime Soup Object
def get_episode_anime_soup(anime_soup):
    anime_results = anime_soup.find("a", title="One Piece")
    film_detail = anime_results.find_parent("div", class_="film-detail")
    fd_info = film_detail.find("div", class_="fd-infor")
    sub_ep_num = int(fd_info.find("div", class_="tick-sub").text.strip())

    return sub_ep_num

# Finding the Chapter Number for One Piece Manga Soup Object
def get_chapter_manga_soup(manga_soup):
    manga_results = manga_soup.find("div", id="chpt_rows")
    future_div = manga_results.find("div", class_="section_future_chapter")
    latest_chapter_div = future_div.find_next_sibling("div")
    def is_chapter_text(text):
        return text and "Ch." in text
    chapter_num_str = latest_chapter_div.find("div", string=is_chapter_text).text.strip()
    chapter_num = int(chapter_num_str[4:])

    return chapter_num

# ---Bot Logic---
def run_bot():
    # Initial Fetch
    last_anime_page = requests.get(ANIME_URL)
    last_manga_page = requests.get(MANGA_URL)

    last_anime_soup = BS(last_anime_page.content, "html.parser")
    last_manga_soup = BS(last_manga_page.content, "html.parser")

    #last_anime_episode = get_episode_anime_soup(last_anime_soup)
    last_anime_episode = 1137
    last_manga_chapter = get_chapter_manga_soup(last_manga_soup)

    print("Bot started. Last known episode:", last_anime_episode)
    print("Last known chapter:", last_manga_chapter)

    while True: 
        try:
            this_anime_page = requests.get(ANIME_URL)
            this_manga_page = requests.get(MANGA_URL)

            this_anime_soup = BS(this_anime_page.content, "html.parser")
            this_manga_soup = BS(this_manga_page.content, "html.parser")

            this_anime_episode = get_episode_anime_soup(this_anime_soup)
            this_manga_chapter = get_chapter_manga_soup(this_manga_soup)

            if this_anime_episode != last_anime_episode: 
                # Send email about new episode
                yag.send(
                    to=EMAIL_USER,
                    subject="New One Piece Episode! Episode " + str(this_anime_episode),
                    contents="empty body",
                )
                print("New One Piece Episode! Episode " + str(this_anime_episode))
                last_anime_episode = this_anime_episode

            if this_manga_chapter != last_manga_chapter: 
                # Send email about new chapter
                yag.send(
                    to=EMAIL_USER,
                    subject="New One Piece Chapter! Chapter " + str(this_manga_chapter),
                    contents="empty body",
                )
                print("New One Piece Chapter! Chapter " + str(this_manga_chapter))
                last_manga_chapter = this_manga_chapter
        except Exception as e:
            print("Error during check:", str(e))
        
        # how often to run
        current_weekday = datetime.now().weekday() # 0 = Monday, 1 = Tuesday, ... , 6 = Sunday
        if current_weekday == 6 or current_weekday == 0:
            time.sleep(5 * 60) # every 5 minutes
        else:
            time.sleep(10 * 60) # every 10 minutes
    
# ---Start Flask and Bot Together---
if __name__ == "__main__":
    bot_thread = threading.Thread(target=run_bot)
    bot_thread.daemon = True
    bot_thread.start()

    app.run(host="0.0.0.0", port=5000)