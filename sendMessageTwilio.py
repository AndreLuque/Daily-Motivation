from twilio.rest import Client
from typing import List, NoReturn, TypeVar

T = TypeVar('T')

def sendMessageTwilio(text: T, user_number: str) -> NoReturn:

	#primero inicializamos nuestros credenciales
	account_sid = 'AC79f4fb318d07f76a17b23a56573bd04a' 
	auth_token = '*********************************'
	#creamos el cliente 
	client: Client = Client(account_sid, auth_token)

	#aqui haremos el request para coger el body
	body = str(text)

	#establecemos los numeros que se utilizaran para mandar y recibir el mensje
	sender_number = 'whatsapp:+14155238886'
	receiver_number = 'whatsapp:' + user_number

	#creamos el mensaje que se mandara
	message = client.messages.create(from_ = sender_number, body = body, to = receiver_number)

