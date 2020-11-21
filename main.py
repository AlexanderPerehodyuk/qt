import sys

from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication
from random import randint


class mWindow(QWidget):
    def __init__(self):
        super(mWindow, self).__init__()
        uic.loadUi("UI.ui", self)
        self.button.clicked.connect(self.draw)

    def draw(self):
        self.repaint()

    def paintEvent(self, a0: QPaintEvent):
        qp = QPainter(self)
        qp.begin(a0)
        qp.setBrush(Qt.yellow)
        d = randint(0, 100)
        qp.drawEllipse(randint(0, self.label.width() - d), randint(0, self.label.height() - d), d, d)
        qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = mWindow()
    ex.show()
    sys.exit(app.exec())
