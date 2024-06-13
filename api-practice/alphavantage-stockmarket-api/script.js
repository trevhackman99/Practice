const token = 'APItoken-here';

async function getData() {

    const symbol = "&symbol=" + document.getElementById('symbol').value;
    const interval = "&interval=" + document.getElementById('time-frame').value;

    let timeframe;

    if (interval == 'DAILY' || interval == 'WEEKLY' || interval == 'MONTHLY') {
        timeframe = interval;
    } else {
        timeframe = 'INTRADAY';
    }


    

    const url = `https://www.alphavantage.co/query?function=TIME_SERIES_${timeframe}${symbol}${interval}&apikey=${token}`;
    console.log(url);


    const response = await fetch(url);
    const data = await response.json();
    console.log(data);
}

