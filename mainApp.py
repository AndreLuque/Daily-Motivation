
import time
from getQuoteAPI import getQuote
from sendMessageTwilio import sendMessageTwilio
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QMessageBox, QGridLayout, QMainWindow, QStatusBar, QToolBar, QAction, QLineEdit, QComboBox, QHBoxLayout, QVBoxLayout, QTableWidget, QTableWidgetItem, QHeaderView, QCheckBox
from PyQt5.QtGui import QFont, QPixmap
from PyQt5 import QtCore
import pickle
from typing import List, TypeVar, NoReturn
from datetime import datetime, date

T = TypeVar('T')

class MainWindow(QMainWindow):
	def __init__(self, parent = None):
		#damos los parametros del constructor de su padre
		super().__init__(parent)

		#ponemos la pantalla del inicio
		self.__home_screen()

	def __add_elements_comboBox(self, comboBox: QComboBox, listElements: List[T]) -> NoReturn:
		for element in listElements:
			comboBox.addItem(str(element))	

	def __QRcode(self):
		#como se dsitrubuira la informacion
		layout = QVBoxLayout()

		#ponemos el primer mensaje
		message1 = QLabel('Scan the QR Code')
		message1.setStyleSheet('font-size : 40px; font-weight : bold; color: white')
		message1.setAlignment(QtCore.Qt.AlignCenter)
		layout.addWidget(message1)

		#ponemos la imagen del codigo qr
		qrImage = QLabel()
		qrImage.setStyleSheet('image : url(QRcode.png)')
		#qrImage.setFixedHeight(200)
		#qrImage.setFixedWidth(200)
		layout.addWidget(qrImage)

		#ponemos el segundo mensaje
		message2 = QLabel('and send the message that appears!')
		message2.setStyleSheet('font-size : 40px; font-weight : bold; color: white')
		message2.setAlignment(QtCore.Qt.AlignCenter)
		layout.addWidget(message2)

		#ponemos un boton para probar el numero
		testButton = QPushButton('Test')
		testButton.setStyleSheet('background-color : darkblue; color : white')
		layout.addWidget(testButton)

		centralWidget = QWidget()
		centralWidget.setStyleSheet('background-color : blue')
		centralWidget.setLayout(layout)
		self.setCentralWidget(centralWidget)

		#cuando el boton sea pulsado de conectara a esta funcion
		testButton.clicked.connect(lambda: self.__test_number())

	def __test_number(self):
		try:
			sendMessageTwilio('SUCCESS! You have joined Daily Motivation. (Respond to messages to keep recieving Daily Quotes)', self.numberText)
			self.close()
		except:
			self.__change_to_start_screen()
			self.__enterNumber.setText('')
			self.__enterNumber.setStyleSheet('border : 2px solid red; background-color : white')
			self.__enterNumber.setPlaceholderText('!!INCORRECT NUMBER!!')		

	def __home_screen(self):
		self.setWindowTitle('DAILY MOTIVATION')	

		#como se distrubuiran los widgets
		layout = QVBoxLayout()
			
		#ponemos el titulo de la pantalla y ajustamos su formato
		title = QLabel('DAILY' + '\n' + 'MOTIVATION')
		title.setAlignment(QtCore.Qt.AlignCenter)
		title.setStyleSheet('color : white; font-size : 100px; font-weight : bold')
		layout.addWidget(title)

		#layout.addWidget(QWidget())

		#boton para confirmar el email
		login = QPushButton('START')
		layout.addWidget(login)

		layout.addWidget(QWidget())

		#lo denominamos nuestro central widget
		centralWidget = QWidget()
		centralWidget.setLayout(layout)
		self.setCentralWidget(centralWidget)

		#cuando el boton sea pulsado de conectara a esta funcion
		login.clicked.connect(lambda: self.__change_to_start_screen())

	def __change_to_start_screen(self):
		#establecemos como se van a distribuir los widgets
		layout = QVBoxLayout()
		
		#ponemos el titulo de la pagina
		title = QLabel('Let´s Start')
		title.setStyleSheet('color : white; font-size : 50px; font-weight: bold')		
		layout.addWidget(title)
				
		#dejamos un hueco para introducir el numero
		self.__enterNumber = QLineEdit(placeholderText = 'Enter Whatsapp Phone Number (Example: +34633890056)')
		self.__enterNumber.setStyleSheet('background-color : white; color : black')
		layout.addWidget(self.__enterNumber)

		#dejamos un hueco para introducir la hora
		self.__time = QLineEdit(placeholderText = 'At what time do you want to recieve the quotes? (Example: 12:42)')
		self.__time.setStyleSheet('background-color : white; color : black')
		self.__time.setMaxLength(5)
		layout.addWidget(self.__time)

		self.__checkboxLabel = QLabel('Select Categories that you are interested in:')
		self.__checkboxLabel.setStyleSheet('color : white; font-size : 20px')
		layout.addWidget(self.__checkboxLabel)

		sublayout1 = QHBoxLayout()

		#el usuario pulsara en las cajas que cumple su preferencia
		self.__checkbox1 = QCheckBox('Inspire')
		self.__checkbox1.setStyleSheet('color : white')
		sublayout1.addWidget(self.__checkbox1)
		self.__checkbox2 = QCheckBox('Sports')
		self.__checkbox2.setStyleSheet('color : white')
		sublayout1.addWidget(self.__checkbox2)
		self.__checkbox3 = QCheckBox('Love')
		self.__checkbox3.setStyleSheet('color : white')
		sublayout1.addWidget(self.__checkbox3)
		layout.addLayout(sublayout1)

		sublayout2 = QHBoxLayout()

		self.__checkbox4 = QCheckBox('Life')
		self.__checkbox4.setStyleSheet('color : white')
		sublayout2.addWidget(self.__checkbox4)
		self.__checkbox5 = QCheckBox('Funny')
		self.__checkbox5.setStyleSheet('color : white')
		sublayout2.addWidget(self.__checkbox5)
		self.__checkbox6 = QCheckBox('Students')
		self.__checkbox6.setStyleSheet('color : white')
		sublayout2.addWidget(self.__checkbox6)
		layout.addLayout(sublayout2)

		#widget flaso de relleno
		layout.addWidget(QWidget())

		#boton para continuar
		continueButton = QPushButton('Continue')
		continueButton.setStyleSheet('background-color : lime')
		layout.addWidget(continueButton)

		#ponemos widgets falsos de relleno		
		layout.addWidget(QWidget())		


		#lo denominamos nuestro central widget
		centralWidget = QWidget()
		centralWidget.setLayout(layout)
		centralWidget.setStyleSheet('background-color : black')
		self.setCentralWidget(centralWidget)	

		#cuando el boton sea pulsado de conectara a esta funcion
		continueButton.clicked.connect(lambda: self.__check_start_screen())

	def __check_start_screen(self):
		self.numberText = self.__enterNumber.text()
		self.timeText = self.__time.text()

		#para ver si lo introducido en la casilla es un telefono
		try:
			numberTextInt = int(self.numberText[1:])
		except:
			numberTextInt = self.numberText[1:]	
		#para ver si la hora es correcta
		try:
			timeTextInt = int(self.timeText[0:2] + self.timeText[3:])
		except:
			timeTextInt = self.timeText[0:2] + self.timeText[3:]		

		check1: bool = True
		if len(self.numberText) == 0 or self.numberText[0] != '+' or type(numberTextInt) == str:
			self.__enterNumber.setText('')
			self.__enterNumber.setStyleSheet('border : 2px solid red; background-color : white')
			self.__enterNumber.setPlaceholderText('!!INCORRECT NUMBER!!')
			check1 = False
		if len(self.timeText) != 5 or self.timeText[2] != ':' or type(timeTextInt) == str:
			self.__time.setText('')
			self.__time.setStyleSheet('border : 2px solid red; background-color : white')
			self.__time.setPlaceholderText('!!INCORRECT TIME!!')
			check1 = False
		if not self.__checkbox1.isChecked()	and not self.__checkbox2.isChecked() and not self.__checkbox3.isChecked() and not self.__checkbox4.isChecked() and not self.__checkbox5.isChecked()	and not self.__checkbox6.isChecked():
			self.__checkboxLabel.setStyleSheet('color : red; font-size : 20px')
			check1 = False

		#si cumple el checkeo pasamos a mostrar el codigo qr
		if check1:
			self.listCategories = self.get_categories()
			self.__QRcode()	

	def get_categories(self) -> List[str]:
		#esta funcion nos dará todas las categorias elegidas
		listCategories: List[str] = []
		if self.__checkbox1.isChecked():
			listCategories += [self.__checkbox1.text()]
		if self.__checkbox2.isChecked():
			listCategories += [self.__checkbox2.text()]
		if self.__checkbox3.isChecked():
			listCategories += [self.__checkbox3.text()]
		if self.__checkbox4.isChecked():
			listCategories += [self.__checkbox4.text()]
		if self.__checkbox5.isChecked():
			listCategories += [self.__checkbox5.text()]
		if self.__checkbox6.isChecked():
			listCategories += [self.__checkbox6.text()]		

		return listCategories			

def restoreInfo() -> bool:
	#here we must save and restore info of the number, if todays message has already been sent, the date of last logged in  
	return True

def main ():
	restoreInfo()

	if restoreInfo():
		app = QApplication([]) #se necesita ejecutar QApplication siempre al crear una app con Qt
								#dentro de los corchetes van los paramteros que pasamos al cmd, aqui no es nada. podriamos pasar sys.argv si quisieramos que acepatara argumentos de la linea de cmd.
		
		#creamos el fondo de pantalla de nuestra app, definimos el estilo
		stylesheet = """
	    MainWindow {
	        background-image: url("wallpaper.png"); 
	        background-repeat: no-repeat; 
	        background-position: center;
	    }
	    """
		app.setStyleSheet(stylesheet)

		#inicializamos la pantalla
		window1: MainWindow = MainWindow()
		window1.setGeometry(425, 200, 1000, 700) #posicion en la pantalla x e y, y luego su longitud y anchura
		window1.show() #por defecto se omiten los objetos, hay q poner el .show() para mostrarlo

		app.exec() #debemos poner el .exec() para que el programa siga hasta que el usuario salga de la ventana 

	stay: bool = True
	#primero cogemos la fecha de cuando se inicio la aplicacion
	current_date1 = datetime.date(datetime.now())
	timeDifference: int = 0
	while True:
		t = time.localtime()
		current_hour = time.strftime("%H", t)
		current_minute = time.strftime("%M", t)
		current_date2 = datetime.date(datetime.now())
		#si coincide con el horario elegido por el usuario, mandaremos el quote
		if int(current_hour) == int(window1.timeText[0:2])  and int(current_minute) == int(window1.timeText[3:]) and stay:
			stay = False
			#primero obtenemos las categorias
			listQuotes: List[(str, str)] = []
			for category in window1.listCategories:
				quote, author = getQuote(category.lower())
				if quote != '':
					listQuotes += [(category, quote, author)]
			#mandamos un mensaje separado para cada quote		
			for message in listQuotes:
				sendMessageTwilio('-' + message[0] + '-' + '\n' + message[2] + ':' + '\n' + message[1], window1.numberText)
			if len(listQuotes) != 0:
				sendMessageTwilio('!!!Respond to message to keep recieving quotes daily!!!', window1.numberText)	

		#cada tres dias el usuario tiene que mandar un mensaje para renovar la suscripcion
		if timeDifference != (current_date1 - current_date2).days:
			timeDifference = (current_date1 - current_date2).days
			if timeDifference % 3 == 0 and timeDifference != 0:
				sendMessageTwilio("Send the message 'join invented-outer' to renew your quote subscription", window1.numberText)

		#time.sleep(5)
		if not stay:
			time.sleep(3600)
			stay = True
		else:
			time.sleep(29)


if __name__ == '__main__': main()

#create the pyqt app where user introduces category and hour when he wants to recieve messages, we will save his info in a new pickel file if he doesnt have one or in a prestablished one if there already is one.
#will them give confirmation and who qr code, then when finished button is clicked we close the app.
#hay que mandar un mensaje al usuario cada tres dias de mandar el mensaje otra vez para renovar el sandbox.