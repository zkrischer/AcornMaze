from game import Game
import sys
from player import Player

if len(sys.argv)<2:
    sys.exit("Usage: python3 run.py <filename> [play]")

game=Game(sys.argv[1],Player())
moves = []
test = 0


a = game.run_game(moves)
while True:
    try:
        print(next(a))
    except StopIteration as a:
        print(a)
        sys.exit()