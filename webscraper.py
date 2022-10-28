import requests
from bs4 import BeautifulSoup
from operator import itemgetter

URL = "https://news.ycombinator.com"

class Webscraper:

    def scrape_website():
        try:
            response = requests.get(url=URL)
            response.raise_for_status()
        except requests.HTTPError as e:
            print(e)
        else:
            return response.text

    def get_top_ten(markup):
        soup = BeautifulSoup(markup, "html.parser")

        tags = [ tag.a for tag in soup.find_all(class_="titleline") ]
        titles = [ tag.getText() for tag in tags ]
        links = [ tag["href"] for tag in tags ]

        scores = [ int(score.getText().split()[0]) for score in soup.find_all(class_="score") ]

        articles = []
        for i in range(len(titles)):
            articles.append(
                {
                    "score": scores[i],
                    "title": titles[i],
                    "link": links[i]
                }
            )

        sorted_articles = sorted(articles, key=itemgetter('score'), reverse=True)
        top_ten = sorted_articles[:10]

        return top_ten