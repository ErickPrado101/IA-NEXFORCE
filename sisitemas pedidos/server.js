const app = require('./bin/index');
const keys = require('./bin/keys');
const connection = require('./src/middleware/connection')

app.listen(keys.server.port, ()=>{
    connection.connect();
    console.log('rodando a bagaceira')
});
