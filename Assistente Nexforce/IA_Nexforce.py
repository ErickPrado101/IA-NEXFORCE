# para instalar todos os modulos cole no terminal: pip install -r requirements.txt
import openai  
import speech_recognition as sr  
import whisper  
import pyttsx3  
import os

openai.api_key = "sua_key_string"


sem_palavra_ativadora = False

debug_custo = False

debugar = False

escolher_stt = "google"
entrada_por_texto = False
falar = True

if entrada_por_texto:
    sem_palavra_ativadora = True


def generate_answer(messages):
    #response = openai.ChatCompletion.create( ## Api antiga
    response = openai.chat.completions.create( ## API nova
        model="gpt-3.5-turbo",  ##
        messages=messages,
        temperature=0.5
    )
    return [response.choices[0].message.content, response.usage]


def talk(texto):
    
    engine.say(texto)
    engine.runAndWait()
    engine.stop()


def save_file(dados):
    with open(path + filename, "wb") as f:
        f.write(dados)
        f.flush()



r = sr.Recognizer()
mic = sr.Microphone()
model = whisper.load_model("base")


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', 180)  
for indice, vozes in enumerate(voices): 
    print(indice, vozes.name)
voz = 1  
engine.setProperty('voice', voices[voz].id)

mensagens = [{"role": "system", "content": "Você é um assistente gente boa. E meu nome é Bob!"}]

path = os.getcwd()
filename = "audio.wav"

print("Speak to Text", escolher_stt)

ajustar_ambiente_noise = True

while True:
    text = ""
    question = ""

    if entrada_por_texto:
        question = input("Perguntar pro ChatGPT (\"sair\"): ")
    else:
        
        with mic as fonte:
            if ajustar_ambiente_noise:
                r.adjust_for_ambient_noise(fonte)
                ajustar_ambiente_noise = False
            print("Fale alguma coisa")
            audio = r.listen(fonte)
            print("Enviando para reconhecimento")

            if escolher_stt == "google":
                question = r.recognize_google(audio, language="pt-BR")
            elif escolher_stt == "whisper":
                save_file(audio.get_wav_data())

        if escolher_stt == "whisper":
            text = model.transcribe(path + filename, language='pt', fp16=False)
            question = text["text"]

    if ("esligar" in question and "assistente" in question) or question.startswith("sair"):
        print(question, "Saindo.")
        if falar:
            talk("Desligando")
        break
    elif question == "":
        print("No sound")
        continue
    elif question.startswith("Assistente") or question.startswith("assistente") or question.startswith(
            "chat GPT") or sem_palavra_ativadora:
        print("Me:", question)
        mensagens.append({"role": "user", "content": str(question)})

        answer = generate_answer(mensagens)

        print("ChatGPT:", answer[0])

        if debug_custo:
            print("Cost:\n", answer[1])

        mensagens.append({"role": "assistant", "content": answer[0]})

        if falar:
            talk(answer[0])
    else:
        print("No message")
        continue

    if debugar:
        print("Mensages", mensagens, type(mensagens))
print("See ya!")