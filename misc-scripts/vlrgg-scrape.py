from selenium import webdriver
import bs4 as bs
import requests as req
import time

# URL params

eventGroupID = 'all'
eventID = 2097 # Valorant Champions 2024
seriesID = 'all'
region = 'na'
minRounds = 200
minRating = 1550
agent = 'all'
mapID = 'all'
timespan = '90d'

url = f'https://www.vlr.gg/stats/?event_group_id={eventGroupID}&event_id={eventID}&series_id={seriesID}&region={region}&min_rounds={minRounds}&min_rating={minRating}&agent={agent}&map_id={mapID}&timespan={timespan}'




def openUrl(url):
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(5)
    parseHtml(driver)

def parseHtml(driver):
    html = driver.page_source
    soup = bs.BeautifulSoup(html, 'html.parser')
    statsTable = soup.find('table', {'class': 'wf-table mod-stats mod-scroll'})
    print(statsTable)

openUrl(url)




