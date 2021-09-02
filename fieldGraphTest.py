from tkinter import *
from classes.field import Field
width = 50
height = 35 
pixW = 1100
pixH = 950
scale = 0.75

def window_close():
    root.destroy()
    root.quit()

if __name__ == "__main__":
    sizeCellW = pixW // width
    sizeCellH = pixH // height
    field = Field(width,height)

    root = Tk()
    root.protocol('WM_DELETE_WINDOW', window_close)
    root.geometry("{}x{}".format(pixW, pixH))
    root.resizable(True, True) #разрешить изменение высоты и ширины окна
    root.iconbitmap('img/icon.ico')
    root.title("BattleShip - field class graphic test")

    #создаем рабочую область
    frame = Frame(root)
    frame.grid()
    
    column = 2
    for key in field.cells.keys():
        l = Label(frame, text = key).grid(column = column, row = 1)
        column += 1

    row = 2
    for i in range(len(field.cells.get('a'))):
        l = Label(frame, text = i + 1).grid(column = 1, row = row)
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
            c = Canvas(frame, background = bgColor, height = sizeCellH*scale, width = sizeCellW*scale).grid(column = column , row = row)
            row += 1
        column += 1

    root.mainloop()
