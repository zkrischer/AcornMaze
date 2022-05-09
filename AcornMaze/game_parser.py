from cells import (
    Start,
    End,
    Air,
    Wall,
    Fire,
    Water,
    Teleport
)
import sys

def read_lines(filename):
    """Read in a file, process them using parse(),
    and return the contents as a list of list of cells."""
    
    # Tests if the file exists, and if it doesn't will display a FileNotFoundError
    try:
        f = open(filename,"r")
    except FileNotFoundError:
        sys.exit(f"{filename} does not exist!")
    
    # Turns each line into a seperate item in a list
    lines=[]
    for line in f:
        lines.append(line)
    f.close()

    #Just runs the parse function and returns 

    return(parse(lines))
    
        



def parse(lines):
    """Transform the input into a grid.

    Arguments:
        lines -- list of strings representing the grid

    Returns:
        list -- contains list of lists of Cells
    """
    # Cells will be what is returned and cell type identifies the amount of each different type of cell.
    cells=[]
    cell_type=[0,0,0,0,0,0,0,0,0,0,0]
    for line in lines:
        # Get's rid of any \n's etc
        line=line.strip("\n")
        cellz=[]

        for cell in line:
            # Tests if the letters are of the correct forms and changes each to it's respective class
            if (cell!="" and cell!= " " and cell!= "*" and cell!="X" and cell!="Y" and cell!="F" and cell!="W" and cell!="A" and cell!="1" and cell!="2" and cell!="3" and cell!="4" and cell!="5" and cell!="6" and cell!="7" and cell!="8" and cell!="9"):
                raise ValueError(f"Bad letter in configuration file: {cell}.")
            elif cell == "X":
                cell= Start("X")
            elif cell == "Y":
                cell = End("Y")
            elif cell == "W":
                cell = Water("W")
            elif cell == "F":
                cell = Fire("F")
            elif cell == "1":
                cell = Teleport('1')
            elif cell == "2":
                cell = Teleport('2')
            elif cell == "3":
                cell = Teleport('3')
            elif cell == "4":
                cell = Teleport('4')
            elif cell == "5":
                cell = Teleport('5')
            elif cell == "6":
                cell = Teleport('6')
            elif cell == "7":
                cell = Teleport('7')
            elif cell == "8":
                cell = Teleport('8')
            elif cell == "9":
                cell = Teleport('9')
            elif cell == " ":
                cell = Air(" ")
            elif cell == "*":
                cell = Wall("*")
            
            cellz.append(cell)

            
        cells.append(cellz)
    
    # This is for error checking, it updates the cell_type list with the different amounts of each cell_type
    for cellz in cells:
        for cell in cellz:
            if type(cell)==Start:
                cell_type[0]+=1
            if type(cell)==End:
                cell_type[1]+=1
            if type(cell)==Teleport:
                if cell.display=='1':
                    cell_type[2]+=1
                if cell.display=='2':
                    cell_type[3]+=1
                if cell.display=='3':
                    cell_type[4]+=1
                if cell.display=='4':
                    cell_type[5]+=1
                if cell.display=='5':
                    cell_type[6]+=1
                if cell.display=='6':
                    cell_type[7]+=1
                if cell.display=='7':
                    cell_type[8]+=1
                if cell.display=='8':
                    cell_type[9]+=1
                if cell.display=='9':
                    cell_type[10]+=1
    
    # For raising any type based errors.
    if cell_type[0]!=1:
        raise ValueError(f"Expected 1 starting position, got {cell_type[0]}.")
    if cell_type[1]!=1:
        raise ValueError(f"Expected 1 ending position, got {cell_type[1]}.")
    if (cell_type[2]!=0 and cell_type[2]!=2):
        raise ValueError("Teleport pad 1 does not have an exclusively matching pad.")
    if (cell_type[3]!=0 and cell_type[3]!=2):
        raise ValueError("Teleport pad 2 does not have an exclusively matching pad.")
    if (cell_type[4]!=0 and cell_type[4]!=2):
        raise ValueError("Teleport pad 3 does not have an exclusively matching pad.")
    if (cell_type[5]!=0 and cell_type[5]!=2):
        raise ValueError("Teleport pad 4 does not have an exclusively matching pad.")
    if (cell_type[6]!=0 and cell_type[6]!=2):
        raise ValueError("Teleport pad 5 does not have an exclusively matching pad.")
    if (cell_type[7]!=0 and cell_type[7]!=2):
        raise ValueError("Teleport pad 6 does not have an exclusively matching pad.")
    if (cell_type[8]!=0 and cell_type[8]!=2):
        raise ValueError("Teleport pad 7 does not have an exclusively matching pad.")
    if (cell_type[9]!=0 and cell_type[9]!=2):
        raise ValueError("Teleport pad 8 does not have an exclusively matching pad.")
    if (cell_type[10]!=0 and cell_type[10]!=2):
        raise ValueError("Teleport pad 9 does not have an exclusively matching pad.")    

    return(cells)   
