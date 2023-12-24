import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QIntValidator

from CSVManager import CSVManager

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1150, 670)
        MainWindow.setMinimumSize(QtCore.QSize(1250, 670))
        MainWindow.setMaximumSize(QtCore.QSize(1250, 670))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        

        self.picture = QtWidgets.QLabel(parent=self.centralwidget)
        self.picture.setGeometry(QtCore.QRect(0, 0, 921, 671))
        self.picture.setText("")
        self.picture.setPixmap(QtGui.QPixmap("periodic.png"))
        self.picture.setScaledContents(True)
        self.picture.setObjectName("picture")
        

        self.inputLine = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.inputLine.setGeometry(QtCore.QRect(1050, 50, 75, 40))
        self.inputLine.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.inputLine.setObjectName("inputLine")
        
        self.inputLine.setMaxLength(3)
        int_validator = QIntValidator(1, 118)
        self.inputLine.setValidator(int_validator)
        

        self.outputLine = QtWidgets.QLabel(parent=self.centralwidget)
        self.outputLine.setGeometry(QtCore.QRect(940, 170, 300, 391))
        self.outputLine.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.outputLine.setText("Enter the element number")
        self.outputLine.setObjectName("outputLine")
        
        

        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1050, 110, 75, 23))
        self.pushButton.setText("Check")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.show_element_data)

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.csv_manager = CSVManager()
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Mendeleev Table"))

    def show_element_data(self):
        if self.inputLine.text() != '':
            if int(self.inputLine.text()) in range(1, 119):
                self.outputLine.setText(self.csv_manager.get_data_by_id(int(self.inputLine.text())))
            else:
                self.outputLine.setText("Enter the element number")
        else:
            self.outputLine.setText("Enter the element number")
            
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
