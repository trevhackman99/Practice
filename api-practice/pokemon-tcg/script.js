// Listens for the button click event and calls FUNCTION fetchData
document.getElementById('fetchDataBtn').addEventListener('click', fetchData);

// Async FUNCTION that takes user input from 'searchInput' and makes an API FETCH request
async function fetchData() {

    // Retrieves userInput from the searchInput field
    const userInput = document.getElementById('searchInput').value;

    // API URL and TOKEN
    const url = 'https://api.pokemontcg.io/v2';
    const TOKEN = '';

    // TRY / CATCH block to handle request and report errors
    try {
        console.log('fetchData FUNCTION called');
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
        
        // 
        const cardImgCtn =
        document.createElement('div');

        cardImgCtn.setAttribute('class', 'card-img-ctn');
        cardCtn.appendChild(cardImgCtn);

        const cardImg =
        document.createElement('img');

        cardImg.setAttribute('src', card.images.small);
        cardImgCtn.appendChild(cardImg);

        const cardInfoCtn =
        document.createElement('div');

        cardInfoCtn.setAttribute('class', 'card-info-ctn');
        cardCtn.appendChild(cardInfoCtn);

        const cardName =
        document.createElement('h3');

        cardName.setAttribute('class', 'card-name');
        cardName.textContent = card.name;
        cardInfoCtn.appendChild(cardName);

        const cardSet =
        document.createElement('p');

        cardSet.setAttribute('class', 'card-set');
        cardSet.textContent = card.set.name;
        cardInfoCtn.appendChild(cardSet);

        const cardNum =
        document.createElement('p');

        cardNum.setAttribute('class', 'card-num');
        cardNum.textContent = 'Card Number: ' + card.number;
        cardInfoCtn.appendChild(cardNum);

        const cardPriceMkt =
        document.createElement('p');
        cardPriceMkt.setAttribute('class', 'card-price-mkt');
        
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

    