const express = require('express');
const router = express.Router();
const paypal = require('paypal-rest-sdk');

router.post('/payment', (req, res) => {
  const paymentData = {
    intent: 'sale',
    payer: {
      payment_method: 'paypal'
    },
    transactions: [{
      amount: {
        total: '10.00',
        currency: 'USD'
      },
      description: 'Bookstore purchase'
    }],
    redirect_urls: {
      return_url: 'http://return.url',
      cancel_url: 'http://cancel.url'
    }
  };

  paypal.payment.create(paymentData, (error, payment) => {
    if (error) {
      res.status(500).json({ error: error.message });
    } else {
      res.json({ paymentLink: payment.links[1].href });
    }
  });
});

module.exports = router;

