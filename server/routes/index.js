const express = require('express');
const router = express.Router();
const search = require('./search');
const elasticsearch = require('@elastic/elasticsearch');
const {Client} = require('@elastic/elasticsearch');
const client = new Client({node: 'http://localhost:9200'});
const path = require("path");

/* GET */
router.get('/', function(req, res){
    res.sendFile(path.join(__dirname+'/index.html'));
})

router.get('/search/:input', function (req, res, next) {
    return search.query('ingredient_index', req.body)
        .then(r => res.send(r))
        .err(e => res.send(e.message));
})


router.get('/suggest/:input', function (req, res) {
    client.search({
        index: 'ingredients_index',
        body: {
            "query": {
                    "should": {
                            "match": {
                                    "ingredients": {query: req.params.title, slop: 100}
                                }
                        }
                }
        }
    })
        .then(function(resp) {res.send(resp);},
            function(err){console.trace(err.message); res.send(err.message);});
});


/* POST */
// None

module.exports = router;
