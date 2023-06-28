from bs4 import  BeautifulSoup
import requests

root = 'https://subslikescript.com'
website = f'{root}/movies'
result = requests.get(website).text
soup = BeautifulSoup(result, 'html.parser')
pagination = soup.find('ul', class_='pagination')
pages = pagination.find_all('li',class_='page-item')
last_page = pages[-2].text

links = []
for page in range(1, int(last_page)+1)[:2]:
    result = requests.get(f'{website}?page={page}').text
    soup = BeautifulSoup(result, 'html.parser')

    box = soup.find('article', class_='main-article')

    for link in box.find_all('a', href=True):
        links.append(link['href'])

    for link in links:
        try:
            print(link)
            results = requests.get(f'{root}/{link}').text
            soups = BeautifulSoup(results, 'html.parser')
            box = soups.find('article', class_='main-article')
            title = box.find('h1').get_text()
            transcript = box.find('p', class_='plot').get_text()
            with open(f'{title}.txt', 'w') as file:
                file.write(transcript)
        except:
            print('**********linj not work************')
            print(link)
            
