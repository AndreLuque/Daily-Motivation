import requests
from typing import NoReturn, TypeVar, List
import time
import datetime


def getQuote(category: str) -> (str, str):
	#primero hacemos un request al API
	response = requests.get(f'https://quotes.rest/qod?category={category}&language=en')
	#la respuesta volvera en json por lo que lo formatamos asi
	response_JSON = response.json()
	#si hay un error en el request si lanzara una excepcion
	if 'error' in response_JSON.keys():
		return '', ''
	#sino cogemos el quote con su autor, fecha, etc.
	else:
		#obtenemos la frase y el autor
		quote = response_JSON['contents']['quotes'][0]['quote']
		author = response_JSON['contents']['quotes'][0]['author']
		return quote, author



