import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5.QtGui import QPixmap

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.grid = QGridLayout()
        for i in range(5):
            for j in range(2):
                im = QPixmap("./img/icon.jpg")
                im = im.scaled(60, 60, aspectRatioMode = 0)
                label = QLabel()
                label.setPixmap(im)
                self.grid.addWidget(label, j, i)
        self.setLayout(self.grid)

        self.setGeometry(50,50,800,600)
        self.setWindowTitle("PyQT show image")
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())