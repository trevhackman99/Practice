import json

formattedData = []

formattedJSON = 'formattedData.json'

desiredKeys = [
    "name",
    "version",
    "set",
    "collector_number",
    "rarity",
    "prices"

    
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
        elif key == "prices":
            
            formattedCard["normal"] = card[key]['usd']

            if formattedCard['normal'] == None:
                formattedCard["normal"] = 0;

            formattedCard["foil"] = card[key]['usd_foil']

            if formattedCard['foil'] == None:
                formattedCard["foil"] = 0;
 
        else:

            formattedCard[key] = card.get(key, "N/A").replace("\u2019", "'").replace("\u0101", "a")

    formattedData.append(formattedCard)

with open(formattedJSON, 'w') as f:
    json.dump(formattedData, f, indent=2)

print("Success!")



        
