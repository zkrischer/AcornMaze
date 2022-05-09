import sys
import os
from game import Game
from player import Player
from solve import solve


def test_solver():
    # For solving a simple grid 
    a = solve("board_simple.txt","dfs")
    b = solve("board_simple.txt","bfs")

    assert a == "Path has 2 moves.\nPath: s, s"
    assert b == "Path has 2 moves.\nPath: s, s"

    # For solving a grid requiring the use of 'e' 
    a = solve("board_trapped.txt","dfs")
    b = solve("board_trapped.txt","bfs")

    assert a == "Path has 8 moves.\nPath: s, d, d, s, e, s, s, s"
    assert b == "Path has 8 moves.\nPath: s, d, d, s, e, s, s, s"

    # For solving a harder grid requiring back-tracking 
    a = solve("board_hard.txt","dfs")
    b = solve("board_hard.txt","bfs")

    assert a == "Path has 37 moves.\nPath: s, s, s, s, s, s, s, d, a, a, w, w, e, a, a, a, s, s, w, w, d, d, d, e, s, s, d, d, e, d, d, d, s, s, s, s, s"
    assert b == "Path has 25 moves.\nPath: s, d, d, d, d, s, s, w, w, d, d, d, a, a, s, s, d, d, d, d, s, s, s, s, s"

    #Testing a grid with holes in the walls
    a = solve("board_hard.txt","dfs")
    b = solve("board_hard.txt","bfs")

    assert a == "Path has 37 moves.\nPath: s, s, s, s, s, s, s, d, a, a, w, w, e, a, a, a, s, s, w, w, d, d, d, e, s, s, d, d, e, d, d, d, s, s, s, s, s"
    assert b == "Path has 25 moves.\nPath: s, d, d, d, d, s, s, w, w, d, d, d, a, a, s, s, d, d, d, d, s, s, s, s, s"

    #Testing for a non possible solution
    a = solve("board_firedeath.txt","dfs")
    b = solve("board_firedeath.txt","bfs")

    assert a == None
    assert b == None









def run_tests():
    test_solver()

run_tests()