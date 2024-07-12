const common = 6;
const uncommon = 3;
const rare = 1.362;
const super_rare = .478;
const legendary = .160;

const commonFoil = .5591;
const uncommonFoil = .25;
const rareFoil = .12;
const superRareFoil = .0417;
const legendaryFoil = .02;

const enchanted = .0092;



let cardData = ""

window.onload = function() {
    fetch('formattedData.json')
        .then(response => response.json())
        .then(data => {
            cardData = data;
        })

        .catch(error => {
            console.error('Error fetching data:', error);
        }

    );
};

document.getElementById('gen-chart-btn').addEventListener('click', function() {
    let chart = document.getElementById('chart');

    let ranges = ['0-30', '31-60', '61-90', '91-120', '121-150', '151-180', '181-210', '211-240', '241-270', '271-300', '301-330', '331-360', '361-390', '391-420', '421-10000'];

    let counts = ranges.map(function(range) {
        let bounds = range.split('-').map(Number);
        return bbValue.reduce(function(count, num) {
            return (num >= bounds[0] && num <= bounds[1]) ? count + 1 : count;
        }, 0);
    })

    console.log(bbValue)

    createChart = new Chart(chart, {
        type: 'bar',
        data: {
            labels: ranges,
            datasets: [{
                label: 'Number of BBs',
                data: counts,
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                    
                },
                x: {
                    type: 'category',
                    labels: ranges
                }
            }
        }

    });
});


document.getElementById('reset-btn').addEventListener('click', function() {
    packsOpenedCount = 0;
    totalValue = 0;
    maxPackValue = 0;
    packValue = 0;
    superRareCounter = 0;
    legendaryCounter = 0;
    currentbbValue = 0;
    bbValue = [];


    superRareFoilCounter = 0;
    legendaryFoilCounter = 0;
    enchantedCounter = 0;

    expectedValue = 0;
    avgValue = 0;

    document.getElementById('packs-opened').innerHTML = `Packs Opened: ${packsOpenedCount}`;

    document.getElementById('total-value').textContent = `Total Value: $${totalValue.toFixed(2)}`;
    maxPackValueElement.textContent = "Max Pack Value: $" + maxPackValue.toFixed(2);
    packValueElement.textContent = "Pack Value: $" + packValue.toFixed(2);
    document.getElementById('expected-value').textContent = `EV per Pack: $${expectedValue.toFixed(2)}`;
    document.getElementById('avg-value').textContent = `Average Value: $${avgValue.toFixed(2)}`;
    document.getElementById('current-bb-value').textContent = `Current BB Value: $${currentbbValue.toFixed(2)}`;
    document.getElementById('avg-bb-value').textContent = `Average BB Value: $0.00`;

    document.getElementById('super-rare-counter').textContent = `Super Rares: ${superRareCounter}`;
    document.getElementById('legendary-counter').textContent = `Legendaries: ${legendaryCounter}`;
    document.getElementById('super-rare-foil-counter').textContent = `Super Rare Foils: ${superRareFoilCounter}`;
    document.getElementById('legendary-foil-counter').textContent = `Legendary Foils: ${legendaryFoilCounter}`;
    document.getElementById('enchanted-counter').textContent = `Enchanted: ${enchantedCounter}`;

    document.getElementById('main-table-body').innerHTML = "";
    document.getElementById('info-table').innerHTML = "";

    document.getElementById('chart').innerHTML = "";

});

document.getElementById('pack-open-btn').addEventListener('click', function() {

    const desiredPacks = document.getElementById('desiredPacks').value;

    

    for (let totalPacksDesired = 0; totalPacksDesired < desiredPacks; totalPacksDesired++) {
        const pack = [];

        const commonCards = cardData.filter(card => 
            card.rarity === 'Common');

        for (let i = 0; i < common; i++) {
            let randomIndex = Math.floor(Math.random() * commonCards.length);
            if (pack.includes(commonCards[randomIndex])) {
                i--;
            } else {
                pack.push(commonCards[randomIndex]);
            }
        }

        const uncommonCards = cardData.filter(card =>
            card.rarity === 'Uncommon');

        for (let i = 0; i < uncommon; i++) {
            let randomIndex = Math.floor(Math.random() * uncommonCards.length);
            if (pack.includes(uncommonCards[randomIndex])) {
                i--;
            } else {
                pack.push(uncommonCards[randomIndex]);
            }
        }
            

        const rareCards = cardData.filter(card =>
            card.rarity === 'Rare');

        const superRareCards = cardData.filter(card =>
            card.rarity === 'Super_rare');

        const legendaryCards = cardData.filter(card =>
            card.rarity === 'Legendary');

        let slotRoll = Math.random() * 2;
        for (let i = 0; i < 2; i++) {
            let cardAdded = false;
            //console.log("Slot Roll: ", slotRoll);
            if (!cardAdded && slotRoll <= rare) {
                let randomIndex = Math.floor(Math.random() * rareCards.length);
                if (!pack.includes(rareCards[randomIndex])) {
                   
                    pack.push(rareCards[randomIndex]);
                    cardAdded = true;
                    slotRoll = Math.random() * 2;

                }
            } 
                
            else if (!cardAdded && slotRoll <= super_rare + rare) {
                let randomIndex = Math.floor(Math.random() * superRareCards.length);
                if (!pack.includes(superRareCards[randomIndex])) {
                   
                    pack.push(superRareCards[randomIndex]);
                    superCardPulled(foil = false);
                    cardAdded = true;
                    slotRoll = Math.random() * 2;

                }
            }
            else if (!cardAdded && slotRoll >= (2 - legendary)) {
                let randomIndex = Math.floor(Math.random() * legendaryCards.length);
                if (!pack.includes(legendaryCards[randomIndex])) {
                    
                    pack.push(legendaryCards[randomIndex]);
                    legendaryCardPulled(foil = false);
                    cardAdded = true;
                    slotRoll = Math.random() * 2;

                }
            }
            if (!cardAdded) {
                // console.log("DUPLICATE CARD PULLED! " + slotRoll);
                i--;
                
            }
        }

        const enchantedCards = cardData.filter(card =>
            card.rarity === 'Enchanted');

        let foilSlotRoll = Math.random();
        if (foilSlotRoll <= commonFoil) {
            let randomIndex = Math.floor(Math.random() * commonCards.length);
            pack.push(commonCards[randomIndex]);
        } else if (foilSlotRoll <= uncommonFoil + commonFoil) {
            let randomIndex = Math.floor(Math.random() * uncommonCards.length);
            pack.push(uncommonCards[randomIndex]);
        } else if (foilSlotRoll <= rareFoil + uncommonFoil + commonFoil) {
            let randomIndex = Math.floor(Math.random() * rareCards.length);
            pack.push(rareCards[randomIndex]);
        } else if (foilSlotRoll <= superRareFoil + rareFoil + uncommonFoil + commonFoil) {
            let randomIndex = Math.floor(Math.random() * superRareCards.length);
            pack.push(superRareCards[randomIndex]);
            superCardPulled(foil = true);
        } else if (foilSlotRoll <= legendaryFoil + superRareFoil + rareFoil + uncommonFoil + commonFoil) {
            let randomIndex = Math.floor(Math.random() * legendaryCards.length);
            pack.push(legendaryCards[randomIndex]);
            legendaryCardPulled(foil = true);
        } else if (foilSlotRoll >= (1 - enchanted)) {
            let randomIndex = Math.floor(Math.random() * enchantedCards.length);
            pack.push(enchantedCards[randomIndex]);
            enchantedCardPulled();
        }


            

                
        loadPackResults(pack);
        loadCardInfoStatistics(pack);
}
});

packsOpenedCount = 0;
revolvingPackCount = 0;
bbValue = [];
currentbbValue = 0;
totalValue = 0;
maxPackValue = 0;
expectedValue = 0;
avgValue = 0;

superRareCounter = 0;
legendaryCounter = 0;

superRareFoilCounter = 0;
legendaryFoilCounter = 0;
enchantedCounter = 0;

function superCardPulled(foil = false) {
    if (foil === false) {
        superRareCounter++;
        superRareCounterElement = document.getElementById('super-rare-counter');
        superRareCounterElement.textContent = `Super Rares: ${superRareCounter}`;
    } else if (foil === true) {
        superRareFoilCounter++;
        superRareFoilCounterElement = document.getElementById('super-rare-foil-counter');
        superRareFoilCounterElement.textContent = `Super Rare Foils: ${superRareFoilCounter}`;
    }
}

function legendaryCardPulled(foil = false) {
    if (foil === false) {
        legendaryCounter++;
        legendaryCounterElement = document.getElementById('legendary-counter');
        legendaryCounterElement.textContent = `Legendaries: ${legendaryCounter}`;
    } else if (foil === true) {
        legendaryFoilCounter++;
        legendaryFoilCounterElement = document.getElementById('legendary-foil-counter');
        legendaryFoilCounterElement.textContent = `Legendary Foils: ${legendaryFoilCounter}`;

    }
}

function enchantedCardPulled() {
    enchantedCounter++;
    enchantedCounterElement = document.getElementById('enchanted-counter');
    enchantedCounterElement.textContent = `Enchanted: ${enchantedCounter}`;
}

function loadPackResults(pack) {
    
    packsOpened = document.getElementById('packs-opened');
    packsOpenedCount++;
    packsOpened.textContent = `Packs Opened: ${packsOpenedCount}`;

    

    totalValueElement = document.getElementById('total-value');
    packValueElement = document.getElementById('pack-value');
    maxPackValueElement = document.getElementById('max-pack-value');
    expectedValueElement = document.getElementById('expected-value');
    avgValueElement = document.getElementById('avg-value');

    let packValue = 0;
    //console.log(pack.length)

    for (let i = 0; i < pack.length; i++) {
        if (i === (pack.length - 1)) {
            packValue += pack[i].foil;
           // console.log("Card FOIL $ added: $" + pack[i].foil);
        } else {
            packValue += pack[i].normal;
           // console.log("Card $ added: $" + pack[i].normal);
        }
    }

    if (packValue > 300) {
        highValuePack(pack, packValue);
    }

    totalValue += packValue;
    if (maxPackValue < packValue) {
        maxPackValue = packValue;
    }

    avgValue = totalValue / packsOpenedCount;

    avgValueElement.textContent = "Average Value: $" + avgValue.toFixed(2);

    maxPackValueElement.textContent = "Max Pack Value: $" + maxPackValue.toFixed(2);
    packValueElement.textContent = "Pack Value: $" + packValue.toFixed(2);
    totalValueElement.textContent = "Total Value: $" + totalValue.toFixed(2);

    revolvingPackCount++;
    

    if (revolvingPackCount > 24) {
        bbValue.push(currentbbValue);
        currentbbValue = 0;
        revolvingPackCount = 1;

        avgbbValueElement = document.getElementById('avg-bb-value');
        avgbbValueElement.textContent = "Average BB Value: $" + (bbValue.reduce((a, b) => a + b, 0) / bbValue.length).toFixed(2);
        

    } else {
        currentbbValue += packValue;
    }

    currentbbValueElement = document.getElementById('current-bb-value');
    currentbbValueElement.textContent = "Current BB Value: $" + currentbbValue.toFixed(2);



    

    
    document.getElementById('main-table-body').innerHTML = "";

    for (let i = 0; i < pack.length; i++) {
        const table = document.getElementById('main-table-body');
        let row = document.createElement('tr');
        let cell = document.createElement('td');
        cell.textContent = `${pack[i].name} - ${pack[i].version}`;
        row.appendChild(cell);
        cell = document.createElement('td');
        cell.textContent = pack[i].set;
        row.appendChild(cell);
        cell = document.createElement('td');
        cell.textContent = pack[i].collector_number;
        row.appendChild(cell);
        cell = document.createElement('td');
        cell.textContent = pack[i].rarity;
        row.appendChild(cell);
        cell = document.createElement('td');
        cell.textContent = pack[i].normal;
        row.appendChild(cell);
        cell = document.createElement('td');
        cell.textContent = pack[i].foil;
        row.appendChild(cell);

        table.appendChild(row);



    }
}


function loadCardInfoStatistics(pack) {

    const allPulledCards = [];

    const uniqueCardIds = [];


    for (let i = 0; i < pack.length; i++) {
        pulledCard = {};
        if ((pack[i].normal >= 5) || (pack[i].rarity === "Enchanted")) {
            
            if (!allPulledCards.some(card => card.id === pack[i].id)) {
                pulledCard.id = pack[i].id;
                pulledCard.count = 1;
                allPulledCards.push(pulledCard);
                uniqueCardIds.push(pack[i].id);
            } else {
                allPulledCards.find(card => card.id === pack[i].id).count++;
            }
            
        }

    }



/*

    for (let card of uniqueCardIds) {
        let table = document.getElementById('info-table');

        let row = document.createElement('tr');
        let cell = document.createElement('td');
        let imgCell = document.createElement('td');
        
        let img = document.createElement('img');
        img.src = cardData.find(cardData => cardData.id === card).img;

        imgCell.appendChild(img);
        
        row.appendChild(imgCell);


        cell.innerHTML = `${cardData.find(cardData => cardData.id === card).name} - ${cardData.find(cardData => cardData.id === card).version}`;
        

        row.appendChild(cell);

        cell.innerHTML = `${cardData.find(cardData => cardData.id === card).normal}`;

        table.appendChild(row);

        


    } */
}

function highValuePack(pack) {
    console.log("High Value Pack Opened!");

    for (let i = 0; i < pack.length; i++) {
        if (i < pack.length - 1) {
            console.log(pack[i].name + " " + pack[i].normal);
        } else {
            console.log(pack[i].name + " " + pack[i].foil);
        }
        
    }

}

