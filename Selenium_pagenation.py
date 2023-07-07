from selenium import webdriver
import  pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)
website = 'https://www.audible.com/search'
driver = webdriver.Chrome(options=options)
driver.get(website)

pagenation = driver.find_element(By.XPATH, '//*[@id="pagination-a11y-skiplink-target"]/div/div[2]/div/span/ul')
pages = pagenation.find_elements(By.TAG_NAME, 'li')
last_page = int(pages[-2].text)


book_title = []
book_author = []
book_length = []

curent_page = 1
while curent_page <= last_page:
   time.sleep(2)
   container = driver.find_element(By.XPATH, '//*[@id="center-3"]/div/div')
   products = container.find_elements(By.XPATH, './/*[@id="product-list-a11y-skiplink-target"]/span/ul/li' )
   for product in products:
      book_title.append(product.find_element(By.XPATH, './/h3[contains(@class, "bc-heading")]').text)
      book_author.append(product.find_element(By.XPATH, './/li[contains(@class, "authorLabel")]').text)
      book_length.append(product.find_element(By.XPATH, './/li[contains(@class, "runtimeLabel")]').text)

   curent_page = curent_page + 1
   try:
      next_page = driver.find_element(By.XPATH, '//*[@id="pagination-a11y-skiplink-target"]/div/div[2]/div/span/ul/li[6]/span/a')
      next_page.click()
   except:
      pass

driver.quit()

df_book = pd.DataFrame({'title': book_title, 'athour': book_author, 'length': book_length})
df_book.to_csv('books.csv', index=False )
