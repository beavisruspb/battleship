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