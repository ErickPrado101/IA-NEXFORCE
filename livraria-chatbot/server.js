const express = require('express');
const sqlite3 = require('sqlite3').verbose();
const bodyParser = require('body-parser');
const { OpenAIAPI } = require('openai');

const app = express();
const port = 3000;

app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

const db = new sqlite3.Database('livraria.db');

// Configura sua chave de API do OpenAI
const openai = new OpenAIAPI('SUA_CHAVE_DE_API_AQUI');

app.get('/', (req, res) => {
  res.sendFile(__dirname + '/index.html');
});

app.get('/listar-livros', (req, res) => {
  db.all("SELECT * FROM livros WHERE disponivel = 1", (err, rows) => {
    if (err) {
      res.status(500).send(err.message);
    } else {
      res.json(rows);
    }
  });
});

app.post('/fazer-pedido', (req, res) => {
  const livroId = req.body.livroId;

  db.get("SELECT * FROM livros WHERE id = ? AND disponivel = 1", [livroId], (err, row) => {
    if (err) {
      res.status(500).send(err.message);
    } else if (row) {
      res.send('Livro adicionado ao carrinho!');
    } else {
      res.send('Livro não disponível ou inexistente.');
    }
  });
});

app.post('/interagir-chatgpt', async (req, res) => {
  const mensagemUsuario = req.body.mensagem;

  try {
    const respostaChatGPT = await openai.complete({
      model: 'text-davinci-002',
      messages: [
        { role: 'system', content: 'Você é um chatbot que ajuda em uma livraria.' },
        { role: 'user', content: mensagemUsuario },
      ],
    });

    const mensagemResposta = respostaChatGPT.choices[0].message.content;

    res.send(mensagemResposta);
  } catch (error) {
    res.status(500).send('Erro ao interagir com o ChatGPT.');
  }
});


app.listen(port, () => {
  console.log(`Servidor rodando em http://localhost:${port}`);
});
