class Game:

    players = None # [] Players

    def finish():
        return

    def getGameFinished():
        return

    def getPlayers():
        return  #[] Player

    def start(player_count, width, height, ai_number):
        return

class Cell:

    #ссылка на корабль
    ship = None

    #ранее стреляли по этой клетке или нет
    closed = True
    
    #Запоминаем адрес корабля
    def setShip(self, ship):
        self.ship = ship
    
    #Проверяем выстрел
    def hit(self):
        if self.closed:
            #подстреливаем ячейку
            self.closed = False
            #если ячейка еще не подстрелена и есть корабль
            if self.ship:
                return True
            return False

class Ship:

    #лист палуб
    cells = []
    
    def __init__(self,cells):
        #запоминаем палубы
        self.cells = cells
        #перебираем палубы с цикле
        for cell in self.cells:
            #для каждой палубы предствляемся повелителем
            cell.setShip(self)

    def isAlive(self):
        #посмотрим все ячейки корабля
        for cell in self.cells:
            #если есть ячейка в которую не стреляли
            if cell.closed:
                #значит кораблик еще барахтается
                #дальше можно и не проверять
                return True
        return False
        
    def getSize(self):
        return len(self.cells)

class Field:

    cells = None

    ships = None

    def makeField(width, height):
        start = 97
        end = 122
        
