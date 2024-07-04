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

            if formattedCard['normal'] == None or formattedCard['normal'] < .24 and \
            formattedCard["rarity"] != "Enchanted":
                
                formattedCard["normal"] = .24

            elif formattedCard['rarity'] == "Enchanted":
                formattedCard["normal"] = 0

            formattedCard["foil"] = card[key]['usd_foil']

            if formattedCard['foil'] == None or formattedCard['foil'] < .24:
                formattedCard["foil"] = .99
 
        else:

            formattedCard[key] = card.get(key, "N/A").replace("\u2019", "'").replace("\u0101", "a").replace("N/A", "")

    formattedData.append(formattedCard)



commonIndex = {
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
}

uncommonIndex = {
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
}
rareIndex = {
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
}
superRareIndex = {
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
}
legendaryIndex = {
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
   
}
enchantedIndex = {
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

for card in formattedData:

    if card["rarity"] == "Common":
        commonIndex["count"] += 1
        commonIndex["normal_price_list"]["prices"].append(card["normal"])
        commonIndex["foil_price_list"]["prices"].append(card["foil"])
        commonIndex["normal_price_list"]["avg"] = np.average(commonIndex["normal_price_list"]['prices'])
        commonIndex["foil_price_list"]["avg"] = np.average(commonIndex["foil_price_list"]['prices'])
        commonIndex["normal_price_list"]["std_dev"]["first"] = np.std(commonIndex["normal_price_list"]['prices'])
        commonIndex["foil_price_list"]["std_dev"]["first"] = np.std(commonIndex["foil_price_list"]['prices'])
        commonIndex["normal_price_list"]["std_dev"]["second"] = np.std(commonIndex["normal_price_list"]['prices'] * 2)
        commonIndex["foil_price_list"]["std_dev"]["second"] = np.std(commonIndex["foil_price_list"]['prices'] * 2)
        commonIndex["normal_price_list"]["std_dev"]["third"] = np.std(commonIndex["normal_price_list"]['prices'] * 3)
        commonIndex["foil_price_list"]["std_dev"]["third"] = np.std(commonIndex["foil_price_list"]['prices'] * 3)
        commonIndex["normal_price_list"]["max"] = np.max(commonIndex["normal_price_list"]['prices'])
        commonIndex["foil_price_list"]["max"] = np.max(commonIndex["foil_price_list"]['prices'])
        commonIndex["normal_price_list"]["min"] = np.min(commonIndex["normal_price_list"]['prices'])
        commonIndex["foil_price_list"]["min"] = np.min(commonIndex["foil_price_list"]['prices'])


    

    elif card["rarity"] == "Uncommon":
        uncommonIndex["count"] += 1
        uncommonIndex["normal_price_list"]["prices"].append(card["normal"])
        uncommonIndex["foil_price_list"]["prices"].append(card["foil"])
        uncommonIndex["normal_price_list"]["avg"] = np.average(uncommonIndex["normal_price_list"]['prices'])
        uncommonIndex["foil_price_list"]["avg"] = np.average(uncommonIndex["foil_price_list"]['prices'])
        uncommonIndex["normal_price_list"]["std_dev"]["first"] = np.std(uncommonIndex["normal_price_list"]['prices'])
        uncommonIndex["foil_price_list"]["std_dev"]["first"] = np.std(uncommonIndex["foil_price_list"]['prices'])
        uncommonIndex["normal_price_list"]["std_dev"]["second"] = np.std(uncommonIndex["normal_price_list"]['prices'] * 2)
        uncommonIndex["foil_price_list"]["std_dev"]["second"] = np.std(uncommonIndex["foil_price_list"]['prices'] * 2)
        uncommonIndex["normal_price_list"]["std_dev"]["third"] = np.std(uncommonIndex["normal_price_list"]['prices'] * 3)
        uncommonIndex["foil_price_list"]["std_dev"]["third"] = np.std(uncommonIndex["foil_price_list"]['prices'] * 3)
        uncommonIndex["normal_price_list"]["max"] = np.max(uncommonIndex["normal_price_list"]['prices'])
        uncommonIndex["foil_price_list"]["max"] = np.max(uncommonIndex["foil_price_list"]['prices'])
        uncommonIndex["normal_price_list"]["min"] = np.min(uncommonIndex["normal_price_list"]['prices'])
        uncommonIndex["foil_price_list"]["min"] = np.min(uncommonIndex["foil_price_list"]['prices'])



    elif card["rarity"] == "Rare":
        rareIndex["count"] += 1
        rareIndex["normal_price_list"]["prices"].append(card["normal"])
        rareIndex["foil_price_list"]["prices"].append(card["foil"])
        rareIndex["normal_price_list"]["avg"] = np.average(rareIndex["normal_price_list"]['prices'])
        rareIndex["foil_price_list"]["avg"] = np.average(rareIndex["foil_price_list"]['prices'])
        rareIndex["normal_price_list"]["std_dev"]["first"] = np.std(rareIndex["normal_price_list"]['prices'])
        rareIndex["foil_price_list"]["std_dev"]["first"] = np.std(rareIndex["foil_price_list"]['prices'])
        rareIndex["normal_price_list"]["std_dev"]["second"] = np.std(rareIndex["normal_price_list"]['prices'] * 2)
        rareIndex["foil_price_list"]["std_dev"]["second"] = np.std(rareIndex["foil_price_list"]['prices'] * 2)
        rareIndex["normal_price_list"]["std_dev"]["third"] = np.std(rareIndex["normal_price_list"]['prices'] * 3)
        rareIndex["foil_price_list"]["std_dev"]["third"] = np.std(rareIndex["foil_price_list"]['prices'] * 3)
        rareIndex["normal_price_list"]["max"] = np.max(rareIndex["normal_price_list"]['prices'])
        rareIndex["foil_price_list"]["max"] = np.max(rareIndex["foil_price_list"]['prices'])
        rareIndex["normal_price_list"]["min"] = np.min(rareIndex["normal_price_list"]['prices'])
        rareIndex["foil_price_list"]["min"] = np.min(rareIndex["foil_price_list"]['prices'])


    elif card["rarity"] == "Super_rare":
        superRareIndex["count"] += 1
        superRareIndex["normal_price_list"]["prices"].append(card["normal"])
        superRareIndex["foil_price_list"]["prices"].append(card["foil"])
        superRareIndex["normal_price_list"]["avg"] = np.average(superRareIndex["normal_price_list"]['prices'])
        superRareIndex["foil_price_list"]["avg"] = np.average(superRareIndex["foil_price_list"]['prices'])
        superRareIndex["normal_price_list"]["std_dev"]["first"] = np.std(superRareIndex["normal_price_list"]['prices'])
        superRareIndex["foil_price_list"]["std_dev"]["first"] = np.std(superRareIndex["foil_price_list"]['prices'])
        superRareIndex["normal_price_list"]["std_dev"]["second"] = np.std(superRareIndex["normal_price_list"]['prices'] * 2)
        superRareIndex["foil_price_list"]["std_dev"]["second"] = np.std(superRareIndex["foil_price_list"]['prices'] * 2)
        superRareIndex["normal_price_list"]["std_dev"]["third"] = np.std(superRareIndex["normal_price_list"]['prices'] * 3)
        superRareIndex["foil_price_list"]["std_dev"]["third"] = np.std(superRareIndex["foil_price_list"]['prices'] * 3)
        superRareIndex["normal_price_list"]["max"] = np.max(superRareIndex["normal_price_list"]['prices'])
        superRareIndex["foil_price_list"]["max"] = np.max(superRareIndex["foil_price_list"]['prices'])
        superRareIndex["normal_price_list"]["min"] = np.min(superRareIndex["normal_price_list"]['prices'])
        superRareIndex["foil_price_list"]["min"] = np.min(superRareIndex["foil_price_list"]['prices'])


    elif card["rarity"] == "Legendary":
        legendaryIndex["count"] += 1
        legendaryIndex["normal_price_list"]["prices"].append(card["normal"])
        legendaryIndex["foil_price_list"]["prices"].append(card["foil"])
        legendaryIndex["normal_price_list"]["avg"] = np.average(legendaryIndex["normal_price_list"]['prices'])
        legendaryIndex["foil_price_list"]["avg"] = np.average(legendaryIndex["foil_price_list"]['prices'])
        legendaryIndex["normal_price_list"]["std_dev"]["first"] = np.std(legendaryIndex["normal_price_list"]['prices'])
        legendaryIndex["foil_price_list"]["std_dev"]["first"] = np.std(legendaryIndex["foil_price_list"]['prices'])
        legendaryIndex["normal_price_list"]["std_dev"]["second"] = np.std(legendaryIndex["normal_price_list"]['prices'] * 2)
        legendaryIndex["foil_price_list"]["std_dev"]["second"] = np.std(legendaryIndex["foil_price_list"]['prices'] * 2)
        legendaryIndex["normal_price_list"]["std_dev"]["third"] = np.std(legendaryIndex["normal_price_list"]['prices'] * 3)
        legendaryIndex["foil_price_list"]["std_dev"]["third"] = np.std(legendaryIndex["foil_price_list"]['prices'] * 3)
        legendaryIndex["normal_price_list"]["max"] = np.max(legendaryIndex["normal_price_list"]['prices'])
        legendaryIndex["foil_price_list"]["max"] = np.max(legendaryIndex["foil_price_list"]['prices'])
        legendaryIndex["normal_price_list"]["min"] = np.min(legendaryIndex["normal_price_list"]['prices'])
        legendaryIndex["foil_price_list"]["min"] = np.min(legendaryIndex["foil_price_list"]['prices'])



    elif card["rarity"] == "Enchanted":
        enchantedIndex["count"] += 1
        enchantedIndex["foil_price_list"]["prices"].append(card["foil"])
        enchantedIndex["foil_price_list"]["avg"] = np.average(enchantedIndex["foil_price_list"]['prices'])
        enchantedIndex["foil_price_list"]["std_dev"]["first"] = np.std(enchantedIndex["foil_price_list"]['prices'])
        enchantedIndex["foil_price_list"]["std_dev"]["second"] = np.std(enchantedIndex["foil_price_list"]['prices'] * 2)
        enchantedIndex["foil_price_list"]["std_dev"]["third"] = np.std(enchantedIndex["foil_price_list"]['prices'] * 3)
        enchantedIndex["foil_price_list"]["max"] = max(enchantedIndex["foil_price_list"]['prices'])
        enchantedIndex["foil_price_list"]["min"] = min(enchantedIndex["foil_price_list"]['prices'])

with open(formattedJSON, 'w') as f:
    json.dump(formattedData, f, indent=2)

with open("priceIndex.json", 'w') as f:
    json.dump((commonIndex, uncommonIndex, rareIndex, superRareIndex, legendaryIndex, enchantedIndex), f, indent=2)

print("Success!")



        
