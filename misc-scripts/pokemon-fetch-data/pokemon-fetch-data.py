import pandas as pd
import json
import requests

tcgSET = "sv6"
url = "https://api.pokemontcg.io/v2/cards?q=set.id:" + tcgSET
TOKEN = ""


# FETCH POKEMON TCG DATA

def fetch_data(url):
    response = requests.get(url, headers={"X-Api-Key": TOKEN})
    data = response.json()
    
    # data is an object with a key called "data" that contains the actual data
    # other keys are "page", "pageSize", "count", "totalCount"
    data = data["data"]

    convertto_to_file(data)

def convertto_to_file(data):
    with open('pokemon-tcg-data.json', 'w') as f:
        json.dump(data, f, indent=4)
        print("Data saved to file")



def parseJSON():
    with open('pokemon-tcg-data.json', 'r') as f:
        data = json.load(f)
        data = data["data"]
        
        
        for dict in data:
            for key in dict.keys():
                print(key)
                        



parseJSON()