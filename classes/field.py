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


    def checkBlockCell(self, width, height, rotate, startPosW, startPosH, shipLong):

        block = False

        indexList = self.__getWidhtIndex(width)

        if rotate == "up" or rotate == "down":
            #если индекс w равен 0
            if indexList.index(startPosW) == 0:
                #только строка с и та что под ней
                listCellList = [self.cells[indexList.index(startPosW)], self.cells[indexList.index(startPosW) + 1]]
            #если индекс равен последнему в списке    
            elif indexList.index(startPosW) == len(indexList) - 1:
                #только строка сверху и сама строка индекса
                listCellList = [self.cells[indexList.index(startPosW - 1 )], self.cells[indexList.index(startPosW)]]
            else:
                #все 3 строки
                listCellList = [self.cells[indexList.index(startPosW - 1 )], self.cells[indexList.index(startPosW)], self.cells[indexList.index(startPosW) + 1]]

            for cellList in listCellList:
                if not block:
                    for cell in cellList:
                        if cell.block:
                            block = True
                            break
                else:
                    break
            return block
        else:



    # На каждые 100 ячеек:
    #    1 - 4хп
    #    2 - 3хп
    #    3 - 2хп
    #    4 - 1оп
    def placeShips(self, width, height):

        #Свободная область для корабля
        def findFreeCell(shipLong):
                
                indexList = self.__getWidhtIndex(width)
                while True:

                    while True:
                        direct = random.choise(["up","down","right","left"])
                        #ищем ключ
                        startPosW = random.choice(list(self.cells.keys()))
                        #ищем индекс
                        startPosH = self.cells[startPosW].index(random.choise(self.cells[startPosW]))

                        block = False
                        #если  вверх и начальная точка больше дилны шипа
                        if direct == "up" and startPosH > shipLong:                            

                            if not block:
                                break

                        #если  вниз и начальная точка плюс длина шипа меньше длины листа
                        if direct == "down" and startPosH + shipLong < len(self.cells[startPosW]):
                            
                            for cellList in [self.cells[indexList.index(startPosW- 1 )], self.cells[indexList.index(startPosW- 1 )], self.cells[indexList.index(startPosW- 1 )]]:
                                if not block:
                                    for cell in cellList:
                                        if cell.block:
                                            block = True
                                            break
                                else:
                                    break

                            if not block:
                                break
                        #если  вправо и индекс начальной точки + длина шипа меньше количества элементов в листе с числовыми ключами
                        if direct == "right" and indexList.index(startPosW) + shipLong < len(indexList):
                            break
                        #если  влево и индекс начальной точки больше дилны корабля
                        if dict == "left" and indexList.index(startPosW) > shipLong:
                            break
                    


        cellsCount = width * height
        factor = cellsCount // 100

        
        return

    #Создаем игровое поле
    def makeField(self, width, height):

        if width < 10:
            width = 10
        if height < 10:
            height = 10

        self.cells = dict()
        #если адресов ячеек не передали и свойство cells объекта так же пустое то возвращает пустое игровое поле
        for a in self.__getWidhtIndex(width):
            bb = list()
            for b in range(1, height+1):
                icell = cell.Cell()
                bb.append(icell)
            self.cells.update( { a : bb } )

    #возвращает количество живых кораблей
    def shipsAlive(self):
        
        shipCount = 0
        #перебираем все шипы
        for ship in self.ships:
            if ship:
                shipCount += 1
        return shipCount

    #Приватная служебная функция для правильного составления буквенных индексов
    #Возвращает list стрингов
    def __getWidhtIndex(self, width):

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

if __name__ == "__main__":
    field = Field(10,10)
    print(vars(field))
