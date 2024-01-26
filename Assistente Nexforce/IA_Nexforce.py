

import openai


openai.api_key = "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"

def gerar_resposta(messages):
    
    response = openai.chat.completions.create( 
        model="gpt-3.5-turbo", 
        messages=messages,
        temperature=0.5
    )
    return [response.choices[0].message.content, response.usage]

mensagens = [{"role": "system", "content": "Você é um assistente da Nexforce formado em Relações públicas, seu nome é Carla."}]

while True:
    
    question = input("Perguntar pro ChatGPT (\"sair\"): ")

    if question == "sair" or question == "":
        print("saindo")
        break
    else:
        mensagens.append({"role": "user", "content": str(question)})

        answer = gerar_resposta(mensagens)
        print("Você:", question)
        print("ChatGPT:", answer[0], "\nCusto:\n", answer[1])
        mensagens.append({"role": "assistant", "content": answer[0]})

    debugar = True
    if debugar:
        print("Mensagens", mensagens, type(mensagens))
