// Listens for the button click event and calls FUNCTION fetchData
document.getElementById('fetchDataBtn').addEventListener('click', fetchData);

const setLinks = document.querySelectorAll('.set-link');
console.log(setLinks);

// Async FUNCTION that takes user input from 'searchInput' and makes an API FETCH request
async function fetchData() {

    // Retrieves userInput from the searchInput field
    const userInput = document.getElementById('searchInput').value;

    // API URL and TOKEN
    const url = 'https://api.pokemontcg.io/v2';
    const TOKEN = '';


    // TRY & CATCH block to handle request and report errors
    try {
        const response = await 
        fetch(`${url}/cards?q=name:${userInput}`, {
            headers: {
                'X-Api-Key': TOKEN
            },
        });

        if (response.ok) {
            const data = await response.json();
            const cards = data.data;
            console.log('Success:', cards);
            createDiv(cards);
        } else {
            console.error('Error:', response.status);
        }
    } catch (error) {
        console.error('Error:', error);
    }
}

function createDiv(cards) {
    
    const container 
    = document.getElementById('search-res-ctn');

    cards.forEach((card) => {

        // Creates 'card-ctn' div and appends to 'search-res-ctn
        const cardCtn =
        document.createElement('div');

        cardCtn.setAttribute('class', 'card-ctn');
        container.appendChild(cardCtn);
        
        // Creates 'card-img-ctn' div and appends to 'card-ctn'
        const cardImgCtn =
        document.createElement('div');

        cardImgCtn.setAttribute('class', 'card-img-ctn');
        cardCtn.appendChild(cardImgCtn);

        // Creates 'img' element and appends to 'card-img-ctn'
        const cardImg =
        document.createElement('img');

        cardImg.setAttribute('src', card.images.small);
        cardImgCtn.appendChild(cardImg);

        // Creates 'card-info-ctn' div and appends to 'card-ctn'
        const cardInfoCtn =
        document.createElement('div');

        cardInfoCtn.setAttribute('class', 'card-info-ctn');
        cardCtn.appendChild(cardInfoCtn);

        // Creates 'h3' element with 'card-name' class and appends to 'card-info-ctn'
        const cardName =
        document.createElement('h3');

        cardName.setAttribute('class', 'card-name');
        cardName.textContent = card.name;
        cardInfoCtn.appendChild(cardName);

        // Creates 'p' element with 'card-set' class and appends to 'card-info-ctn'
        const cardSet =
        document.createElement('p');

        cardSet.setAttribute('class', 'card-set');
        cardSet.textContent = card.set.name;
        cardInfoCtn.appendChild(cardSet);

        // Creates 'p' element with 'card-num' class and appends to 'card-info-ctn'
        const cardNum =
        document.createElement('p');

        cardNum.setAttribute('class', 'card-num');
        cardNum.textContent = 'Card Number: ' + card.number;
        cardInfoCtn.appendChild(cardNum);

        // Creates 'p' element with 'card-price-mkt' class and appends to 'card-info-ctn'
        const cardPriceMkt =
        document.createElement('p');
        cardPriceMkt.setAttribute('class', 'card-price-mkt');
        
        // Depending on card there are multiple prices
        // This loop will iterate through each price and display it
        const cardPrices =
        card.tcgplayer.prices;
        // console.log(cardPrices);

        for (print in cardPrices) {

            const cardPrint =
            document.createElement('p');
            cardPrint.setAttribute('class', 'card-price');
            
            if (print === 'reverseHolofoil') {
                cardPrint.textContent = `Reverse Holofoil: ${cardPrices[print].market}`;
            } else if (print === 'holofoil') {
                cardPrint.textContent = `Holofoil: ${cardPrices[print].market}`;
            } else {
                cardPrint.textContent = `Normal: ${cardPrices[print].market}`;
            }

            cardPriceMkt.appendChild(cardPrint);
            };

        cardInfoCtn.appendChild(cardPriceMkt);



    });
}

async function fetchSetNames(seriesName) {

    // API URL and TOKEN
    const url = 'https://api.pokemontcg.io/v2';
    const TOKEN = '';

    try {
        const response = await 
        fetch(`${url}/sets?q=series:${seriesName}`, {
            headers: {
                'X-Api-Key': TOKEN
            },
        });

        if (response.ok) {
            const data = await response.json();
            const sets = data.data;
            console.log('Success:', sets);
            createSetDiv(sets);

        } else {
            console.error('Error:', response.status);
        }
    } catch (error) {
        console.error('Error:', error);
    }
}

function createSetDiv(sets) {

    const container
    = document.getElementById('set-results-select');

    sets.forEach((set) => {

        const setLink =
        document.createElement('a');
        setLink.setAttribute('href', 'set_temp.html');
        setLink.setAttribute('class', 'set-link');
        setLink.setAttribute('id', set.id);
        container.appendChild(setLink);

        const setImg =
        document.createElement('img');
        setImg.setAttribute('src', set.images.logo);
        setImg.setAttribute('class', 'set-image');
        setLink.appendChild(setImg);


    });
}

for (let i = 0; i < setLinks.length; i++) {
    setLinks[i].onclick = function () {
        console.log('Set link clicked');
        const setId = setLinks[i].id;
        fetchSetData(setId);
       

    }

}



async function fetchSetData(setName) {

    console.log('Set link clicked and page is loaded: ' + setName);
}