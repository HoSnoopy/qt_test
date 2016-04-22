import sys
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QSpinBox
from mainwindow import mainWindow

def main():

    app = QApplication(sys.argv)
    form = mainWindow()
    form.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
