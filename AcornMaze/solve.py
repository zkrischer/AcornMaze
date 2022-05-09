from game import Game
import sys
from player import Player
from cells import (
    Start,
    End,
    Air,
    Wall,
    Fire,
    Water,
    Teleport
)


def solve(file,mode):
    # Assigns the solution found variable so it can be changed inside the function

    # means it doesn't matter if the user inputs upper or lower case
    mode=mode.upper()
    
# The two modes are identical except for one line, so comments in DFS also apply to BFS.

    if mode == 'DFS':
        # Will continue to run until the game is over
        game_over = False

        #These are lists of places visited, moves to take, and the full path.
        moves_to_take = [' ']
        moves_to_end = []
        visited = []

        while game_over == False:
            # If there are no more moves to take the solver will quit and show no solution.
            if len(moves_to_take)==0:
                break

            # Initialises the game and will take the last move in the possible lists (which is why it's DFS)
            a = False
            moves = moves_to_take.pop(-1)
            game = Game(file,Player(),solver=True)

            # Will enact the moves that have been done previously, if water is picked up it will clear the visited list.
            for move in moves:
                if move == 'q' or move == 'e' or move == 'a' or move == 'd' or move == 's' or move == 'w':
                    a = game.gameMove(move)
                    if a == True:
                        visited = []
                    current = game.grid[game.player.row][game.player.column]
                    # Adds that location to the visited list.
                    visited.append(current)
            
            # If you've one the game end the loop and store the path.
            if game.player.game_over==2:
                game_over = True
                for move in moves:
                    moves_to_end.append(move)

            
            row = game.player.row
            column = game.player.column
            current = game.grid[row][column]
            
            up = None
            down = None
            left = None
            right = None


            # Checks if you are on the edge of the grid, and if you are restricts your movement to only inside the grid.
            if row!=0:
                up = game.grid[row-1][column]
            if row<(len(game.grid)-1):
                down = game.grid[row+1][column]
            if column!=0:
                left = game.grid[row][column-1]
            if column<(len(game.grid[1])-1):
                right = game.grid[row][column+1]


            # Checks if each side is a Wall or a Fire type, although fire is ignored if you have more than one water bucket.
            # Also checks if you've visited the space before. Then adds it to a possible move_to_take.
            
            if left!= None and type(left)!= Wall and (type(left)!=Fire or game.player.num_water_buckets>0):
                if left not in visited:
                    if game.player.move_count==0:
                        moves_1 = moves+'a'
                        moves_to_take.append(moves_1)

                    # This makes sure you can't go back and forth instantaneously, but it is ignore if you step in a teleporter
                    elif game.player.moves[-1]!='d' or type(current)==Teleport:
                        moves_1 = moves+'a'
                        moves_to_take.append(moves_1)

            if up!= None and type(up)!= Wall and (type(up)!=Fire or game.player.num_water_buckets>0):
                if up not in visited:
                    if game.player.move_count==0:
                        moves_2 = moves+'w'
                        moves_to_take.append(moves_2)

                    elif game.player.moves[-1]!='s' or a==True:
                        moves_2 = moves+'w'
                        moves_to_take.append(moves_2)

            if right!= None and type(right)!= Wall and (type(right)!=Fire or game.player.num_water_buckets>0):
                if right not in visited:
                    if game.player.move_count==0:
                        moves_3 = moves+'d'
                        moves_to_take.append(moves_3)

                    elif game.player.moves[-1]!='a' or type(current)==Teleport:
                        moves_3 = moves+'d'
                        moves_to_take.append(moves_3)

            if down!= None and type(down)!= Wall and (type(down)!=Fire or game.player.num_water_buckets>0):
                if down not in visited:
                    if game.player.move_count==0:
                        moves_4 = moves+'s'
                        moves_to_take.append(moves_4)

                    elif game.player.moves[-1]!='w' or a==True:
                        moves_4 = moves+'s'
                        moves_to_take.append(moves_4)

            # Checks if the current space is a teleporter, and if it is adds 'e' to the possible moves, won't do it if you did 'e' last.
            if type(current) == Teleport and game.player.moves[-1]!='e':
                moves_5 = moves+"e"
                moves_to_take.append(moves_5)
    

    # This occurs once the upper loop is finished, it makes the printable phrase and returns it to the original program.
        if game_over == True:
            for move in moves_to_end:
                if move == ' ':
                    moves_to_end.pop(moves_to_end.index(move))

            moves=", ".join(moves_to_end)

            return f"Path has {len(moves_to_end)} moves.\nPath: {moves.strip(', ')}"
        if game_over == False:
            return


    if mode == 'BFS':
        game_over = False

        moves_to_take = [' ']
        moves_to_end = []
        visited = []

        while game_over == False:
            if len(moves_to_take)==0:
                break

            # Initialises the game and will take the first move in the possible lists (which is why it's BFS)
            a = False
            moves = moves_to_take.pop(0)
            game = Game(file,Player(),solver=True)

            for move in moves:
                if move == 'q' or move == 'e' or move == 'a' or move == 'd' or move == 's' or move == 'w':
                    a = game.gameMove(move)
                    if a == True:
                        visited = []

                    current = game.grid[game.player.row][game.player.column]
                    visited.append(current)
            
            if game.player.game_over==2:
                game_over = True
                for move in moves:
                    moves_to_end.append(move)

            
            row = game.player.row
            column = game.player.column
            current = game.grid[row][column]
            
            up = None
            down = None
            left = None
            right = None


            if row!=0:
                up = game.grid[row-1][column]
            if row<(len(game.grid)-1):
                down = game.grid[row+1][column]
            if column!=0:
                left = game.grid[row][column-1]
            if column<(len(game.grid[1])-1):
                right = game.grid[row][column+1]


            
            if left!= None and type(left)!= Wall and (type(left)!=Fire or game.player.num_water_buckets>0):
                if left not in visited:
                    if game.player.move_count==0:
                        moves_1 = moves+'a'
                        moves_to_take.append(moves_1)

                    elif game.player.moves[-1]!='d' or type(current)==Teleport:
                        moves_1 = moves+'a'
                        moves_to_take.append(moves_1)

            if up!= None and type(up)!= Wall and (type(up)!=Fire or game.player.num_water_buckets>0):
                if up not in visited:
                    if game.player.move_count==0:
                        moves_2 = moves+'w'
                        moves_to_take.append(moves_2)

                    elif game.player.moves[-1]!='s' or a==True:
                        moves_2 = moves+'w'
                        moves_to_take.append(moves_2)

            if right!= None and type(right)!= Wall and (type(right)!=Fire or game.player.num_water_buckets>0):
                if right not in visited:
                    if game.player.move_count==0:
                        moves_3 = moves+'d'
                        moves_to_take.append(moves_3)

                    elif game.player.moves[-1]!='a' or type(current)==Teleport:
                        moves_3 = moves+'d'
                        moves_to_take.append(moves_3)

            if down!= None and type(down)!= Wall and (type(down)!=Fire or game.player.num_water_buckets>0):
                if down not in visited:
                    if game.player.move_count==0:
                        moves_4 = moves+'s'
                        moves_to_take.append(moves_4)

                    elif game.player.moves[-1]!='w' or a==True:
                        moves_4 = moves+'s'
                        moves_to_take.append(moves_4)

            if type(current) == Teleport and game.player.moves[-1]!='e':
                moves_5 = moves+"e"
                moves_to_take.append(moves_5)
    

        if game_over == True:
            for move in moves_to_end:
                if move == ' ':
                    moves_to_end.pop(moves_to_end.index(move))

            moves=", ".join(moves_to_end)

            return f"Path has {len(moves_to_end)} moves.\nPath: {moves.strip(', ')}"
        if game_over == False:
            return
