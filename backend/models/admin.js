const mongoose = require("mongoose");

const peopleSchema = new mongoose.Schema({
    first_name: {
        type : String,
        unique : true,
        required : true,
    },
    last_name: {
        type : String,
        unique : true,
        required : true,
    },
    email : {
        type : String,
        required : true,
    },
    password : {
        type : String,
        required : true,

    },
    gender : {
        type : String,
    }
    
})


const People = mongoose.model("People",peopleSchema);

module.exports = People;