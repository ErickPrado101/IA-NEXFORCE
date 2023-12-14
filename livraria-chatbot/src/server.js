const express = require('express');
const bodyParser = require('body-parser');
const chatbotRoutes = require('./routes/chatbot');
const excelRoutes = require('./routes/excel');
const paypalRoutes = require('./routes/paypal');

const app = express();
const PORT = 3000;

app.use(bodyParser.json());

app.use('/chatbot', chatbotRoutes);
app.use('/excel', excelRoutes);
app.use('/paypal', paypalRoutes);

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
