const express = require('express');
const app = express();
const PORT = 3000;

// Connects routes.js to server.js
const { fetchData } = require('./routes.js');

// Serve static files (css and js files will not link without this)
app.use(express.static(__dirname));

// TERMINAL cmd to start server; node server.js
app.get('/', (req, res) => {
    res.sendFile(__dirname + '/main.html');
});

app.listen(PORT, () => {
  console.log(`Server is listening on port ${PORT}`);
});

app.get('/call', (req, res) => {
  console.log(`/call route hit: ${req}`);
});
