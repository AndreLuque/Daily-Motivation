
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
	
		layout = QVBoxLayout()
				
		title = QLabel('Let´s Start')
		title.setStyleSheet('color : white; font-size : 50px; font-weight: bold')		
		layout.addWidget(title)
				
		#dejamos un hueco para introducir el email
		self.enterNumber = QLineEdit(placeholderText = 'Enter Whatsapp Phone Number (Example: +34633890056)')
		self.enterNumber.setStyleSheet('background-color : white; color : black')
		layout.addWidget(self.enterNumber)

		self.time = QLineEdit(placeholderText = 'At what time do you want to recieve the quotes? (Example: 12:42)')
		self.time.setStyleSheet('background-color : white; color : black')
		layout.addWidget(self.time)

		checkboxLabel = QLabel('Select Categories that you are interested in:')
		checkboxLabel.setStyleSheet('color : white; font-size : 20px')
		layout.addWidget(checkboxLabel)


		sublayout1 = QHBoxLayout()

		checkbox1 = QCheckBox('Inspirational')
		checkbox1.setStyleSheet('color : white')
		sublayout1.addWidget(checkbox1)
		checkbox2 = QCheckBox('Sports')
		checkbox2.setStyleSheet('color : white')
		sublayout1.addWidget(checkbox2)
		checkbox3 = QCheckBox('Love')
		checkbox3.setStyleSheet('color : white')
		sublayout1.addWidget(checkbox3)
		layout.addLayout(sublayout1)

		sublayout2 = QHBoxLayout()

		checkbox4 = QCheckBox('Life')
		checkbox4.setStyleSheet('color : white')
		sublayout2.addWidget(checkbox4)
		checkbox5 = QCheckBox('Funny')
		checkbox5.setStyleSheet('color : white')
		sublayout2.addWidget(checkbox5)
		checkbox6 = QCheckBox('Students')
		checkbox6.setStyleSheet('color : white')
		sublayout2.addWidget(checkbox6)
		layout.addLayout(sublayout2)

		layout.addWidget(QWidget())		
		layout.addWidget(QWidget())		


		#lo denominamos nuestro central widget
		centralWidget = QWidget()
		centralWidget.setLayout(layout)
		centralWidget.setStyleSheet('background-color : black')
		self.setCentralWidget(centralWidget)	

		#cuando el boton sea pulsado de conectara a esta funcion
		login.clicked.connect(lambda: self.__QRcode())	


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