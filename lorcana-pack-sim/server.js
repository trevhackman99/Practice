const express = require('express');
const app = express();
const path = require('path');
const PORT = 3000;

app.use(express.static('public/html'));

// Enable CORS for all routes
app.use((req, res, next) => {
    res.header('Access-Control-Allow-Origin', 'https://api.lorcana-api.com/cards/all'); // Replace with your frontend URL
    res.header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE');
    res.header('Access-Control-Allow-Headers', 'Content-Type, Authorization');
    next();
});

app.get("/", (req, res) => {
    res.sendFile(path.join(__dirname, "public/html/lorcanasim.html"));
});

app.listen(PORT, () => {
    console.log('Express server running');
});