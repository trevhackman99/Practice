//Makes a GET request to the API
const keys = ['Artist', 'Name', 'Card_Num']

fetch('https://api.lorcana-api.com/cards/all')
    // Handles the response
    .then(res => {
        //Checks if the response is ok before turning response
        //into JSON and returning it
        if (!res.ok) {
            throw new Error('Network response was not ok');
        } else {
            return res.json();
        }
    })
    // Takes JSON response, converts it to a string and logs it into the console
    .then(data => {
        //Loops through the keys array and stringifys/logs the values of each key from the data JSON
        for (let i = 0; i < keys.length; i++) {
            console.log(JSON.stringify(data[0][keys[i]]));
        }
        
    });

