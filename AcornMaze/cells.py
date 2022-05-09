# All have of these classes have a display input, this makes it easy to change what type of letter related to the cell.

class Start:
    def __init__(self,display):
        self.display = display

# Doesn't need a step function
    def step(self, player):
        pass


class End:
    def __init__(self,display):
        self.display = display

#Makes sure the end of the game occurs
    def step(self, player):
        player.game_over+=2


class Air:
    def __init__(self,display):
        self.display = display

# Doesn't need a step function
    def step(self, player):
        pass


class Wall:
    def __init__(self,display):
        self.display = display

# Moves you back to the space you were before.
    def step(self, player):
        if player.moves[-1]=='w':
            player.row+=1
        if player.moves[-1]=='s':
            player.row-=1
        if player.moves[-1]=='a':
            player.column+=1
        if player.moves[-1]=='d':
            player.column-=1


class Fire:
    def __init__(self,display):
        self.display = display

# Sees if you have a water bucket, and then either gets rid of one or triggers the beginning of a death sequence.
    def step(self, player):
        if player.num_water_buckets>0:
            player.num_water_buckets-=1
            return True
        else:
            player.game_over+=1
            return False


class Water:
    def __init__(self,display):
        self.display = display

# Gives you an additional water
    def step(self, player):
        player.num_water_buckets+=1


class Teleport:
# Differentiates between the different teleport cells based on the number their display is.
    def __init__(self,number):
        self.display = number  

# This is what happens when you step on a teleport cell
    def step(self, player,grid):
        # This searches through the grid and identifies all points that are a teleporter with the same display.
        display = self.display
        teleport_points = []
        i=0
        while i<len(grid):
            j=0
            while j<len(grid[i]):
                if (grid[i][j]).display== display:
                    tp = [i,j]
                    teleport_points.append(tp)
                j+=1
            i+=1

        # This identifies which of the teleport cells the player is at and which they want to teleport to.
        tp=[]
        if player.row==teleport_points[0][0]:
            if player.column==teleport_points[0][1]:
                target = teleport_points[1]
                tp.append(teleport_points[1])
                tp.append(teleport_points[0])
                
        if player.row==teleport_points[1][0]:
            if player.column==teleport_points[1][1]:
                target = teleport_points[0]
                tp.append(teleport_points[0])
                tp.append(teleport_points[1])
                
        # Sets the players coordinates to their target location
        player.row=target[0]
        player.column=target[1]
        
        # Returns the two teleport points, so that they can be reset once the string has been made.
        return tp
        


