import requests
from bs4 import BeautifulSoup
import pprint


res = requests.get('https://www.dailymail.co.uk/home/index.html')

soupObj = BeautifulSoup(res.text, 'html.parser')
print(soupObj)

links = soupObj.select('.linkro-darkred') 
#text = soupObj.select('.articletext') 

print(links)


def get(links,):
    results = []
    for inx, item in enumerate(links):
        title = item.getText() 
        href = item.get('href', None)
        results.append({'title': title, 'link': href})

    return results 

pprint.pprint(get(links))