
document.getElementById('generatePack').addEventListener('click', packRoll);

//Encoded URL for API fetch request
const url = 'https://api.lorcana-api.com/cards/all';

//Fetches data from API after being called by user button #generatePack click
async function packRoll() {
    try {
        const response = await fetch(url, { mode: 'cors' });
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        displayData(data);
    } catch (error) {
        console.error('Error fetching data:', error);
    }
}

//Takes 'data' from API fetch request in packRoll() and displays it in a div
function displayData(data) {
    const dataDiv = document.getElementById('data');
    dataDiv.innerHTML = JSON.stringify(data[0], null, 2);

}