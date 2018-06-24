from django.views import generic
from django.views.decorators.csrf import csrf_exempt
import json
import requests
import random
from django.shortcuts import render
from dicionario_farmacos.models import Farmaco
from dicionario_doencas.models import Doenca
from dicionario_alimentos.models import Alimento
from dicionario_termos.models import Termo


def respond_to_websockets(message):
    lista_farmacos = Farmaco.objects.filter(nome__isnull=False).order_by('nome')
    mensagens = {
     'saudacoes': ["""Olá! Digite um fármaco ou uma doença que você deseja consultar.""",
                   """Oi! Posso te ajudar? digite um termo médico ou um alimento que deseja saber a respeito""",],
     'naosei': ["""Não sei uma resposta para essa mensagem. Digite um medicamento ou uma doença que você deseja consultar.""",
                """Desculpe, mas não entendo essa mensagem. Digite um termo médico ou um alimento que você deseja consultar."""],
    'AAS': ["""medicamento.""",],
      }

    result_message = {
        'type': 'text'
    }

    for farmaco in lista_farmacos:
        if farmaco.nome == message['text']:
            result_message['text'] = farmaco.introducao+" Para saber mais sobre "+farmaco.nome+" ou outro fármaco, digite:"+'\n'+"nome e assunto\
            (indicações, farmacodinâmica, farmacocinética, contraindicações,\
            risco na gravidez, interações ou reações adversas)"
            return result_message
        elif farmaco.nome in message['text'] and "indicações" in message['text']:
            result_message['text'] = "Indicações para "+farmaco.nome+" : "+farmaco.indicacoes
            return result_message
        else:
            pass

    if 'AAS' in message['text'] or 'nimesulida' in message['text']:
        result_message['text'] = random.choice(mensagens['AAS'])
    elif message['text'] in ['oi', 'olá', 'Oi', "Olá", "Bom dia", "Boa noite", "Boa tade"]:
        result_message['text'] = random.choice(mensagens['saudacoes'])
    else:
        result_message['text'] = random.choice(mensagens['naosei'])

    return result_message
