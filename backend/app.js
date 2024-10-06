const express = require("express");
const mongoose = require("mongoose");
const bcrypt = require("bcrypt");
const jwt = require("jsonwebtoken");
const cookieParser = require("cookie-parser");
const multer = require('multer');
const path = require('path');
const dotenv = require('dotenv');
const cors = require('cors');
const app = express();
dotenv.config();

const portNo = process.env.port;
const mongourl = process.env.DB;
//console.log(mongourl);



mongoose
  .connect(mongourl, {
    useNewUrlParser: true,
    useUnifiedTopology: true,
  })
  .then(() => {
    console.log("Connected to MongoDB");
  })
  .catch((error) => {
    console.error("Error connecting to MongoDB:", error);
  });



app.use(express.json());
app.use(cors())
//app.use(cors());
app.use(cookieParser());
app.use(express.urlencoded({ extended: true }));
app.set("view engine", "ejs");



app.get('/',(req,res)=>{
  res.send("Is IT OKK::??");

})
const RegisterRouter = require('./routers/RegisterRouter');
const LoginRouter = require('./routers/LoginRouter');



app.use('/',RegisterRouter);
app.use('/',LoginRouter);


app.listen(portNo,()=> {
    console.log(`Server listening on port ${portNo}`);
})