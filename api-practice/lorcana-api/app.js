const express = require('express');
const app = express();
const PORT = 3000;

app.use(express.static(__dirname));

// Enable CORS for all routes
app.use((req, res, next) => {
    res.header('Access-Control-Allow-Origin', 'https://api.lorcana-api.com/cards/all'); // Replace with your frontend URL
    res.header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE');
    res.header('Access-Control-Allow-Headers', 'Content-Type, Authorization');
    next();
});

app.get('/', (req, res) => {
    res.sendFile(__dirname + '/index.html');
});

app.listen(PORT, () => {
    console.log('Express server running');
});