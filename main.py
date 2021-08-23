from classes.game import Game
conf = {
    "real_player_num" : 1,
    "width" : 10,
    "height" : 10,
    ai_players : ['easy']
}


def main():
    game = Game()
    game.start(real_player_num, width, height, ai_players = ['easy'])
    return

if __name__ == "__main__":
    main()
