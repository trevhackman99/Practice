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

document.getElementById('reset-btn').addEventListener('click', function() {
    packsOpenedCount = 0;
    superRareCounter = 0;
    legendaryCounter = 0;

    superRareFoilCounter = 0;
    legendaryFoilCounter = 0;
    enchantedCounter = 0;

    document.getElementById('packs-opened').innerHTML = `Packs Opened: ${packsOpenedCount}`;
    document.getElementById('super-rare-counter').textContent = `Super Rares: ${superRareCounter}`;
    document.getElementById('legendary-counter').textContent = `Legendaries: ${legendaryCounter}`;
    document.getElementById('super-rare-foil-counter').textContent = `Super Rare Foils: ${superRareFoilCounter}`;
    document.getElementById('legendary-foil-counter').textContent = `Legendary Foils: ${legendaryFoilCounter}`;
    document.getElementById('enchanted-counter').textContent = `Enchanted: ${enchantedCounter}`;

    document.getElementById('main-table-body').innerHTML = "";

    

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
            console.log("Slot Roll: ", slotRoll);
            if (slotRoll <= rare) {
                let randomIndex = Math.floor(Math.random() * rareCards.length);
                if (!pack.includes(rareCards[randomIndex])) {
                   
                    pack.push(rareCards[randomIndex]);
                    cardAdded = true;
                    slotRoll = Math.random() * 2;

                }
            } 
                
            if (!cardAdded && slotRoll >= super_rare + rare) {
                let randomIndex = Math.floor(Math.random() * superRareCards.length);
                if (!pack.includes(superRareCards[randomIndex])) {
                   
                    pack.push(superRareCards[randomIndex]);
                    superCardPulled(foil = false);
                    cardAdded = true;
                    slotRoll = Math.random() * 2;

                }
            }
            if (!cardAdded && slotRoll <= (2 - legendary)) {
                let randomIndex = Math.floor(Math.random() * legendaryCards.length);
                if (!pack.includes(legendaryCards[randomIndex])) {
                    
                    pack.push(legendaryCards[randomIndex]);
                    legendaryCardPulled(foil = false);
                    cardAdded = true;
                    slotRoll = Math.random() * 2;

                }
            }
            if (!cardAdded) {
                console.log("DUPLICATE CARD PULLED! " + slotRoll);
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
}
});

packsOpenedCount = 0;
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