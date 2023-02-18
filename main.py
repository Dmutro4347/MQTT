import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import QtGui, QtWidgets
import mqtt.PyMQTT as mqtt
from UI.design import Ui_MainWindow
from UI.design_setup import Ui_DialogSetup


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.lblError.setVisible(False)
        self.ui.lneError.setVisible(False)
        # self.ui.statusbar.showMessage('Я готовий')
        self.ui.pbtnOnOff.clicked.connect(self.on_clicked_onoff)
        self.ui.pbtnConnect.clicked.connect(self.on_clicked_connect)
        self.ui.pbtnSettings.clicked.connect(self.on_clicked_settings)
        self.ui.pbtnOnOff.setEnabled(False)
        # self.ui.lcdTemperature()
        # self.ui.lcdPressure()
        # self.ui.lcdLuminocity()

    def on_clicked_onoff(self):
        if self.ui.pbtnOnOff.text() == 'Увімкнути':
            self.ui.pbtnOnOff.setText('Вимкнути')
            if mqtt.publish_massage_mqtt('python/LED', '1') == 0:
                self.ui.statusbar.showMessage('Send on to topic python/LED')
            else:
                self.ui.statusbar.showMessage('Failed to send massage to topic')
        else:
            self.ui.pbtnOnOff.setText('Увімкнути')
            if mqtt.publish_massage_mqtt('python/LED', '0') == 0:
                self.ui.statusbar.showMessage('Send on to topic python/LED')
            else:
                self.ui.statusbar.showMessage('Failed to send massage to topic')

    def on_clicked_connect(self):
        if self.ui.pbtnConnect.text() == 'Підключити':
            self.ui.pbtnConnect.setText('Відключити')
            self.ui.lblIconConnect.setPixmap(QtGui.QPixmap('icon/checkNo.jpg'))
            mqtt.connect_mqtt()
            self.ui.pbtnOnOff.setEnabled(True)
            mqtt.subscribe(('sensor/temperature', 'sensor/luminocity', 'sensor/pressure'), self.foo)

        else:
            self.ui.pbtnConnect.setText('Підключити')
            self.ui.lblIconConnect.setPixmap(QtGui.QPixmap('icon/checkYes.jpg'))
            mqtt.disconnect_mqtt()
            self.ui.pbtnOnOff.setEnabled(False)

    def on_clicked_settings(self):
        self.ui.statusbar.showMessage('Settings')
        DialogSetup = QtWidgets.QDialog()
        ui = Ui_DialogSetup()
        ui.lneBroker.setText(mqtt.mqtt_connect['broker'])
        ui.setupUi(DialogSetup)
        buttonClicked = DialogSetup.exec()
        if buttonClicked:
            self.ui.statusbar.showMessage('Нажали кнопку Save')
        else:
            self.ui.statusbar.showMessage('Нажали кнопку Cancel')

    def foo(self, var1, var2):
        print(f"got massage {var2} - {var1}")
        if var2 == 'temperature':
            self.ui.lcdTemperature.display(var1)
        elif var2 == 'luminocity':
            self.ui.lcdLuminocity.display(var1)
        elif var2 == 'pressure':
            self.ui.lcdPressure.display(var1)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
