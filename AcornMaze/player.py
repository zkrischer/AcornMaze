class Player:

    def __init__(self):
        # Correctly establishes the initial values.
        self.display = 'A'
        self.num_water_buckets = 0
        self.move_count=0
        self.moves=[]
        self.row=0
        self.column=0
        self.game_over=0
        self.solver = False

# Updates the move count and list of moves so that they can be displayed at the end of the game properly.
    def move(self, move):
        if move == 'q' or move == 'w' or move == 'a' or move == 's' or move == 'd' or move == 'e':
            self.move_count+=1
            self.moves.append(move)
        
