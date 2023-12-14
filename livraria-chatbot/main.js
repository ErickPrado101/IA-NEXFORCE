const chatContainer = document.getElementById('chat');
const userInput = document.getElementById('user-input');

async function sendMessage() {
  const message = userInput.value;
  displayUserMessage(message);

  const respostaServidor = await enviarMensagemParaServidor(message);
  displayBotMessage(respostaServidor);

  userInput.value = '';
}

function displayUserMessage(message) {
  const messageDiv = document.createElement('div');
  messageDiv.innerHTML = `<div class="user-message">${message}</div>`;
  chatContainer.appendChild(messageDiv);
}

function displayBotMessage(message) {
  const messageDiv = document.createElement('div');
  messageDiv.innerHTML = `<div class="bot-message">${message}</div>`;
  chatContainer.appendChild(messageDiv);
}

async function enviarMensagemParaServidor(mensagem) {
  try {
    const resposta = await fetch('http://localhost:3000/interagir-chatgpt', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ mensagem }),
    });

    const resultado = await resposta.json();
    return resultado;
  } catch (error) {
    return 'Erro ao interagir com o servidor.';
  }
}
