import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import QtGui
from UI.MQTT_design import Ui_MainWindow

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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
