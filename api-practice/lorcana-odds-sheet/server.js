
const express = require('express');
const app = require('express')();

PORT = 3000;

app.use(express.static(__dirname));

app.get('/', (req, res) => {
    res.sendFile(__dirname + '/table.html');
});

app.get('/formattedData.json', (req, res) => {
    res.sendFile(__dirname + '/formattedData.json');
});

app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});


