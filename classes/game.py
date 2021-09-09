from player import Player
from player import AIPlayer


class Game:
    players = []

    def start(self, real_player_num, width, height, ai_players=['easy']):

        ai_player_num = len(ai_players)

        if real_player_num <= 0:
            print("Слишком мало живых игроков")
            return False

        if real_player_num + ai_player_num < 2:
            print("Слишком мало игроков")
            return False

        number = 0

        for i in range(real_player_num):
            number += 1
            self.players.append(Player(self, width, height, number))

        if ai_player_num > 0:
            for level in ai_players:
                number += 1
                self.players.append(
                    AIPlayer(self, width, height, level, number))

        while True:
            for player in self.players:
                if player.isAlive():
                    while True:
                        print("Ходит игрок " + player.number)
                        if player.turn() == False:
                            break
            if self.isGameFinished():
                break

        for player in self.players:
            if player.isAlive():
                print('Game Over! Winner: ' + str(player.number))
                return self.finish()

    def isGameFinished(self):
        alives = 0

        for player in self.players:
            if player.isAlive():
                alives += 1

        if alives > 1:
            return False

        return True

    def getPlayers(self, alives=False):
        if alives == True:
            return self.players
        alivePlayers = []
        for player in self.players:
            if player.isAlive():
                alivePlayers.append(player)
        return alivePlayers

    def finish():
        return True
