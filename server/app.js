const express = require('express');
const path = require('path');
const cookieParser = require('cookie-parser');
const logger = require('morgan');
const indexRouter = require('./routes/index');
const app = express();
const createError = require('http-errors');

app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(express.static("public"));
app.use(cookieParser());

// Routers
app.use('/', indexRouter);
app.use('/recipes', indexRouter);


app.listen(3000, function() {});
// TODO --> what should happen on bad input/ user inputs bogus URL? ie, .../asdf

// Will we have some sort of 404 page?
app.use(function(req,res,next){
    res.send('404 route not found');
})

module.exports = app;
