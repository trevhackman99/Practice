import requests
import time
import json

sets = [1, 2, 3, 4, 5]

def fetchLorcanaAPI():
    for s in sets:
        url = "https://api.lorcast.com"
        response = requests.get(url)
        if response.status_code != 200:
            print("Error: ", response.status_code)
        else:

            time.sleep(5)
            
            query = url + f"/v0/cards/search?q=set:{s}"
            response = requests.get(query)
            data = response.json()['results']

            
            

            query = url + f"/v0/cards/search?q=set:{s}+rarity:enchanted"
            response = requests.get(query)
            dataEnchanted = response.json()['results']
            
            with open(f'dataCombined{s}.json', 'w') as f:
                json.dump(data + dataEnchanted, f, indent=4)

            print("Success!")


fetchLorcanaAPI()