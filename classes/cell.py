class Cell:

    #ссылка на корабль
    ship = None

    #ранее стреляли по этой клетке или нет
    closed = True

    block = False
    
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
                print("Попал")
                return True
            return False
        print("Сюда уже стреляли")
        return False
