'use strict';

const mongoose = require('mongoose');
const keys = require('../../bin/keys');

module.exports.connect = async () => {
  try {
    await mongoose.connect(keys.database.connection, {
      useNewUrlParser: true,
      useUnifiedTopology: true,
    });
    console.log('==> [+] mongodb');
  } catch (err) {
    console.error('==> [-] mongodb:', err.message);
  }
};

