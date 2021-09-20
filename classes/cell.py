import logging

class Cell:

    #ссылка на корабль
    ship = None

    #ранее стреляли по этой клетке или нет
    closed = True

    block = False

    def __init__(self, logLevel = logging.DEBUG):
        #Настраивается логирование
        #Объект шаблона
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        #Объект консоли
        consoleOut = logging.StreamHandler()
        #Объект файла лога
        fileLog = logging.FileHandler("cell.log")
        #Устанавливаем формат сообщения для дескрипторов устройств
        [stream.setFormatter(formatter) for stream in [fileLog, consoleOut]]
        #Создаем логгер
        self.log = logging.getLogger("Cell_Obj")
        #Добавляем дескрипторы устройств к объекту логера
        [self.log.addHandler(handler) for handler in [consoleOut, fileLog]]
        #Устанавливаем уровень логирования для объекта логера
        self.log.setLevel(logLevel)
    
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
                self.log.info("Попал")
                return True
            self.log.info("Мазила")
            return False
        self.log.info("Сюда уже стреляли")
        return None
