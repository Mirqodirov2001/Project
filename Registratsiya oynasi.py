from PyQt5.QtGui import*
from PyQt5.QtCore import*
from PyQt5.QtWidgets import*
import sys
import os

class Window(QDialog):

	def __init__(self):
		super(Window, self).__init__()

		self.setWindowTitle("Python")

		self.setGeometry(100, 100, 300, 400)

		self.formGroupBox = QGroupBox("Sign up")
		self.ageSpinBar = QSpinBox()

		self.residenceComboBox = QComboBox()
		self.residenceComboBox.addItems(["UZBEKISTAN", "QOZOG'ISTON", "QIRG'IZISTON","AVG'ONISTON","TOJIKISTON","TURKMANISTON"])

		self.nameLineEdit = QLineEdit()

		self.createForm()

		self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)

		self.buttonBox.accepted.connect(self.getInfo)

		self.buttonBox.rejected.connect(self.reject)

		mainLayout = QVBoxLayout()

		mainLayout.addWidget(self.formGroupBox)

		mainLayout.addWidget(self.buttonBox)
		self.setLayout(mainLayout)

	
	def getInfo(self):

		print("Person Name : {0}".format(self.nameLineEdit.text()))
		print("Residence : {0}".format(self.residenceComboBox.currentText()))
		print("Age : {0}".format(self.ageSpinBar.text()))

		self.close()


	def createForm(self):

		layout = QFormLayout()
		layout.addRow(QLabel("Name"), self.nameLineEdit)
		layout.addRow(QLabel("Residence"), self.residenceComboBox)
		layout.addRow(QLabel("Age"), self.ageSpinBar)
		self.formGroupBox.setLayout(layout)



if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = Window()
	window.show()
	sys.exit(app.exec_())
