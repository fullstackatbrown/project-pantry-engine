const express = require('express');
const router = express.Router();
const {query} = require('./search');
const {queryT} = require('./search');
const path = require("path");

/* GET */
router.get('/', function (req, res) {
    res.sendFile(path.join(__dirname + '/index.html'));
});

router.get('/search/:input', function (req, res, next) {
    query('recipe_index', req.params.input)
        .then(function (resp) {
            res.send(resp);
        });
});

router.get('/searchT/:input', function (req, res) {
    queryT('recipe_index', req.params.input)
        .then(function (resp) {
            res.send(resp);
        });
})

/* POST */

module.exports = router;
