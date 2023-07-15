//to run : node filename.js
const express = require('express')
var cors = require('cors');

const app = express()
const port = 3000

app.use(express.static('public'));
app.use(cors({origin: '*'}));

app.listen(port, () => console.log(`http://localhost:${port}`))
