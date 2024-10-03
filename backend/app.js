const express = require("express");
const dotenv = require("dotenv");

dotenv.config();

const app = express();

const portNo = process.env.port;

app.listen(portNo,()=> {
    console.log(`Server listening on port ${portNo}`);
})