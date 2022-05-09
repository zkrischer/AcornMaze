import sys
import os
from game import Game
from player import Player


def test_game():
    # For Testing Easy
    game = Game("board_simple.txt",Player())
    moves = ['s','s']
    result = game.run_game(moves)
    try:
        while True:
            next(result)
    except StopIteration as a:

        assert str(a) == "\n\nYou conquer the treacherous maze set up by the Fire Nation and reclaim the Honourable Furious Forest Throne, restoring your hometown back to its former glory of rainbow and sunshine! Peace reigns over the lands.\n\nYou made 2 moves.\nYour moves: s, s\n\n=====================\n====== YOU WIN! =====\n====================="

    # Testing that non-valid moves are ignored
    game = Game("board_simple.txt",Player())
    moves = ['s','dd','s']
    result = game.run_game(moves)
    try:
        while True:
            next(result)
    except StopIteration as a:
        assert str(a) == "\n\nYou conquer the treacherous maze set up by the Fire Nation and reclaim the Honourable Furious Forest Throne, restoring your hometown back to its former glory of rainbow and sunshine! Peace reigns over the lands.\n\nYou made 2 moves.\nYour moves: s, s\n\n=====================\n====== YOU WIN! =====\n====================="

    # Testing the quit move
    game = Game("board_simple.txt",Player())
    moves = ['q']
    result = game.run_game(moves)
    try:
        while True:
            next(result)
    except StopIteration as a:
        assert str(a) == "\nBye!"

    # Testing dying in fire.
    game = Game("board_hard.txt",Player())
    moves = ['s', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'e', 's', 's', 'a', 's', 's', 'd', 's', 'd', 'd']
    result = game.run_game(moves)
    try:
        while True:
            next(result)
    except StopIteration as a:
        assert str(a) == f"\nThe Fire Nation triumphs! The Honourable Furious Forest is reduced to a pile of ash and is scattered to the winds by the next storm... You have been roasted.\n\nYou made {game.player.move_count} moves.\nYour moves: s, d, d, d, d, d, d, d, e, s, s, a, s, s, d, s, d, d\n\n=====================\n===== GAME OVER =====\n====================="

    # Dying in one move
    game = Game("board_firedeath.txt",Player())
    moves = ['s']
    result = game.run_game(moves)
    try:
        while True:
            next(result)
    except StopIteration as a:
        assert str(a) == "\nThe Fire Nation triumphs! The Honourable Furious Forest is reduced to a pile of ash and is scattered to the winds by the next storm... You have been roasted.\n\nYou made 1 move.\nYour move: s\n\n=====================\n===== GAME OVER =====\n====================="

    # Winning in One move
    game = Game("Easy_win.txt",Player())
    moves = ['w']
    result = game.run_game(moves)
    try:
        while True:
            next(result)
    except StopIteration as a:
        assert str(a) == f"\n\nYou conquer the treacherous maze set up by the Fire Nation and reclaim the Honourable Furious Forest Throne, restoring your hometown back to its former glory of rainbow and sunshine! Peace reigns over the lands.\n\nYou made 1 move.\nYour move: w\n\n=====================\n====== YOU WIN! =====\n====================="





def run_tests():
    test_game()

run_tests()