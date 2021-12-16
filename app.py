import sys
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QMainWindow
from PyQt5.QtGui import QPixmap, QCursor


class Window(QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("Image to PDF")
        self.setFixedSize(1200, 800)

        self.setStyleSheet(
            """
            background: yellow;
            color: black;
            font-weight: 500;
            font-size: 16px;
            """
        )

        self.label = QLabel(self)
        self.label.setText("Hello World")

        self.show()


app = QApplication(sys.argv)
window = Window()

sys.exit(app.exec())
