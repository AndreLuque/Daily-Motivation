import requests
from typing import NoReturn, TypeVar, List


def getQuote():
	#primero hacemos un request al API
	response = requests.get('https://quotes.rest/qod?category=sports&language=en')
	#la respuesta volvera en json por lo que lo formatamos asi
	response_JSON = response.json()
	#si hay un error en el request si lanzara una excepcion
	if 'error' in response_JSON.keys():
		raise ValueError
	#sino cogemos el quote con su autor, fecha, etc.
	else:
		quote = response.json()['contents']['quotes'][0]['quote']

