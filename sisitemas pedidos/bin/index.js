 const express = require('express');
 const bp = require('body-parser');

 const app = express();

 app.use(bp.json({limit: '10mps'}));
 app.use(bp.urlencoded({extendend: false}));

 app.set('view engine', 'ejs');
 app.set('views', 'views')

 app.use(express.static('public'));

 app.use('/', (req, res)=>{
    return res.render('login')
    });

module.exports = app;
