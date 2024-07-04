import json
import numpy as np

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

with open('dataCombined.json', 'r') as f:
    data = json.load(f)
    allKeys = data[0].keys()



for card in data:
    formattedCard = {}
    for key in desiredKeys:

        # Takes "name" value from "set" key and assigns it to "set" key of the new formattedCard dictionary
        if key == "set":

            formattedCard[key] = card[key]['name']
        elif key == "prices":
            
            formattedCard["normal"] = card[key]['usd']

            if formattedCard["rarity"] == "Enchanted":
                formattedCard["normal"] = 0

            elif formattedCard['normal'] == None or formattedCard['normal'] < .24:
                formattedCard["normal"] = .24


            formattedCard["foil"] = card[key]['usd_foil']

            if formattedCard['foil'] == None or formattedCard['foil'] < .24:
                formattedCard["foil"] = .99
 
        else:

            formattedCard[key] = card.get(key, "N/A").replace("\u2019", "'").replace("\u0101", "a").replace("N/A", "")

    formattedData.append(formattedCard)



index = {
    "common": {
        "count": 0,
        "normal_price_list": {
            "prices": [],
            "std_dev": {
                "first": 0,
                "second": 0,
                "third": 0
            },
            "avg": 0,
            "max": 0,
            "min": 0
        },
        
        "foil_price_list": {
            "prices": [],
            "std_dev": {
                "first": 0,
                "second": 0,
                "third": 0
            },
            "avg": 0,
            "max": 0,
            "min": 0
        }
    },

    "uncommon": {
        "count": 0,
        "normal_price_list": {
            "prices": [],
            "std_dev": {
                "first": 0,
                "second": 0,
                "third": 0
            },
            "avg": 0,
            "max": 0,
            "min": 0
        },
        
        "foil_price_list": {
            "prices": [],
            "std_dev": {
                "first": 0,
                "second": 0,
                "third": 0
            },
            "avg": 0,
            "max": 0,
            "min": 0
        }
    },
    "rare": {
        "count": 0,
        "normal_price_list": {
            "prices": [],
            "std_dev": {
                "first": 0,
                "second": 0,
                "third": 0
            },
            "avg": 0,
            "max": 0,
            "min": 0
        },
        
        "foil_price_list": {
            "prices": [],
            "std_dev": {
                "first": 0,
                "second": 0,
                "third": 0
            },
            "avg": 0,
            "max": 0,
            "min": 0
        }

    },
    "super_rare": {
        "count": 0,
        "normal_price_list": {
            "prices": [],
            "std_dev": {
                "first": 0,
                "second": 0,
                "third": 0
            },
            "avg": 0,
            "max": 0,
            "min": 0
        },
        
        "foil_price_list": {
            "prices": [],
            "std_dev": {
                "first": 0,
                "second": 0,
                "third": 0
            },
            "avg": 0,
            "max": 0,
            "min": 0
        }
    },
    "legendary": {
        "count": 0,
        "normal_price_list": {
            "prices": [],
            "std_dev": {
                "first": 0,
                "second": 0,
                "third": 0
            },
            "avg": 0,
            "max": 0,
            "min": 0
        },
        
        "foil_price_list": {
            "prices": [],
            "std_dev": {
                "first": 0,
                "second": 0,
                "third": 0
            },
            "avg": 0,
            "max": 0,
            "min": 0
        }
    
    },
    "enchanted": {
        "count": 0,
        "foil_price_list": {
            "prices": [],
            "std_dev": {
                "first": 0,
                "second": 0,
                "third": 0
            },
            "avg": 0,
            "max": 0,
            "min": 0
        }
    }
}


for card in formattedData:

    if card["rarity"] == "Common":
        index["common"]["count"] += 1
        index["common"]["normal_price_list"]["prices"].append(card["normal"])
        index["common"]["foil_price_list"]["prices"].append(card["foil"])
        index["common"]["normal_price_list"]["avg"] = np.average(index["common"]["normal_price_list"]['prices'])
        index["common"]["foil_price_list"]["avg"] = np.average(index["common"]["foil_price_list"]['prices'])
        index["common"]["normal_price_list"]["std_dev"]["first"] = np.std(index["common"]["normal_price_list"]['prices'])
        index["common"]["foil_price_list"]["std_dev"]["first"] = np.std(index["common"]["foil_price_list"]['prices'])
        index["common"]["normal_price_list"]["std_dev"]["second"] = np.std(index["common"]["normal_price_list"]['prices']) * 2
        index["common"]["foil_price_list"]["std_dev"]["second"] = np.std(index["common"]["foil_price_list"]['prices']) * 2
        index["common"]["normal_price_list"]["std_dev"]["third"] = np.std(index["common"]["normal_price_list"]['prices']) * 3
        index["common"]["foil_price_list"]["std_dev"]["third"] = np.std(index["common"]["foil_price_list"]['prices']) * 3
        index["common"]["normal_price_list"]["max"] = np.max(index["common"]["normal_price_list"]['prices'])
        index["common"]["foil_price_list"]["max"] = np.max(index["common"]["foil_price_list"]['prices'])
        index["common"]["normal_price_list"]["min"] = np.min(index["common"]["normal_price_list"]['prices'])
        index["common"]["foil_price_list"]["min"] = np.min(index["common"]["foil_price_list"]['prices'])


    

    elif card["rarity"] == "Uncommon":
        index["uncommon"]["count"] += 1
        index["uncommon"]["normal_price_list"]["prices"].append(card["normal"])
        index["uncommon"]["foil_price_list"]["prices"].append(card["foil"])
        index["uncommon"]["normal_price_list"]["avg"] = np.average(index["uncommon"]["normal_price_list"]['prices'])
        index["uncommon"]["foil_price_list"]["avg"] = np.average(index["uncommon"]["foil_price_list"]['prices'])
        index["uncommon"]["normal_price_list"]["std_dev"]["first"] = np.std(index["uncommon"]["normal_price_list"]['prices'])
        index["uncommon"]["foil_price_list"]["std_dev"]["first"] = np.std(index["uncommon"]["foil_price_list"]['prices'])
        index["uncommon"]["normal_price_list"]["std_dev"]["second"] = np.std(index["uncommon"]["normal_price_list"]['prices']) * 2
        index["uncommon"]["foil_price_list"]["std_dev"]["second"] = np.std(index["uncommon"]["foil_price_list"]['prices']) * 2
        index["uncommon"]["normal_price_list"]["std_dev"]["third"] = np.std(index["uncommon"]["normal_price_list"]['prices']) * 3
        index["uncommon"]["foil_price_list"]["std_dev"]["third"] = np.std(index["uncommon"]["foil_price_list"]['prices']) * 3
        index["uncommon"]["normal_price_list"]["max"] = np.max(index["uncommon"]["normal_price_list"]['prices'])
        index["uncommon"]["foil_price_list"]["max"] = np.max(index["uncommon"]["foil_price_list"]['prices'])
        index["uncommon"]["normal_price_list"]["min"] = np.min(index["uncommon"]["normal_price_list"]['prices'])
        index["uncommon"]["foil_price_list"]["min"] = np.min(index["uncommon"]["foil_price_list"]['prices'])



    elif card["rarity"] == "Rare":
        index["rare"]["count"] += 1
        index["rare"]["normal_price_list"]["prices"].append(card["normal"])
        index["rare"]["foil_price_list"]["prices"].append(card["foil"])
        index["rare"]["normal_price_list"]["avg"] = np.average(index["rare"]["normal_price_list"]['prices'])
        index["rare"]["foil_price_list"]["avg"] = np.average(index["rare"]["foil_price_list"]['prices'])
        index["rare"]["normal_price_list"]["std_dev"]["first"] = np.std(index["rare"]["normal_price_list"]['prices'])
        index["rare"]["foil_price_list"]["std_dev"]["first"] = np.std(index["rare"]["foil_price_list"]['prices'])
        index["rare"]["normal_price_list"]["std_dev"]["second"] = np.std(index["rare"]["normal_price_list"]['prices']) * 2
        index["rare"]["foil_price_list"]["std_dev"]["second"] = np.std(index["rare"]["foil_price_list"]['prices']) * 2
        index["rare"]["normal_price_list"]["std_dev"]["third"] = np.std(index["rare"]["normal_price_list"]['prices']) * 3
        index["rare"]["foil_price_list"]["std_dev"]["third"] = np.std(index["rare"]["foil_price_list"]['prices']) * 3
        index["rare"]["normal_price_list"]["max"] = np.max(index["rare"]["normal_price_list"]['prices'])
        index["rare"]["foil_price_list"]["max"] = np.max(index["rare"]["foil_price_list"]['prices'])
        index["rare"]["normal_price_list"]["min"] = np.min(index["rare"]["normal_price_list"]['prices'])
        index["rare"]["foil_price_list"]["min"] = np.min(index["rare"]["foil_price_list"]['prices'])


    elif card["rarity"] == "Super_rare":
        index["super_rare"]["count"] += 1
        index["super_rare"]["normal_price_list"]["prices"].append(card["normal"])
        index["super_rare"]["foil_price_list"]["prices"].append(card["foil"])
        index["super_rare"]["normal_price_list"]["avg"] = np.average(index["super_rare"]["normal_price_list"]['prices'])
        index["super_rare"]["foil_price_list"]["avg"] = np.average(index["super_rare"]["foil_price_list"]['prices'])
        index["super_rare"]["normal_price_list"]["std_dev"]["first"] = np.std(index["super_rare"]["normal_price_list"]['prices'])
        index["super_rare"]["foil_price_list"]["std_dev"]["first"] = np.std(index["super_rare"]["foil_price_list"]['prices'])
        index["super_rare"]["normal_price_list"]["std_dev"]["second"] = np.std(index["super_rare"]["normal_price_list"]['prices']) * 2
        index["super_rare"]["foil_price_list"]["std_dev"]["second"] = np.std(index["super_rare"]["foil_price_list"]['prices']) * 2
        index["super_rare"]["normal_price_list"]["std_dev"]["third"] = np.std(index["super_rare"]["normal_price_list"]['prices']) * 3
        index["super_rare"]["foil_price_list"]["std_dev"]["third"] = np.std(index["super_rare"]["foil_price_list"]['prices']) * 3
        index["super_rare"]["normal_price_list"]["max"] = np.max(index["super_rare"]["normal_price_list"]['prices'])
        index["super_rare"]["foil_price_list"]["max"] = np.max(index["super_rare"]["foil_price_list"]['prices'])
        index["super_rare"]["normal_price_list"]["min"] = np.min(index["super_rare"]["normal_price_list"]['prices'])
        index["super_rare"]["foil_price_list"]["min"] = np.min(index["super_rare"]["foil_price_list"]['prices'])


    elif card["rarity"] == "Legendary":
        index["legendary"]["count"] += 1
        index["legendary"]["normal_price_list"]["prices"].append(card["normal"])
        index["legendary"]["foil_price_list"]["prices"].append(card["foil"])
        index["legendary"]["normal_price_list"]["avg"] = np.average(index["legendary"]["normal_price_list"]['prices'])
        index["legendary"]["foil_price_list"]["avg"] = np.average(index["legendary"]["foil_price_list"]['prices'])
        index["legendary"]["normal_price_list"]["std_dev"]["first"] = np.std(index["legendary"]["normal_price_list"]['prices'])
        index["legendary"]["foil_price_list"]["std_dev"]["first"] = np.std(index["legendary"]["foil_price_list"]['prices'])
        index["legendary"]["normal_price_list"]["std_dev"]["second"] = np.std(index["legendary"]["normal_price_list"]['prices']) * 2
        index["legendary"]["foil_price_list"]["std_dev"]["second"] = np.std(index["legendary"]["foil_price_list"]['prices']) * 2
        index["legendary"]["normal_price_list"]["std_dev"]["third"] = np.std(index["legendary"]["normal_price_list"]['prices']) * 3
        index["legendary"]["foil_price_list"]["std_dev"]["third"] = np.std(index["legendary"]["foil_price_list"]['prices']) * 3
        index["legendary"]["normal_price_list"]["max"] = np.max(index["legendary"]["normal_price_list"]['prices'])
        index["legendary"]["foil_price_list"]["max"] = np.max(index["legendary"]["foil_price_list"]['prices'])
        index["legendary"]["normal_price_list"]["min"] = np.min(index["legendary"]["normal_price_list"]['prices'])
        index["legendary"]["foil_price_list"]["min"] = np.min(index["legendary"]["foil_price_list"]['prices'])



    elif card["rarity"] == "Enchanted":
        index["enchanted"]["count"] += 1
        index["enchanted"]["foil_price_list"]["prices"].append(card["foil"])
        index["enchanted"]["foil_price_list"]["avg"] = np.average(index["enchanted"]["foil_price_list"]['prices'])
        index["enchanted"]["foil_price_list"]["std_dev"]["first"] = np.std(index["enchanted"]["foil_price_list"]['prices'])
        index["enchanted"]["foil_price_list"]["std_dev"]["second"] = np.std(index["enchanted"]["foil_price_list"]['prices']) * 2
        index["enchanted"]["foil_price_list"]["std_dev"]["third"] = np.std(index["enchanted"]["foil_price_list"]['prices']) * 3
        index["enchanted"]["foil_price_list"]["max"] = max(index["enchanted"]["foil_price_list"]['prices'])
        index["enchanted"]["foil_price_list"]["min"] = min(index["enchanted"]["foil_price_list"]['prices'])

with open(formattedJSON, 'w') as f:
    json.dump(formattedData, f, indent=2)

with open("priceIndex.json", 'w') as f:
    json.dump(index, f, indent=2)

print("Success!")



        
