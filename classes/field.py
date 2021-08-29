from ship import Ship
from cell import Cell
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


    def __checkBlockCells(self, region):
        for column in region:
            if column:
                for cell in column:
                    if cell.block:
                        return True
        return False

    #Размещаем корабль на поле
    def __placeOneShip(self, shipLong, width, height):

        print("Длина корабля {}. Пробуем разместить его на поле размером {}x{}".format(shipLong, width, height))

        indexList = self.__getWidhtIndex(width)

        #Цикл выбора начальной позиции
        while True:

            #Выбираем ориентацию шипа
            direct = random.choice(["down", "right"])
            #Выбираем ключ
            startPosW = random.choice(indexList)
            #Выбираем индекс
            startPosH = random.randint(0, height - 1)

            #если  вниз и начальная точка + длина меньше высоты
            if direct == "down" and startPosH + shipLong <= height:                            
                region = list()
                #Лист срезов от начальной точки до начальной точки + длина шипа
                #Ячейки шипа и вокруг него
                region.append(self.cells.get(startPosW) [ startPosH  : startPosH + shipLong])
                if indexList.index(startPosW) != 0:
                    region.append(self.cells.get(indexList [indexList.index(startPosW) - 1] ) [ startPosH  : startPosH + shipLong])
                if indexList.index(startPosW) < len(indexList) - 1:
                    region.append(self.cells.get(indexList [indexList.index(startPosW) + 1]) [ startPosH  : startPosH + shipLong])
                
                #Если в указанной области нет заблокированных ячеек
                if not self.__checkBlockCells(region):
                    #Выходим из цикла выбора начальной позиции
                    break

            #если  вправо и индекс начальной точки + длина шипа меньше количества элементов в листе с числовыми ключами
            if direct == "right" and indexList.index(startPosW) + shipLong <= len(indexList):
                region = list()
                #Проходим по всей длине шипа
                for i in range(shipLong):
                    #берем срез из 3 ячеек
                    region.append(self.cells.get( indexList [ indexList.index(startPosW) + i ] )[startPosH : startPosH + 3])
                
                #Если в указанной области нет заблокированных ячеек
                if not self.__checkBlockCells(region):
                    #Выходим из цикла выбора начальной позиции
                    break

        for column in region:
            if column:
                for cell in column:
                    cell.block = True

        print ( "Для шипа длиной {} палуб(а\ы) выбрана начальная позиция с координатами {}{} и направлением  {}".format( shipLong, startPosW, startPosH + 1, direct) )

        ship = Ship() 
        cellsShip = list()
        if direct == "down":
            for cell in self.cells.get(startPosW)[startPosH : startPosH + shipLong]:
                cell.setShip(ship)
                cellsShip.append(cell)
            ship.cells = cellsShip
        if direct == "right":
            for i in range(shipLong):
                self.cells.get( indexList [ indexList.index(startPosW) + i ] )[startPosH].setShip(ship)
                cellsShip.append(self.cells.get( indexList [ indexList.index(startPosW) + i ] )[startPosH])
            ship.setCells(cellsShip)
        
        print("Ячейки шипа {}", ship.cells)
        print("Добавляем к селф.шипс наш шип", ship)
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
    field = Field(100,70)
    print("Живых кораблей {}".format(field.shipsAlive()))
    exit()