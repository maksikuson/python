import requests
from dotenv import load_dotenv,find_dotenv
load_dotenv(find_dotenv())
import os

CHAT_GPT_API = os.getenv('CHAT_GPT_API')

def get_random_duck():
    enpoint = "https://random-d.uk/api/random"
    response = requests.get(enpoint)
    data = response.json()
    return data['url']

def get_random_cat():
    enpoint = "https://api.thecatapi.com/v1/images/0XYvRd7oD"
    response = requests.get(enpoint)
    data = response.json()
    return data['url']

def get_random_dog():
    enpoint= "https://dog.ceo/api/breeds/image/random"
    response = requests.get(enpoint)
    data = response.json()
    return data['message']

def get_chat_gpt_response(quastion):
    url = 'https://api.openai.com/v1/chat/completions'
    header = {'Content-type': 'application/json', 'Authorization': f'Bearer {CHAT_GPT_API}'}
    data = { "model": "gpt-3.5-turbo", "messages": [{"role": "user", "content": quastion}]}
    response = requests.post(url, headers=header, json=data)
    if response.status_code == 200:
        data = response.json()
        return data['choices'][0]['message']['content']
    else:
        return "Sorry, i can't"
    