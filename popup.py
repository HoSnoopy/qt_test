from popup_ui import Ui_Dialog
from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit, QSpinBox, QWidget, QDialog


class popup(QDialog, Ui_Dialog):
    def __init__(self):
        super(popup, self).__init__()
        self.setupUi(self)
        self.pushButton_okidoki.clicked.connect(self.exit)


