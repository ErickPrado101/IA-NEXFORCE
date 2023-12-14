const express = require('express');
const router = express.Router();
const exceljs = require('exceljs');

router.get('/product/:productId', (req, res) => {
  const productId = req.params.productId;

  const workbook = new exceljs.Workbook();
  workbook.xlsx.readFile('./data/products.xlsx')
    .then(() => {
      const worksheet = workbook.getWorksheet(1);
      const productRow = worksheet.findRow(productId, 1);

      if (productRow) {
        res.json({ productInfo: productRow.values });
      } else {
        res.status(404).json({ message: 'Product not found' });
      }
    })
    .catch(error => {
      res.status(500).json({ error: error.message });
    });
});

module.exports = router;
