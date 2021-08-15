class Ship:

    #лист палуб
    cells = []
    
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

    def setCells(self, cells):
        self.cells = cells