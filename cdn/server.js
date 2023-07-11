//to run : node filename.js
const express = require('express')
var cors = require('cors');

const app = express()
const port = 3000
var filepath = './'

app.use(express.static('public'));
app.use(cors({origin: '*'}));

app.listen(port, () => console.log(`Example app listening at http://localhost:${port}`))

//visit localhost:3000
// assuming you have done 1) npm init 2) npm install express