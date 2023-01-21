import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import QtGui, QtWidgets

from UI.design import Ui_MainWindow
from UI.design_setup import Ui_DialogSetup

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.lblError.setVisible(False)
        self.ui.lneError.setVisible(False)
        self.ui.statusbar.showMessage('Я готовий')
        self.ui.pbtnOnOff.clicked.connect(self.on_clicked_onoff)
        self.ui.pbtnConnect.clicked.connect(self.on_clicked_connect)
        self.ui.pbtnSettings.clicked.connect(self.on_clicked_settings)

    def on_clicked_onoff(self):
        if self.ui.pbtnOnOff.text() == 'Увімкнути':
            self.ui.pbtnOnOff.setText('Вимкнути')
        else:
            self.ui.pbtnOnOff.setText('Увімкнути')

    def on_clicked_connect(self):
        if self.ui.pbtnConnect.text() == 'Підключено':
            self.ui.pbtnConnect.setText('Відключено')
            self.ui.lblIconConnect.setPixmap(QtGui.QPixmap('icon/checkNo.jpg'))
        else:
            self.ui.pbtnConnect.setText('Підключено')
            self.ui.lblIconConnect.setPixmap(QtGui.QPixmap('icon/checkYes.jpg'))

    def on_clicked_settings(self):
        self.ui.statusbar.showMessage('Settings')
        DialogSetup = QtWidgets.QDialog()
        ui = Ui_DialogSetup()
        ui.setupUi(DialogSetup)
        buttonClicked = DialogSetup.exec()
        if buttonClicked:
            self.ui.statusbar.showMessage('Нажали кнопку Save')
        else:
            self.ui.statusbar.showMessage('Нажали кнопку Cancel')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
