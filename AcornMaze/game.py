from game_parser import read_lines
from grid import grid_to_string
from player import Player
import os
import sys




class Game:
    def __init__(self, filename,player,solver=False):
        self.grid= read_lines(filename)
        self.player=player
        if solver == True or sys.argv[-1]=='solve':
            self.player.solver=True
        self.string = grid_to_string(self.grid,self.player)
        
        

    def gameMove(self, move):
        # Records the move in the player class
        self.player.move(move)
        
        a = self.player.num_water_buckets

        # Adjusts the player's indexes depending on which move is made
        if self.player.move_count>0:
            if self.player.moves[-1]=='w':
                self.player.row-=1
            if self.player.moves[-1]=='s':
                self.player.row+=1
            if self.player.moves[-1]=='a':
                self.player.column-=1
            if self.player.moves[-1]=='d':
                self.player.column+=1
                
        # Changes the grid based on the move you made
        self.string=grid_to_string(self.grid, self.player)
        
        # Returns true if your water buckets have changed.
        if self.player.num_water_buckets != a:
            return True
        
    
    # I'm choosing to run the game as a function for ease of testing later, as I can just test what the function returns.
    def run_game(self,moves):
        
        test=0
        while True:
            # Causes the system to clear if chosen to 'play'
            if sys.argv[-1]=='play':
                os.system('clear')

            #Exclusively for testing/solving if there are moves pregiven it won't print to screen
            if len(moves)==0:
                yield(self.string)

            # Game_over 1 is the lose condition for when you burn in the fires!
            if self.player.game_over==1:
                moves=", ".join(self.player.moves)
                if self.player.move_count == 1:
                    to_print = f"\nThe Fire Nation triumphs! The Honourable Furious Forest is reduced to a pile of ash and is scattered to the winds by the next storm... You have been roasted.\n\nYou made {self.player.move_count} move.\nYour move: {moves.strip(', ')}\n\n=====================\n===== GAME OVER =====\n====================="
                else:
                    to_print = f"\nThe Fire Nation triumphs! The Honourable Furious Forest is reduced to a pile of ash and is scattered to the winds by the next storm... You have been roasted.\n\nYou made {self.player.move_count} moves.\nYour moves: {moves.strip(', ')}\n\n=====================\n===== GAME OVER =====\n====================="
                return to_print

            # Game_over 2 is the win condition
            if self.player.game_over==2:
                moves=", ".join(self.player.moves)
                if self.player.move_count == 1:
                    to_print = f"\n\nYou conquer the treacherous maze set up by the Fire Nation and reclaim the Honourable Furious Forest Throne, restoring your hometown back to its former glory of rainbow and sunshine! Peace reigns over the lands.\n\nYou made {self.player.move_count} move.\nYour move: {moves.strip(', ')}\n\n=====================\n====== YOU WIN! =====\n====================="
                else:
                    to_print = f"\n\nYou conquer the treacherous maze set up by the Fire Nation and reclaim the Honourable Furious Forest Throne, restoring your hometown back to its former glory of rainbow and sunshine! Peace reigns over the lands.\n\nYou made {self.player.move_count} moves.\nYour moves: {moves.strip(', ')}\n\n=====================\n====== YOU WIN! =====\n====================="
                return to_print
                
            # This runs the input and calculates the input from the player and stores it in it's respective places.
            while True:
                # This is a test step, subbing in the moves from a list instead of input
                if len(moves)>0:
                    move = moves[test]
                    test+=1
                else:
                    move=input("\nInput a move: ")
                move=move.lower()

                # Makes sure all moves are valid, and none break the system.
                if move != 'q' and move!="w" and move!='a' and move!='s' and move!='d' and move!='e':
                    
                    #Ensures it's only printed to screen in regular play
                    if len(moves)==0:
                        print(self.string)
                        yield("\nPlease enter a valid move (w, a, s, d, e, q).")

                    continue
                
                elif move== 'q':
                    # Triggers the quit action
                    to_print = "\nBye!"
                    return to_print
                else:
                    self.gameMove(move)
                    break
                
                
                continue


