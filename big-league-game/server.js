const express = require('express');

const app = express();
const port = 3000;

app.use(express.static(__dirname));

app.get('/', (req, res) => {
    res.sendFile('game.html', { root: __dirname });
});

app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});