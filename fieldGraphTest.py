from tkinter import *
from classes.field import Field
width = 50
height = 35 

def window_close():
    root.destroy()
    root.quit()

if __name__ == "__main__":
    sizeCellW = 1000 // width
    sizeCellH = 800 // height
    field = Field(width,height)

    root = Tk()
    root.protocol('WM_DELETE_WINDOW', window_close)
    root.geometry("1000x800")
    root.resizable(True, True) #разрешить изменение высоты и ширины окна

    #создаем рабочую область
    frame = Frame(root)
    frame.grid()
    
    rowCount = 0
    for key,val in field.cells.items():
        rowCount += 1  
        columnCount = 0
        for cell in val:
            columnCount += 1
            if cell.ship:
                bgColor = "black"
            elif cell.block:
                bgColor = "yellow"
            else:
                bgColor = "white"
            c = Canvas(frame, background = bgColor, height = sizeCellH*0.8, width = sizeCellW*0.8).grid(column = rowCount , row = columnCount)

    root.mainloop()
