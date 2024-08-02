from PyQt5.QtCore import pyqtSlot, QObject

class WebChannel(QObject):
    @pyqtSlot(str)
    def sendSignal(self, message):
        print(f"Received signal with message: {message}")