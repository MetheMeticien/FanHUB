const express = require('express')

const router = express.Router();

const{login,profile,logout} = require('../controller/LoginController');
// const CheckLogin = require('../middlewares/checklogin');




router.post("/api/login",login);
router.get("/api/profile/:username", profile);
router.delete("/api/logout",logout)

module.exports = router;