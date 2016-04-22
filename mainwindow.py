import sys
from mainwindow_ui import Ui_MainWindow
from popup_ui import Ui_Dialog
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QSpinBox, QWidget, QDialog



class mainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(mainWindow, self).__init__()
        self.setupUi(self)
        self.pushButton_schreib_was.clicked.connect(self.shreib_endlich_was)
        self.pushButton_clear.clicked.connect(self.clear)
        self.spinBox.valueChanged.connect(self.spinbox_value)
        self.label.setText('Hallo 0')

    def shreib_endlich_was(self):
        self.textBrowser.setPlainText('Hallo Uli!')

    def spinbox_value(self):
        val = str(self.spinBox.value())
        self.label.setText('Hallo ' + val)

    def clear(self): 
        app = QApplication(sys.argv)
        form = popup()
        form.show()

