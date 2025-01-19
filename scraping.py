import requests
from bs4 import BeautifulSoup
import pprint


res = requests.get('https://www.dailymail.co.uk/home/index.html')

soupObj = BeautifulSoup(res.text, 'html.parser')
#print(soupObj)

leftColumn = soupObj.select('.alpha')
rightColumn = soupObj.select('.beta')
print(leftColumn)
links = soupObj.select('.linkro-darkred') 
text = soupObj.select('.articletext') 

#print(links) # this is a list []
#
print(text)


def get(links, text):
    results = []
    for inx, item in enumerate(links):
        title = item.getText() 
        href = item.get('href', None)
        
        for  item in text:
            text = item.get('p', None)
                                
    results.append({'title': title, 'link': href, 'text': text})

    return results 

pprint.pprint(get(links, text))