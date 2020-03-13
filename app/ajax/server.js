const bodyParse = require('body-parse')
const express = require('express')
const app = express()

app.use(express.static('.'))
app.use(bodyParse.urlencode({ extended: true}))
app.use(bodyParse.json())

app.get('/test', (req, res) => res.send('Ok'))
app.listen(8081, () => console.log('Executando...'))