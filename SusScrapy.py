from bs4 import  BeautifulSoup
import requests

root = 'https://subslikescript.com'
website = f'{root}/movies'
result = requests.get(website).text
soup = BeautifulSoup(result, 'html.parser')

box = soup.find('article', class_='main-article')
links = []
for link in box.find_all('a', href=True):
    links.append(link['href'])

for link in links:
    try:
        websites = f'{root}/{link}'
        results = requests.get(websites).text
        soups = BeautifulSoup(results, 'html.parser')
        box = soups.find('article', class_='main-article')
        title = box.find('h1').get_text()
        transcript = box.find('p', class_='plot').get_text()
        with open(f'{title}.txt', 'w') as file:
            file.write(transcript)
    except:
        pass
