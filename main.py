import requests
from bs4 import BeautifulSoup as BS

anime_URL = "https://aniwatchtv.to/one-piece-100?ref=search"
manga_URL = "https://www.viz.com/shonenjump/chapters/one-piece"

anime_page = requests.get(anime_URL)
manga_page = requests.get(manga_URL)

# print(anime_page.text)
# print(manga_page.text, "\n")

anime_soup = BS(anime_page.content, "html.parser")
manga_soup = BS(manga_page.content, "html.parser")

# Finding the Subbed Episode Number for One Piece Anime
anime_results = anime_soup.find("a", title="One Piece")
film_detail = anime_results.find_parent("div", class_="film-detail")
fd_info = film_detail.find("div", class_="fd-infor")
sub_ep_num = fd_info.find("div", class_="tick-sub").text.strip()

# Finding the Chapter Number for One Piece Manga
manga_results = manga_soup.find("div", id="chpt_rows")
future_div = manga_results.find("div", class_="section_future_chapter")
latest_chapter_div = future_div.find_next_sibling("div")
def is_chapter_text(text):
    return text and "Ch." in text
chapter_num_str = latest_chapter_div.find("div", string=is_chapter_text).text.strip()
chapter_num = chapter_num_str[4:]

