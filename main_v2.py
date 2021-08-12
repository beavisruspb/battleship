class MyCell:

    #ссылка на корабль
    ship = None

    #ранее стреляли по этой клетке или нет
    wounded = None

    def __init__(self):
        #ячейка не стреляная
        self.wounded = False
    
    #Запоминаем адрес корабля
    def setShip(self, ship):
        self.ship = ship
    
    #Проверяем выстрел
    def check(self):
        #если ячейка еще не подстрелена и есть корабль
        if  not self.wounded and self.ship:
            #подстреливаем ячейку
            self.wounded = True
            #вызываем метод палубы
            self.ship.setLiveStatus()

class MyShip:

    #статус
    live = None
    #лист палуб
    cells = []
    
    def __init__(self,cells):
        #запоминаем палубы
        self.cells = cells
        #перебираем палубы с цикле
        for cell in self.cells:
            #для каждой палубы предствляемся повелителем
            cell.setShip(self)
        #оживляем
        self.setLiveStatus()

    def setLiveStatus(self):
        #пердположим что корабль уже все
        self.live = False
        #посмотрим все ячейки корабля
        for cell in self.cells:
            #если есть ячейка в которую не стреляли
            if not cell.wounded:
                #значит кораблик еще барахтается
                self.live = True


#создаем ячейки игрового поля
a1 = MyCell()
a2 = MyCell()
a3 = MyCell()

#создаем корабли определяя список палуб для корабля
ship1 = MyShip([a1, a2, a3])

print("кораблик", vars(ship1))

a1.check()

print(vars(a1))

a3.check()

print(vars(a3))

a2.check()

print(vars(a2))

#таким образом коробль оживить нельзя ведь ячейки уже битые
#необходимо либо оживить ячейки, либо указать нестреляные
#ship1.__init__([a2, a1, a3])
#print(vars(ship1))

