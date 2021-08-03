import time
from typing import List, TypeVar, NoReturn
from datetime import datetime, date
from getQuoteAPI import getQuote
from sendMessageTwilio import sendMessageTwilio


def main ():
	stay: bool = True
	#primero cogemos la fecha de cuando se inicio la aplicacion
	current_date1 = datetime.date(datetime.now())
	timeDifference: int = 0
	while True:
		t = time.localtime()
		print(t)
		current_hour = time.strftime("%H", t)
		current_minute = time.strftime("%M", t)
		current_date2 = datetime.date(datetime.now())
		#si coincide con el horario elegido por el usuario, mandaremos el quote
		if int(current_hour) == 20  and int(current_minute) == 5 and stay:
			stay = False
			#primero obtenemos las categorias
			listQuotes: List[(str, str)] = []
			for category in ['Inspire']:
				quote, author = getQuote(category.lower())
				if quote != '':
					listQuotes += [(category, quote, author)]
			#mandamos un mensaje separado para cada quote		
			for message in listQuotes:
				sendMessageTwilio('-' + message[0] + '-' + '\n' + message[2] + ':' + '\n' + message[1], '+34629332528')
			if len(listQuotes) != 0:
				sendMessageTwilio('!!!Respond to message to keep recieving quotes daily!!!', '+34629332528')	

		#cada tres dias el usuario tiene que mandar un mensaje para renovar la suscripcion
		if timeDifference != (current_date1 - current_date2).days:
			timeDifference = (current_date1 - current_date2).days
			if timeDifference % 3 == 0 and timeDifference != 0:
				sendMessageTwilio("Send the message 'join invented-outer' to renew your quote subscription", '+34629332528')

		#time.sleep(5)
		if not stay:
			time.sleep(3600)
			stay = True
		else:
			time.sleep(29)


if __name__ == '__main__': main()