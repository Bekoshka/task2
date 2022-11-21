import sys

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import randint


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Рисование')
        self.do_paint = False
        self.btn.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circles(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_circles(self, qp):
        qp.setBrush(QColor(255, 0, 0))
        qp.drawEllipse(30, 30, 200)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
