from selenium import webdriver
import time
from bs4 import BeautifulSoup



driver = webdriver.Chrome()
driver.get('https://www.dailymail.co.uk/home/index.html')

time.sleep(3)
soup = BeautifulSoup(driver.page_source, 'lxml')
print('test')
articles = soup.find_all('div', class_ ='article')
print(articles)
for index, article in enumerate(articles):
   title = article.find('h2', class_ ='linkro-darkred').text
   print(title)

   with open(f'C:/Users/Emily/Desktop/projects/scrapingdailymail/{index}.txt', 'w') as f:
        f.write(f"Title: {title}")

        print(f'File saved: {index}')

       

driver.quit()