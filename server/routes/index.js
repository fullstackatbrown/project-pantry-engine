const express = require('express');
const router = express.Router();
const search = require('./search');
const path = require("path");

/* GET */
router.get('/', search.get_search);
router.get('/recipes', search.get_results);
// router.get('/', (req, res) => {
//    res.send('index/ home')
// })


/* POST */


/* Exports */
module.exports = router;
