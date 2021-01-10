var express = require('express');
var router = express.Router();

/* GET / */
router.get('/', function(req, res, next) {
  res.json({ title: 'modify routes/index.js' });
});

module.exports = router;
