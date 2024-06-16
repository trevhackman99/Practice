const token = 'APItoken-here';

async function getData() {

    //Takes input parameters from user at injects them into query

    const symbol = "&symbol=" + document.getElementById('symbol').value;
    const interval = "&interval=" + document.getElementById('time-frame').value;

    // If statement for defining timeframe query parameter

    let timeframe;

    if (interval == 'DAILY' || interval == 'WEEKLY' || interval == 'MONTHLY') {
        timeframe = interval;
    } else {
        timeframe = 'INTRADAY';
    }


    // Query URL

    const url = `https://www.alphavantage.co/query?function=TIME_SERIES_${timeframe}${symbol}${interval}&apikey=${token}`;
    console.log(url);


    const response = await fetch(url);
    const data = await response.json();
    console.log(data);
}

