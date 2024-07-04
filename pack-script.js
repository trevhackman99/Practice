const common = 6;
const uncommon = 3;
const rare = 1.362;
const super_rare = .478;
const legendary = .160;
const enchanted = .0092;

let cardData = ""

window.onload = function() {
    fetch('formattedData.json')
        .then(response => response.json())
        .then(data => {
            console.log("json fetched")
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
    document.getElementById('packs-opened').innerHTML = `Packs Opened: ${packsOpenedCount}`;
    document.getElementById('super-rare-counter').textContent = `Super Rares: ${superRareCounter}`;
    document.getElementById('legendary-counter').textContent = `Legendaries: ${legendaryCounter}`;

    document.getElementById('main-table-body').innerHTML = "";

    

});

document.getElementById('pack-open-btn').addEventListener('click', function() {

    const desiredPacks = document.getElementById('desiredPacks').value;
    console.log(desiredPacks);

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

    for (let i = 0; i < 2; i++) {
            let slotRoll = (Math.random() * 2);
            console.log(slotRoll);
            while (slotRoll <= rare) {
                let randomIndex = Math.floor(Math.random() * rareCards.length);
                if (pack.includes(rareCards[randomIndex])) {
                    continue;
                } else {
                    pack.push(rareCards[randomIndex]);
                    break;
                }
            } 
            
            while (slotRoll > rare && slotRoll < (2 - legendary)) {
                let randomIndex = Math.floor(Math.random() * superRareCards.length);
                if (pack.includes(superRareCards[randomIndex])) {
                    continue;
                } else {
                    pack.push(superRareCards[randomIndex]);
                    superCardPulled();
                    break;
                }
            }
            while (slotRoll >= (2 - legendary)) {
                let randomIndex = Math.floor(Math.random() * legendaryCards.length);
                if (pack.includes(legendaryCards[randomIndex])) {
                    continue;
                } else {
                    pack.push(legendaryCards[randomIndex]);
                    legendaryCardPulled();
                    break;
                }
            }
        }

        loadPackResults(pack);
}
});

packsOpenedCount = 0;
superRareCounter = 0;
legendaryCounter = 0;

function superCardPulled() {
    superRareCounter++;
    superRareCounterElement = document.getElementById('super-rare-counter');
    superRareCounterElement.textContent = `Super Rares: ${superRareCounter}`;

}

function legendaryCardPulled() {
    legendaryCounter++;
    legendaryCounterElement = document.getElementById('legendary-counter');
    legendaryCounterElement.textContent = `Legendaries: ${legendaryCounter}`;


}

function loadPackResults(pack, legendaryCount, superRareCount) {
    
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