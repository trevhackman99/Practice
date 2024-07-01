import json

formattedData = []

formattedJSON = 'formattedData.json'

desiredKeys = [
    "name",
    "version",
    "set",
    "collector_number",
    "rarity"

    
]

with open('data.json', 'r') as f:
    data = json.load(f)
    allKeys = data[0].keys()
    print(allKeys)



for card in data:
    formattedCard = {}
    for key in desiredKeys:

        if key == "set":

            formattedCard[key] = card[key]['name']

        else:

            formattedCard[key] = card.get(key, "N/A")

    formattedData.append(formattedCard)

with open(formattedJSON, 'w') as f:
    json.dump(formattedData, f, indent=2)

print("Success!")



        
