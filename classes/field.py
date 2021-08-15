import ship
import cell
class Field:

    cells = None

    ships = None

    #возвращает количество живых кораблей
    def shipAlive(self):
        
        shipCount = 0
        #перебираем все шипы
        for ship in ships:
            if ship:
                shipCount += 1
        return shipCount

    def placeShips(self):

        return

    #Создаем игровое поле
    def makeField(self, width, height):

        #Приватная служебная функция для правильного составления буквенных индексов
        #Возвращает list стрингов
        def __getWidhtIndex(width):

            from string import ascii_lowercase
            import itertools

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


if __name__ == "__main__":
    field = Field()
    field.makeField(63,4)
    print(vars(field))
