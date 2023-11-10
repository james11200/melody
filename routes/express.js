// var express = require('express');
// var router = express.Router();

// /* GET users listing. */
// router.get('/', function(req, res, next) {
//   res.send('respond with a resource');
// });

// module.exports = router;


const express = require('express');
const router = express.Router();
const db = require('../database');

router.get('/user-list', (req, res) => {
  const sql = 'SELECT * FROM customer_db';
  db.query(sql, (err, data) => {
    if (err) throw err;
    res.render('user-list', { title: 'User List', userData: data });
  });
});

module.exports = router;