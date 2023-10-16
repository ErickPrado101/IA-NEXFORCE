import openai
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from openai import ChatCompletion
from django.http import HttpResponse
from django.conf import settings

def home(request):
    return HttpResponse("Bem-vindo à página inicial do Chatbot.")

@csrf_exempt
def ask_question(request):
    if request.method == 'POST':
        input_text = request.POST.get('question')

        openai.api_key = settings.OPENAI_API_KEY
        response = ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": input_text},
            ]
        )

        chatbot_response = response.choices[0].message['content']

        return JsonResponse({'response': chatbot_response})
    else:
        return JsonResponse({'error': 'Método inválido'})
