from bs4 import BeautifulSoup
import pprint
import requests

pp = pprint.PrettyPrinter(indent=4)
# response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
# movies_web_page = response.text
with open("file.txt", "r") as response:
    movies_web_page = response.read()


soup = BeautifulSoup(movies_web_page, "html.parser")
movies_data = soup.find_all(class_="listicle-item")
movie_titles = [movie.findNext(name="img", alt=True, class_="jsx-952983560 loading")["alt"] for movie in movies_data]
movie_titles = movie_titles[::-1] # ordered from top to buttom
pp.pprint(movie_titles)