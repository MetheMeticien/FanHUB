const express = require('express')

const router = express.Router();


const{register} = require('../controller/RegisterController')



router.post("/api/register",register);


module.exports = router;