import requests
import time

def fetchLorcanaAPI():
    url = "https://api.lorcast.com"
    response = requests.get(url)
    if response.status_code != 200:
        print("Error: ", response.status_code)
    else:

        time.sleep(.5)
        
        query = url + "/v0/cards/search?q=elsa+set:1"
        response = requests.get(query)
        data = response.json()['results']['name']

        print(data)


fetchLorcanaAPI()