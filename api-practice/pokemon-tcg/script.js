// Listens for the button click event and calls FUNCTION fetchData
document.getElementById('fetchDataBtn').addEventListener('click', fetchData);

// Async FUNCTION that takes user input from 'searchInput' and makes an API FETCH request
async function fetchData() {

    // Retrieves userInput from the searchInput field
    const userInput = document.getElementById('searchInput').value;

    // API URL and TOKEN
    const url = 'https://api.pokemontcg.io/v2';
    const TOKEN = 'ba029d49-2600-4cca-9a3d-0167a4b17167';

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
            const card = data.data[0];
            console.log('Success:', card.images.small);
            showImg(card.images.small);
        } else {
            console.error('Error:', response.status);
        }
    } catch (error) {
        console.error('Error:', error);
    }
}

function showImg(imgUrl) {
    const img = document.createElement('img');
    img.src = imgUrl;
    document.body.appendChild(img);
}

    