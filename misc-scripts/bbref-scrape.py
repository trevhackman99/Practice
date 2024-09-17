import requests
import bs4 as bs
from selenium import webdriver
import time

# URL params
playerID = 'troutmi01'
lastNameLetter = playerID[0]

URL_TEMPLATE = f'https://www.baseball-reference.com/players/{lastNameLetter}/{playerID}.shtml'

def openUrl(url):
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(5)
    parseHtml(driver)

def parseHtml(driver):
    html = driver.page_source
    soup = bs.BeautifulSoup(html, 'html.parser')
    statsTable = soup.find('table', {'id': 'batting_standard'})
    statsTableBody = statsTable.find('tbody')
    rows = statsTableBody.find_all('tr')
    for row in rows:
        print(row.text)

openUrl(URL_TEMPLATE)
