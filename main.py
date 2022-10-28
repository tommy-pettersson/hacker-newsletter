from webscraper import Webscraper
from mailman import Mailman

def main():
    markup = Webscraper.scrape_website()
    top_ten_articles = Webscraper.get_top_ten(markup=markup)
    Mailman.send_mail(top_ten_articles)

if __name__ == "__main__":
    main()