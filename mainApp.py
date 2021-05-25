
import time
from getQuoteAPI import getQuote
from sendMessageTwilio import sendMessageTwilio
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QMessageBox, QGridLayout, QMainWindow, QStatusBar, QToolBar, QAction, QLineEdit, QComboBox, QHBoxLayout, QVBoxLayout, QTableWidget, QTableWidgetItem, QHeaderView, QCheckBox
from PyQt5.QtGui import QFont, QPixmap
from PyQt5 import QtCore
import pickle
from typing import List, TypeVar, NoReturn
import datetime

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
		pass	

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
		self.enterNumber = QLineEdit(placeholderText = 'Enter Whatsapp Phone Number (Example: +34633890056)')
		self.enterNumber.setStyleSheet('background-color : white; color : black')
		layout.addWidget(self.enterNumber)

		#dejamos un hueco para introducir la hora
		self.time = QLineEdit(placeholderText = 'At what time do you want to recieve the quotes? (Example: 12:42)')
		self.time.setStyleSheet('background-color : white; color : black')
		self.time.setMaxLength(5)
		layout.addWidget(self.time)

		self.__checkboxLabel = QLabel('Select Categories that you are interested in:')
		self.__checkboxLabel.setStyleSheet('color : white; font-size : 20px')
		layout.addWidget(self.__checkboxLabel)

		sublayout1 = QHBoxLayout()

		#el usuario pulsara en las cajas que cumple su preferencia
		self.__checkbox1 = QCheckBox('Inspirational')
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
		numberText = self.enterNumber.text()
		timeText = self.time.text()

		#para ver si lo introducido en la casilla es un telefono
		try:
			numberTextInt = int(numberText[1:])
		except:
			numberTextInt = numberText[1:]	
		#para ver si la hora es correcta
		try:
			timeTextInt = int(timeText[0:2] + timeText[3:])
		except:
			timeTextInt = timeText[0:2] + timeText[3:]		

		check1: bool = True
		if len(numberText) == 0 or numberText[0] != '+' or type(numberTextInt) == str:
			self.enterNumber.setText('')
			self.enterNumber.setStyleSheet('border : 2px solid red; background-color : white')
			self.enterNumber.setPlaceholderText('!!INCORRECT NUMBER!!')
			check1 = False
		if len(timeText) != 5 or timeText[2] != ':' or type(timeTextInt) == str:
			self.time.setText('')
			self.time.setStyleSheet('border : 2px solid red; background-color : white')
			self.time.setPlaceholderText('!!INCORRECT TIME!!')
			check1 = False
		if not self.__checkbox1.isChecked()	and not self.__checkbox2.isChecked() and not self.__checkbox3.isChecked() and not self.__checkbox4.isChecked() and not self.__checkbox5.isChecked()	and not self.__checkbox6.isChecked():
			self.__checkboxLabel.setStyleSheet('color : red; font-size : 20px')
			check1 = False

		#si cumple el checkeo pasamos a mostrar el codigo qr
		if check1:
			self.__QRcode()	





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
	while True:
		t = time.localtime()
		current_hour = time.strftime("%H", t)
		current_minute = time.strftime("%M", t)
		current_date = time.strftime("%d%m%Y", t)
		if int(current_hour) >= 13  and int(current_minute) >= 53 and stay:
			stay = False
			print('sent message')

		time.sleep(5)
		#if not stay:
		#	time.sleep(82800)
		#else:
		#	time.sleep(29)


if __name__ == '__main__': main()

#create the pyqt app where user introduces category and hour when he wants to recieve messages, we will save his info in a new pickel file if he doesnt have one or in a prestablished one if there already is one.
#will them give confirmation and who qr code, then when finished button is clicked we close the app.
#hay que mandar un mensaje al usuario cada tres dias de mandar el mensaje otra vez para renovar el sandbox.