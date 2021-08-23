class Game():
    players = []

    def start(self, n = 4, w = 8, h = 4, ai_n = 1, lvl = 'hard'):
        for i in range(n - ai_n):
            self.players.append(Player(self, w, h))
        for i in range(ai_n):
            self.players.append(AIPlayer(self, w, h, lvl))
    def getPlayers(self):
        return self.players

class Field():
    cells = []
    def __init__(self, width = 10, height = 10):
        self.cells = []
        for i in range(height):
            buff = []
            for j in range(width):
                buff.append(cell())
            self.cells.append(buff) 
        self.cells[1][1].ship = True  
        self.cells[2][1].ship = True
        self.cells[1][1].closed = True 
        self.cells[0][1].closed = True
        #self.cells[2][1].closed = True        
    def shipsAlive(self):
        return 4

class cell():
    closed = False
    ship = False
    def hit(self):
        self.closed = True
        return self.ship

# А теперь моя часть назадия задом:
class Player():
    alive = True
    field = None
    game = None
    def __init__(self, Game, width = 10, height = 10):
        self.field = Field(width, height)
        self.game = Game

    def turn(self):
        import re
        target = self.selectTarget()
        target.printField()
        test = True
        while test:
            purpose = input('Выберите цель:')
            if re.match('^[a-z]\d{1,2}', purpose) is not None:
                height = ord(re.findall(r'\w', purpose)[0]) - 97
                width = int(re.findall(r'\d+', purpose)[0]) - 1
                rez = target.getHit( height, width)
                if rez != 'stop':
                    return rez      

    def isAlive(self):
        if self.field.shipsAlive() != 0: return True
        self.alive = False
        return False

    def selectTarget(self):
        import re
        if len(self.game.getPlayers()) == 2:
            if self.game.getPlayers()[0] == self:
                return self.game.getPlayers()[1] 
            return self.game.getPlayers()[0]
        print('Пока еще живы следующие враги:')
        k = 0
        lst = []
        for i in self.game.getPlayers():
            k += 1
            pref = ' _Ai'
            try:
                i.level
            except: 
                pref = ''
            if i != self: 
                print('Player', k, pref)
                lst.append(k)
        int_target = 0
        while int_target not in lst:
            target = input('Чьи корабли будем топить? Введите номер игрока:')
            if re.match('\d{1,2}', target) is not None:
                int_target = int(target)
        return self.game.players[int(target) -1]

    #def hit(self, target, x, y):
        #return True

    def printField(self):
        buff = '   '
        k = 1
        for i in self.field.cells[0]:
            buff += str(k) + ' '
            k +=1
        print(buff)
        k = 97
        for i in self.field.cells:
            buff = chr(k) + '  '
            for j in i:    
                if j.closed == False: buff += 'o ' 
                elif j.ship == True: buff += 's ' 
                else: buff += 'x '
            print(buff)
            k += 1

    def getHit(self, x, y):
        try: 
            self.field.cells[x][y]
        except:
            print('Нет такой клетки на поле!')
            return 'stop'
        self.field.cells[x][y].hit()  
        return True

class AIPlayer(Player):
    level = None        # easy, normal

    def __init__(self, Game, width = 10, height = 10, level = 'hard'):
        self.field = Field(width, height)
        self.game = Game
        self.level = level

    def turn():
        print('true')

g = Game()
g.start()
#g.players[0].printField()


#print(g.players)
g.players[0].turn()
g.players[0].turn()
g.players[0].turn()
#print (g.players[0].isAlive()) 
