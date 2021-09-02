class Game():
    players = [];  

    def start(self, n = 3, w = 6, h = 3, ai_n = 2, lvl = 'hard'):
        num = 0;
        for i in range(n - ai_n):
            num += 1;
            self.players.append(Player(self, w, h, num));

        for i in range(ai_n):
            num += 1;
            self.players.append(AIPlayer(self, w, h, num, lvl));
    def getPlayers(self):
        return self.players;

        #fack

class Field():
    cells = [];
    def __init__(self, width = 10, height = 10):
        self.cells = [];
        for i in range(height):
            buff = [];
            for j in range(width):
                buff.append(cell());
            self.cells.append(buff) ;
        self.cells[1][1].ship = True;  
        self.cells[2][1].ship = True;
        self.cells[0][3].ship = True;
        self.cells[1][1].closed = True; 
        self.cells[0][1].closed = True;
        #self.cells[0][3].closed = True;
        #self.cells[2][1].closed = True;        
    def shipsAlive(self):
        return 4;

class cell():
    closed = False;
    ship = False;
    def hit(self):
        self.closed = True;
        return self.ship;

# А теперь моя часть назадия задом:
class Player():
    number = 0;
    alive = True;
    field = None;
    game = None;
    def __init__(self, game, width, height, number):
        self.field = Field(width, height);
        self.game = game;
        self.number = number;

    def turn(self):
        import re;
        target = self.selectTarget();
        target.printField();
        test = True;
        while test:
            purpose = input('Выберите цель:');
            if re.match('^[a-z]\d{1,2}', purpose) is not None:
                height = ord(re.findall(r'\w', purpose)[0]) - 97;
                width = int(re.findall(r'\d+', purpose)[0]) - 1;
                rez = target.getHit( height, width);
                if rez != 'stop':
                    return rez;      

    def isAlive(self):
        if self.field.shipsAlive() != 0: return True;
        self.alive = False;
        return False;

    def selectTarget(self):
        import re;
        if len(self.game.getPlayers()) == 2:
            if self.game.getPlayers()[0] == self:
                return self.game.getPlayers()[1] ;
            return self.game.getPlayers()[0];

        print('Пока еще живы следующие враги:')
        k = 0;
        lst = [];
        for i in self.game.getPlayers():
            k += 1;
            pref = ' _Ai';
            if type(i).__name__ == "Player":
                pref = '';
            if i != self: 
                print('Player', k, pref);
                lst.append(k);
        int_target = 0;

        while int_target not in lst:
            target = input('Чьи корабли будем топить? Введите номер игрока:');
            if re.match('\d{1,2}', target) is not None:
                int_target = int(target);
            print("Введите номер игрока из списка, просто циферку, например '" + str(k) + "':");

        return self.game.players[int(target) -1];

    #def hit(self, target, x, y):
        #return True;

    def printField(self):
        buff = '   '
        k = 1;
        for i in self.field.cells[0]:
            buff += str(k) + ' ';
            k +=1;
        print(buff);
        k = 97;
        for i in self.field.cells:
            buff = chr(k) + '  ';
            for j in i:    
                if j.closed == False: buff += 'o ' ;
                elif j.ship == True: buff += 's ' ;
                else: buff += 'x ';
            print(buff);
            k += 1;

    def getHit(self, x, y):
        try: 
            self.field.cells[x][y];
        except:
            print('Нет такой клетки на поле!')
            return 'stop';
        if self.field.cells[x][y].closed != False:
            print("В эту клетку уже стреляли");
            return 'stop';
        return self.field.cells[x][y].hit() ;

class AIPlayer(Player):
    level = None;        # easy, medium
    easy_purpose_h, easy_purpose_w = None, None;

    def __init__(self, game, width, height, number, level = 'hard'):
        self.field = Field(width, height);
        self.game = game;
        self.level = level;
        self.number = number;

    def turn(self):
        self.easy_purpose_h, self.easy_purpose_w = None, None ;
        target = self.selectTarget();

        if self.easy_purpose_h != None:
            target.printField()            # отладка
            return target.getHit(self.easy_purpose_h, self.easy_purpose_w);
        
        self.hitEasy(target);

        target.printField() # отладка
        

    def hitEasy(self, target):
        from random import randint; 
        k = 1;
        while True:
            width = randint(0, len(self.field.cells[0]) - 1 );
            height = randint(0, len(self.field.cells) - 1 );
            rez = target.getHit( height, width);
            if rez != 'stop':
                return rez;     

    def selectTarget(self):
        players = self.game.getPlayers();
        from random import randint ; 
        num = randint(1, len(players)-1);

        if self.level != 'easy':                    # поиск легкой цели
            j = num ;
            for i in range(len(players)-1): 
                if self.number == (j+1):  j += 1;               
                if j == len(players):   j = 0;
                rez = self.analysisTarget(players[j]) ;
                if rez != None:     return rez;
                j += 1;      

        if self.level == 'hard':
            j = num ;
            isx = 0;
            for i in range(len(players)-1): 
                if self.number == (j+1):  j += 1;               
                if j == len(players):   j = 0;
                rez = self.verAnalysisTarget(players[j]) ;
                if rez > isx:
                    isx = rez;  
                    choice_target = players[j];
                j += 1;     
            return choice_target;

        if self.number <= num:
            return players[num] ;
        return players[num - 1] ;

    def verAnalysisTarget(self, target):
        num_cells, close, purpose = 0, 0, 0  ;
        for i in target.field.cells:
            for j in i:
                num_cells += 1;
                if j.closed: close +=1;
                #if j.closed and j.ship: d_s += 1;
                if (not j.closed) and j.ship: purpose += 1;
        print(purpose, num_cells, close) 
        return purpose/(num_cells - close);

    def analysisTarget(self, target):

        def Test(cell, h, w):
            try:           
                if h>=0 and w>=0:
                    if not cell[h][w].closed:
                        self.easy_purpose_h, self.easy_purpose_w = h, w ;
                        return target;
            except: pass;
            return None;                  
        
        for y in range(len(target.field.cells) ):
            for x in range(len(target.field.cells[0]) ):   
                if target.field.cells[y][x].closed  and target.field.cells[y][x].ship : 
                    if Test(target.field.cells, y, x-1) : return target;
                    if Test(target.field.cells, y, x+1) : return target;
                    if Test(target.field.cells, y-1, x) : return target;
                    if Test(target.field.cells, y+1, x) : return target;
        
                    


g = Game();
g.start();
#g.players[0].printField();


#print(g.players)
for i in range(8):
    g.players[1].turn();
#g.players[0].turn();
#g.players[0].turn();
#print (g.players[0].isAlive()) ;
