from classes.ship import Ship
from classes.cell import Cell
import random

from string import ascii_lowercase
import itertools

class Field:

    cells = dict()

    ships = list()

    def __init__(self, width = 10, height = 10):
        self.makeField(width, height)
        self.placeShips(width, height)
        return


    #Служебная функция для правильного составления буквенных индексов
    #Возвращает list стрингов
    def __getWidhtIndex(self, width):

        ss = list()

        #ваще не понимаю как это работает
        def iter_all_strings():
            for size in itertools.count(1):
                for s in itertools.product(ascii_lowercase, repeat=size):
                    # join собирает содержиме итерируемого объекта s в строку
                    yield "".join(s)


        for s in iter_all_strings():
            ss.append(s)
            if len(ss) == width:
                break
        return ss

    #Размещаем корабль на поле
    def __placeOneShip(self, shipLong, width, height):

        ##print("Длина корабля {}. Пробуем разместить его на поле размером {}x{}".format(shipLong, width, height))

        indexList = self.__getWidhtIndex(width)

        #Цикл выбора начальной позиции
        while True:

            #Выбираем ориентацию шипа
            direct = random.choice(["down", "right"])
            #direct = "down"
            #direct = "right"
            #Выбираем ключ
            startPosW = random.choice(indexList)
            #Выбираем индекс
            startPosH = random.randint(0, height - 1)

            #если  вниз и начальная точка + длина меньше высоты
            if direct == "down" and startPosH + shipLong - 1 < height:                            
            
                
                #индекс конечной точки корабля
                endSlicePosH = startPosH + shipLong

                if startPosH == 0:
                    startSlicePosH = 0
                else: 
                    startSlicePosH = startPosH - 1
                if startPosH + shipLong < height:
                    endSlicePosH += 1


                region = list()

                #Лист срезов от начальной точки до начальной точки + длина шипа
                #Ячейки шипа и вокруг него
                region.append(self.cells.get(startPosW) [ startSlicePosH  : endSlicePosH])
                #если ключ не является первым
                if indexList.index(startPosW) != 0:
                    #добалвяем срез левого столбца
                    region.append(self.cells.get(indexList [indexList.index(startPosW) - 1] ) [ startSlicePosH  : endSlicePosH])
                #если ключ не является последним
                if indexList.index(startPosW) < len(indexList) - 1:
                    #Добавляем срез справа от корабля
                    region.append(self.cells.get(indexList [indexList.index(startPosW) + 1]) [ startSlicePosH  : endSlicePosH])
                
                blockCell = False
                for cell in self.cells.get(indexList [indexList.index(startPosW)]) [ startPosH  : startPosH + shipLong ]:
                    if cell.block:
                        blockCell = True
                        break
                if not blockCell:
                    break

            #если  вправо и индекс начальной точки + длина шипа меньше количества элементов в листе с числовыми ключами
            if direct == "right" and indexList.index(startPosW) + shipLong - 1 < len(indexList):

                region = list()

                #индекс ячейки над кораблем
                if startPosH > 0:
                    startSlicePosH = startPosH - 1
                    endSlicePosH = startSlicePosH + 3                 
                else:
                    startSlicePosH = 0
                    endSlicePosH = startSlicePosH + 2

                #если стартовый столбец не первый тогда
                if indexList.index(startPosW) > 0:
                    #берем срез из 3 ячеек предстощего столбца
                    region.append(self.cells.get( indexList [ indexList.index(startPosW) - 1 ] )[ startSlicePosH : endSlicePosH ])
                    #print("Выбран столбец с ключем {} и ячейки с индексами {}-{}".format(indexList [ indexList.index(startPosW) - 1 ], startSlicePosH, endSlicePosH))

                #если последняя ячейка корабля не упирается в стенку
                if indexList.index(startPosW) + shipLong < len(indexList):
                    #берем столбец за кораблем
                    region.append(self.cells.get( indexList [ indexList.index(startPosW) + shipLong ] )[ startSlicePosH : endSlicePosH ])
                    #print("Выбран столбец с ключем {} и ячейки с индексами {}-{}".format(indexList [ indexList.index(startPosW) + shipLong ], startSlicePosH, endSlicePosH))

                #Проходим по всей длине шипа
                for i in range(shipLong):
                    #берем срез из 3 ячеек для каждого столбка корабля
                    region.append(self.cells.get( indexList [ indexList.index(startPosW) + i ] )[ startSlicePosH : endSlicePosH ])
                    #print("Выбран столбец с ключем {} и ячейки с индексами {}-{}".format(indexList [ indexList.index(startPosW) + i ], startSlicePosH, endSlicePosH))
                
                blockCell = False
                cellsList = list()
                for i in range(shipLong):
                    if blockCell:
                        break
                    for cell in self.cells.get( indexList [ indexList.index(startPosW) + i ] )[ startPosH : startPosH + 1 ]:
                        if cell.block:
                            blockCell = True
                            break
                
                if not blockCell:
                    break

        for column in region:
            if column:
                for cell in column:
                    cell.block = True

        #print ( "Для шипа длиной {} палуб(а\ы) выбрана начальная позиция с координатами {}{} и направлением  {}".format( shipLong, startPosW, startPosH + 1, direct) )

        ship = Ship() 
        cellsShip = list()

        #если корабль строится вниз
        if direct == "down":
            for cell in self.cells.get(startPosW)[ startPosH : startPosH + shipLong]:
                cell.setShip(ship)
                cellsShip.append(cell)
            ship.cells = cellsShip

        if direct == "right":
            for i in range(shipLong):
                self.cells.get( indexList [ indexList.index(startPosW) + i ] )[startPosH].setShip(ship)
                cellsShip.append(self.cells.get( indexList [ indexList.index(startPosW) + i ] )[startPosH])
            ship.setCells(cellsShip)
        
        ##print("Ячейки шипа {}", ship.cells)
        ##print("Добавляем к селф.шипс наш шип", ship)
        self.ships.append(ship)

    # На каждые 100 ячеек:
    #    1 - 4хп
    #    2 - 3хп
    #    3 - 2хп
    #    4 - 1оп
    def placeShips(self, width, height):

        #========================================================#
        #   Вариант предложенный Денисом                         #
        #========================================================#

        #определяем количество ячеек занятых клетками кораблей
        num_cells_ship = width * height // 5
        if width * height % 5 > 0:
            num_cells_ship += 1

        #Собираем клетки кораблей в корабли. Согласно классическому виду игры - это пирамида, где колличество одиночных кораблей
        #равно длине самого крупного корабля

        #словарь в котором индекс это количество палуб, а значение - количество кораблей данного типа
        ships = {}
        i, size = 1, 0
        while True :
            size += i
            if num_cells_ship < size:
                break      
            num_cells_ship -= size       
            i += 1

        #Собираем начальную пирамидку кораблей
        for j in range(i-1):
            ships.update({ i-j-1 : j+1 })

        #Сортируем оставшиеся клетки кораблей не уложившиеся в классическую пирамиду
        if num_cells_ship >= i  and (num_cells_ship > size//2):
            num_cells_ship -= i
            ships.update({ i : 1 })

        for j in range(i-1):
            if num_cells_ship >= i-j-1:
                num_cells_ship -= i-j-1
                ships[i-j-1] += 1
        
        #========================================================#
        #========================================================#

        for i,v in ships.items():
            for a in range(v):
                self.__placeOneShip(i, width, height)
        return
        

    #Создаем игровое поле
    def makeField(self, width, height):

        if width < 10:
            width = 10
        if height < 10:
            height = 10

        #если адресов ячеек не передали и свойство cells объекта так же пустое то возвращает пустое игровое поле
        for a in self.__getWidhtIndex(width):
            bb = list()
            for b in range(1, height+1):
                icell = Cell()
                bb.append(icell)
            self.cells.update( { a : bb } )

    #возвращает количество живых кораблей
    def shipsAlive(self):
        
        shipCount = 0
        #перебираем все шипы
        for ship in self.ships:
            if ship.isAlive():
                shipCount += 1
        return shipCount

if __name__ == "__main__":
    field = Field(100,200)
    print("Живых кораблей {}".format(field.shipsAlive()))
    exit()