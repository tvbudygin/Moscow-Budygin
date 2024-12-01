from random import randrange
import sys
from PyQt6.QtGui import QPainter, QColor
from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QApplication


def main():
    print("Гит в Пайчарме")
    print("add")
    print("add")
    print(1)
    print(2)
    print(12345)


if __name__ == '__main__':
    main()


class Circle(QMainWindow):
    def __init__(self):
        super(Circle, self).__init__()
        uic.loadUi('UI.ui', self)
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()
        self.do_paint = False

    def draw_circle(self, qp):
        qp.setPen(QColor(255, 255, 0))
        a = randrange(1, 600)
        qp.drawEllipse(10, 10, a, a)

    def paint(self):
        self.do_paint = True
        self.update()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Circle()
    form.show()
    sys.exit(app.exec())
