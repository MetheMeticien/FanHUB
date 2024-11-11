const mongoose = require("mongoose");

const postSchema = new mongoose.Schema({
    postedBy: String,
    celebrity: String,
    content: String,
    imageUrl: String, // To store the image path
});

const Post = mongoose.model('Post', postSchema);

module.exports = Post;