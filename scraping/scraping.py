import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news')

soup = BeautifulSoup(res.text, 'html.parser')


# grap link and votes
links = soup.select('.titleline') #heads up! .storylink changed to .titleline
sub_text = soup.select('.subtext')


# for link in soup.find_all('a'):
#     print(link.get('href',None))

def create_custome_hacker_news(links, sub_text):
    hn = []

    for idx, item in enumerate(links):
        # title = item.getText()
        # href = item.get('href', None)
        # vote = subtext[idx].select('.score')

        title = item.getText
        href = item.get('href', None)
        vote = sub_text[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            hn.append({'title': title, 'link': href, 'votes': points})
    return hn


pprint.pprint(create_custome_hacker_news(links, sub_text))
