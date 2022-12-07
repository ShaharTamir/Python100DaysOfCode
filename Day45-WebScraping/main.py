from bs4 import BeautifulSoup
import pprint
import requests


def points_value(title_dict: dict):
    values = list(title_dict.values())
    return values[0]


pp = pprint.PrettyPrinter()

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
titles = [titlespan.next for titlespan in soup.find_all(name="span", class_="titleline")]
points = [int(point.text.split()[0]) for point in soup.find_all(name="span", class_="score")]

data = [{titles[i].text: [points[i], titles[i].get("href")]} for i in range(len(titles))]
data.sort(key=points_value, reverse=True)

pp.pprint(data)


# with open("website.html", "r") as web_file:
#     contents = web_file.read()

# print(contents)
# soup = BeautifulSoup(contents, "html.parser")
# print(soup.prettify())
# print(soup.title.string)

# print([tag.text for tag in soup.find_all(name="li")])
# print([tag.get("href") for tag in soup.find_all(name="a")])
