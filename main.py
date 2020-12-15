"""
Extensão do projeto prático: Extraindo dados da web com Python - Digital Innovation One

Extraindo perguntas e respostas do tópico 'Dúvidas?' do site https://digitalinnovation.one/
"""
import json
import requests
from bs4 import BeautifulSoup

# Página para extração dos dados
link = requests.get('https://digitalinnovation.one/faq')
link.encoding = "utf-8"

soup = BeautifulSoup(link.text, 'html.parser')

div_cards = soup.find_all(class_="card")

all_questions = []
for card in div_cards:
    # Recebe as perguntas e trata informatações
    question_card = card.find(class_="card-title")
    question_temp = question_card.text.split()
    question = ' '.join(question_temp)
    
    # Recebe as respostas e trata informatações
    answer_card = card.find(class_="card-body")
    answer_temp = answer_card.text.split()
    answer = ' '.join(answer_temp)
    
    all_questions.append(
        {
            'pergunta': question,
            'resposta': answer
        }
    )

# Gera arquivo .json contendo as perguntas
with open('questions.json', 'w', encoding='utf-8') as json_file:
    json.dump(all_questions, json_file, indent=3, ensure_ascii=False)


# Gera arquivo .txt contendo as perguntas
with open('questions.txt', 'w', encoding='utf-8') as question_file:
    for index in all_questions:
        question_file.write(f"{index['pergunta']}\n")
        question_file.write(f"{index['resposta']}\n\n")




