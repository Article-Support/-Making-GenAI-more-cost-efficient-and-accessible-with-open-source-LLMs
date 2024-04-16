import re
from time import sleep
from bs4 import BeautifulSoup
import requests
import re 
from newspaper import Article

headers = {
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q=0.9",
    "referer": "https://www.google.com",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36 Edg/85.0.564.44",
}


def remove_tags(text):
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)


def get_article(card):
    """Extract article information from the raw html"""
    headline = card.find("h4", "s-title").text
    source = card.find("span", "s-source").text
    posted = card.find("span", "s-time").text.replace("·", "").strip()
    description = card.find("p", "s-desc").text.strip()
    raw_link = card.find("a").get("href")
    unquoted_link = requests.utils.unquote(raw_link)
    pattern = re.compile(r"RU=(.+)\/RK")
    clean_link = re.search(pattern, unquoted_link).group(1)

    article = (headline, source, posted, description, clean_link)
    return article


def get_the_news(search):
    """Run the main program"""
    template = "https://news.search.yahoo.com/search?p={}"
    url = template.format(search)
    articles = []
    links = set()

    counter = 0

    while True:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        cards = soup.find_all("div", "NewsArticle")

        # extract articles from page
        for card in cards:
            article = get_article(card)
            link = article[-1]
            if not link in links:
                counter += 1

                try:
                    news_article = Article(link, language="en")  # en for English
                    news_article.download()
                    news_article.parse()
                    
                    with open('files/' + str(counter) + '.html', 'wb') as out_file:
                        out_file.write(news_article.text.encode('utf-8'))

                    print("Downloaded article " + str(article[0]) + " from " + link)
                    links.add(link)
                    articles.append(article)
                except Exception as e:
                    print(e)
                    continue    



        # find the next page
        try:
            url = soup.find("a", "next").get("href")
            sleep(1)
        except AttributeError:
            break
    return articles


articles = get_the_news("nvda")
