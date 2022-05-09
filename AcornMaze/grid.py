from cells import (
    Start,
    End,
    Air,
    Wall,
    Fire,
    Water,
    Teleport
)
from player import Player
import sys

def grid_to_string(grid, player):
    """Turns a grid and player into a string

    Arguments:
        grid -- list of list of Cells
        player -- a Player with water buckets

    Returns:
        string: A string representation of the grid and player.
    """
    # These are just useful variables
    string=""
    i=0
    changed_character_1 = None
    changed_character_2 = None
    water=0
    fireout=0
    firedeath=0
    airblock= Air(" ")
    wallblock = Wall("*")
    wall_hit=0
    teleporting=0

    # This runs through the grid, and identifies where the players index would be, placing 
    # the player at that location and then making sure that what was there is recorded
    if player.row>=len(grid) or player.row<0 or player.column>=len(grid[i]) or player.column<0:
        wall_hit+=1
        wallblock.step(player)
        player.move_count-=1
        player.moves.pop(-1)

        #Makes sure that the teleport does not trigger again.
        if type(grid[player.row][player.column])==Teleport:
            teleporting-=1

        changed_character_1=grid[player.row][player.column]
        grid[player.row][player.column]=player

    while i<len(grid):
        j=0
        while j<len(grid[i]):
            # This triggers at the start of the game making sure the player starts at the X
            if player.move_count==0:
                if grid[i][j].display=="X":
                    player.row=i
                    
                    player.column=j
                    if player.solver == True:
                        changed_character_1= wallblock
                    else:
                        changed_character_1=grid[i][j]
                    grid[i][j]=player

            elif player.move_count>0: 
                # reactions to certain blocks once you have made some moves
                
                # This extra condition of teleporting ==0 means that if the user has teleported or hit a wall it will stop searching.
                if i==player.row and j==player.column and teleporting==0 and wall_hit == 0:
                    
                    #T his triggers when you step onto a water block and gets ensures that from now on the water block is just an airblock.
                    if grid[i][j].display=="W":
                        grid[i][j].step(player)
                        water+=1
                        changed_character_1= airblock
                    
                    # What happens when you walk on a fire block, with different responses based on if you have water.
                    elif grid[i][j].display=="F":
                        if grid[i][j].step(player):
                            fireout+=1
                            changed_character_1= airblock
                        else:
                            firedeath+=1
                            changed_character_1=grid[i][j]
                        
                    # triggers what happens when you walk in a wall
                    elif grid[i][j].display=='*':
                        wall_hit+=1
                        grid[i][j].step(player)
                        player.move_count-=1
                        player.moves.pop(-1)
                        
                        #Makes sure that the teleport does not trigger again.
                        if type(grid[player.row][player.column])==Teleport:
                            teleporting-=1
                        changed_character_1=grid[player.row][player.column]
                        grid[player.row][player.column]=player
                    
                    #Back up to make sure that the player is not a saved location in the grid.
                    elif grid[i][j].display=='A':
                        grid[i][j]=airblock
                        changed_character_1=grid[i][j]
                        grid[i][j]=player

                    # Response for Finish Cells
                    elif grid[i][j].display=='Y':
                        grid[i][j].step(player)
                        changed_character_1=grid[i][j]
                    
                    # Response for Teleport Cells
                    elif type(grid[i][j])== Teleport:
                        teleporting+=1
                        teleport=grid[i][j].display
                        tp=grid[i][j].step(player,grid)
                        
                        changed_character_1=grid[tp[0][0]][tp[0][1]]
                        changed_character_2=grid[tp[1][0]][tp[1][1]]
                        grid[player.row][player.column]=player
                        
                        
                        
                    # Forms a base case
                    else:
                        changed_character_1=grid[i][j]
                    if wall_hit!=1:
                        grid[i][j]=player

                        
            j+=1
        i+=1

# This is used to form the string
    i=0
    while i<len(grid):
        j=0
        while j<len(grid[i]):

            #This ensures that the teleporters are printed to screen correctly as the player is in two places at once.
            if grid[i][j].display == 'A' and (i!=player.row or j!=player.column):
                if j<(len(grid[i])-1):
                    string+=f"{teleport}"
                else:
                    string+=f"{teleport}\n"

            elif j<(len(grid[i])-1):
                string+=f"{(grid[i][j]).display}"
            else:
                string+=f"{(grid[i][j]).display}\n"
            j+=1
        i+=1
        

# Changes the string based on the number of water buckets the player has.
    if player.num_water_buckets!=1:
        string+=f"\nYou have {player.num_water_buckets} water buckets."
    else:
        string+=f"\nYou have {player.num_water_buckets} water bucket."

    
# Triggers certain text responses depending on what you hit    
    if water==1:
        string+="\n\nThank the Honourable Furious Forest, you've found a bucket of water!"
    if fireout==1:
        string+="\n\nWith your strong acorn arms, you throw a water bucket at the fire. You acorn roll your way through the extinguished flames!"
    if firedeath==1:
        string+="\n\n\nYou step into the fires and watch your dreams disappear :(."
    if wall_hit==1:
        string+="\n\nYou walked into a wall. Oof!"
    if teleporting==1:
        string+="\n\nWhoosh! The magical gates break Physics as we know it and opens a wormhole through space and time."
    
    if changed_character_2 !=None:
        grid[tp[0][0]][tp[0][1]] = changed_character_1
        grid[tp[1][0]][tp[1][1]] = changed_character_2
    
    elif changed_character_1!=None:
     # returns the grid to it's original form afterwards   
        if changed_character_1==player:
            changed_character_1==airblock
        grid[player.row][player.column]=changed_character_1
        
        

    return string


