import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6 import uic
from drowsiness_detection import detector_cam


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("app.ui", self)
        self.cw = self.centralWidget()
        self.label_status = self.cw.findChild(QtWidgets.QLabel, "label_status")
        self.btn_launch = self.cw.findChild(QtWidgets.QPushButton, "launchBtn")
        self.btn_launch.clicked.connect(self.launch)
        self.btn_exit = self.cw.findChild(QtWidgets.QPushButton, "exitBtn")
        self.btn_exit.clicked.connect(self.close)

    def launch(self):
        self.label_status.setText("Running")
        detector_cam()

    def close(self):
        self.label_status.setText("Stopped")
        sys.exit()

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()