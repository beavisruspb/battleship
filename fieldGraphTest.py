import sys
from classes.field import Field

def main():
    #Количество ячеек в филде
    width = 20
    height = 20
    #создаем объект класса филд
    field = Field(width,height)
    #пробуем загрузить зависимости
    try:
        from PyQt5.QtWidgets import QApplication
    except ImportError:
        #если с зависимостями голяк пробуем выполниться с библиотекой tkinter
        tkmods(field)
    #вызываем функцию отрисовки c использование pyqt
    qt(field)

def qt(field):

    from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QGridLayout, QLineEdit)
    from PyQt5.QtGui import QIcon, QPixmap, QColor

    class GameField(QWidget):

        width = len(field.cells)
        height = len(field.cells.get('a'))
        scale = 0.85
        pixW = 1100
        pixH = 950

        sizeCellW = round((pixW // width) * scale)
        sizeCellH = round((pixH // height) * scale)

        def __init__(self, field):
            super().__init__()
            self.initUI(field, self.sizeCellW, self.sizeCellH)

        def initUI(self, field, sizeCellW, sizeCellH):
            self.setGeometry(100, 60, self.pixW, self.pixH)
            self.setWindowTitle("BattleShip - field class graphic test")
            self.setWindowIcon(QIcon("img/icon.ico"))

            grid = QGridLayout(self)
            
            column = 2
            for key in field.cells.keys():
                label = QLabel(self)
                label.setText(key)
                grid.addWidget(label, 1, column)
                column += 1
            
            row = 2
            for i in range(len(field.cells.get('a'))):
                label = QLabel(self)
                label.setText(str(i + 1))
                grid.addWidget(label, row, 1)
                row += 1

            column = 2
            for key,val in field.cells.items():
                row = 2
                for cell in val:
                    if cell.ship:
                        pixmap = QPixmap("./img/icon.jpg")
                        pixmap = pixmap.scaled(sizeCellW, sizeCellH)
                        imgLabel = QLabel(self)
                        imgLabel.setPixmap(pixmap)
                    elif cell.block:
                        pixmap = QPixmap("./img/wavey.png")
                        pixmap = pixmap.scaled(sizeCellW, sizeCellH)
                        imgLabel = QLabel(self)
                        imgLabel.setPixmap(pixmap)
                    else:
                        pixmap = QPixmap("./img/waveb.png")
                        pixmap = pixmap.scaled(sizeCellW, sizeCellH)
                        imgLabel = QLabel(self)
                        imgLabel.setPixmap(pixmap)
                    grid.addWidget(imgLabel, row, column)
                    row += 1
                column += 1
            
            self.setLayout(grid)
            self.show()
    
    app = QApplication(sys.argv)
    qt = GameField(field)
    sys.exit(app.exec_())

def tkmods(field):

    try:
        import tkinter as tk
    except ImportError:
        print("\n Полный голяк с зависимостями.\nНаверно нам стоит расстаться\nОт себя могу лишь порекомендовать попробовать переустановить интерпритатор с официального сайта.")
        exit()

    class App(tk.Tk):
        def __init__(self):
            super().__init__()

            self.protocol("WM_DELETE_WINDOW", self.window_close)

            self.label1 = tk.Label(self, text = "Не установлены необходимые зависимости. Продолжить с библиотекой tkinter?", font="Arial 18", fg="#eee", bg="#333")
            self.label1.pack()
            self.label2 = tk.Label(self, text = "Для установки зависимостей нажми нет, выполни команду в консоли: \"pip install -r requirements.txt\" и возвращайся", font="Arial 14")
            self.label2.pack()
            self.button1 = tk.Button(text = "Yes", bg = "red", foreground = "yellow", font = "24", width = 25,
                    command=self.clickYes
                )
            self.button1.place(relx = 0.25, rely = 0.5)
            self.button2 = tk.Button(text = "No", bg = "yellow", foreground = "red", font = "24", width = 25,
                    command=self.window_close
                )
            self.button2.place(relx = 0.75, rely = 0.5, )

        def clickYes(self):           
            self.destroy()
            self.quit()

        def window_close(self):
            self.destroy()
            self.quit()
            exit()

    class GameField(tk.Tk):
        
        def __init__(self, field):

            width = len(field.cells)
            height = len(field.cells.get('a'))
            scale = 0.75
            pixW = 1100
            pixH = 950

            sizeCellW = round (pixW // width) * scale
            sizeCellH = round (pixH // height) * scale

            super().__init__()

            self.protocol("WM_DELETE_WINDOW", self.window_close)

            self.frame = tk.Frame(self)

            self.frame.grid()
            
            column = 2
            for key in field.cells.keys():
                self.label = tk.Label(self.frame, text = key).grid(column = column, row = 1)
                column += 1

            row = 2
            for i in range(len(field.cells.get('a'))):
                self.label = tk.Label(self.frame, text = i + 1).grid(column = 1, row = row)
                row += 1

            column = 2
            for key,val in field.cells.items():
                row = 2
                for cell in val:
                    if cell.ship:
                        bgColor = "black"
                    elif cell.block:
                        bgColor = "yellow"
                    else:
                        bgColor = "white"
                    self.canvas = tk.Canvas(self.frame, background = bgColor, height = sizeCellH, width = sizeCellW).grid(column = column , row = row)
                    row += 1
                column += 1

        def window_close(self):
            self.destroy()
            self.quit()
            exit()


    pixW = 1100
    pixH = 950

    app = App()
    app.title("BattleShip - field class graphic test")
    app.geometry("{}x{}".format(pixW, pixH))
    app.resizable(True, True) #разрешить изменение высоты и ширины окна
    app.iconbitmap('img/icon.ico')
    app.mainloop()

    app = GameField(field)
    app.title("BattleShip - field class graphic test")
    app.geometry("{}x{}".format(pixW, pixH))
    app.resizable(True, True) #разрешить изменение высоты и ширины окна
    app.iconbitmap('img/icon.ico')
    app.mainloop()

if __name__ == "__main__":
    main()