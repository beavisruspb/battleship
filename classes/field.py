import ship
import cell
import random

from string import ascii_lowercase
import itertools

class Field:

    cells = None

    ships = None

    blockCells = None

    def __init__(self, width, height):
        self.makeField(width, height)

        return

    # На каждые 100 ячеек:
    #    1 - 4хп
    #    2 - 3хп
    #    3 - 2хп
    #    4 - 1оп
    def placeShips(self, width, height):

        #Свободная область для корабля
        def findFreeCell(shipLong):
                
                while True:
                    direct = random.choise(["up","down","right","left"])
                    #ищем ключ
                    startPosW = random.choice(list(self.cells.keys()))
                    #ищем индекс
                    startPosH = self.cells[startPosW].index(random.choise(self.cells[startPosW]))

                    if direct == "up" and startPosH > shipLong:
                        break
                    if direct == "down" and startPosH + shipLong < len(self.cells[startPosW]):
                        break
                    if direct == "right" and 


        cellsCount = width * height
        factor = cellsCount // 100

        
        return

    #Создаем игровое поле
    def makeField(self, width, height):

        #Приватная служебная функция для правильного составления буквенных индексов
        #Возвращает list стрингов
        def __getWidhtIndex(width):

            ss = list()

            #ваще не понимаю как это работает
            def iter_all_strings():
                for size in itertools.count(1):
                    for s in itertools.product(ascii_lowercase, repeat=size):
                        yield "".join(s)


            for s in iter_all_strings():
                ss.append(s)
                if len(ss) == width:
                    break
            return ss

        self.cells = dict()
        #если адресов ячеек не передали и свойство cells объекта так же пустое то возвращает пустое игровое поле
        for a in __getWidhtIndex(width):
            bb = list()
            for b in range(1, height+1):
                icell = cell.Cell()
                bb.append(icell)
            self.cells.update( { a : bb } )

    #возвращает количество живых кораблей
    def shipsAlive(self):
        
        shipCount = 0
        #перебираем все шипы
        for ship in ships:
            if ship:
                shipCount += 1
        return shipCount

if __name__ == "__main__":
    field = Field(10,10)
    print(vars(field))
