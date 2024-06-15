const express = require('express');
const app = express();
const PORT = 3000;

app.use(express.static(__dirname));

app.get('/', (req, res) => {
    res.sendFile(__dirname + '/home.html');
    });

app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
    });

