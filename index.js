const express = require('express');
const connectDB = require('./DB/Conncection');
const app = express();
const path = require('path');

app.get("/", (req, res )=>{
    res.sendFile(path.join(__dirname, '/src/index.html'));
    
}
)

connectDB();
app.use(express.json({ extended: false }));

const Port = process.env.Port || 4000;

app.listen(Port, () => console.log('Server started'));
