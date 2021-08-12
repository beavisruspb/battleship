#Без конструктора, потому как не счел его наличие необходимым, ведь ячейка может быть и пустой
class MyCell:

    #ссылка на палубу
    deck = None
    
    #Запоминаем адрес палубы
    def setDeck(self, deck):
        self.deck = deck
    
    #Проверяем выстрел
    def check(self):
        #если палуба есть
        if self.deck:
            #вызываем метод палубы
            self.deck.kill()

class MyShip:

    #статус
    live = None
    #лист палуб
    decks = []
    
    def __init__(self,decks):
        #оживляем
        self.live = True
        #запоминаем палубы
        self.decks = decks
        #перебираем палубы с цикле
        for deck in self.decks:
            #для каждой палубы предствляемся повелителем
            deck.setShip(self)
    
    #обработчик попадания
    def hit(self, deck):
        #если в списке палуб есть искомая палуба
        if deck in self.decks:
            #удаляем палубу из списка
            self.decks.remove(deck)
        
        #проверяем а остались ли вообще палубы
        if len(self.decks) <= 0:
            #идем на дно
            self.live = False

class MyDeck:

    #статус
    live = None
    #адрес ячейки
    cell = None
    #адрес корабля
    ship = None
    
    def __init__(self, cell):
        #оживляем
        self.live = True
        #запоминаем ячейку
        self.cell = cell
        #ячейка запоминает нас
        cell.setDeck(self)
        
    #запоминаем шип
    def setShip(self,ship):
        self.ship = ship
        
    #попадание
    def kill(self):
        #умираем
        self.live = False
        #вызываем метод корабля по обработке попадания
        self.ship.hit(self)

#создаем ячейки игрового поля
a1 = MyCell()
a2 = MyCell()
a3 = MyCell()

#создаем палубы запоминая адреса ячеек конструкторе 
deck1 = MyDeck(a1)
deck2 = MyDeck(a2)
deck3 = MyDeck(a3)

#создаем корабли определяя список палуб для корабля
ship1 = MyShip([deck1, deck2,deck3])


print(vars(ship1))

a1.check()

print(vars(ship1))

a3.check()

print(vars(ship1))

a2.check()

print(vars(ship1))

ship1.__init__([deck2, deck1, deck3])

print(vars(ship1))