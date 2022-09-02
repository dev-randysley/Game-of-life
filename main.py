from util import parse_csv
import numpy as np
import pprint
import time, os

HEIGHT_WITH_EDGES = 7 # includes additional rows
WIDTH_WITH_EDGES = 7 # includes additional columns
BOARD_SIZE = 6 # includes board without edges
CELL_LEN = 3 # size of matrix to iterated
CELL_ALIVE = 1
CELL_DEATED = 0

BLOCK = "block.csv"
BLINKER = "blinker.csv"
FILENAME = BLINKER # change filename for different patterns

def get_population(grid):
    return sum([sum(column) for column in grid ])

def get_initial_cell_position(current_position) :
    x,y = current_position
    return x-1, y-1

def is_the_cell_alive(cell):
    return cell == CELL_ALIVE

def is_not_the_current_cell(current_cell,cell):
    return not current_cell == cell

def get_amount_neighbor_cells_alive(grid, current_cell:tuple):
    x_0,y_0 = get_initial_cell_position(current_cell)
    cells_alive = 0
    for row in range(CELL_LEN):
        for column in range(CELL_LEN):
            if (is_the_cell_alive(grid[x_0 + column][y_0 + row]) and is_not_the_current_cell(current_cell,(x_0 + column,y_0 + row))):
                cells_alive += CELL_ALIVE
    return cells_alive
    
def main():
    initial_grid = np.zeros((WIDTH_WITH_EDGES,  HEIGHT_WITH_EDGES))
    setup_initial_config(initial_grid)
    show_grip(initial_grid)
    show_initial_config = input("\n Input b for begin the iterations: ")
    while show_initial_config == 'b':
        initial_grid = next_iteration(initial_grid)
        show_grip(initial_grid)
        time.sleep(5) # refresh every 5 seconds
    

def setup_initial_config(grid):
    print(os.getcwd())
    for data in parse_csv(FILENAME,types=[int,int]):
        grid[data["row"]][data["column"]] = CELL_ALIVE
    

def show_grip(grip):
    pp = pprint.PrettyPrinter(len(grip))
    grip_for_show = []
    for row in grip:
        grip_for_show.append(list(map(lambda x : 'X' if x == 1 else ' ',row)))
    pp.pprint(grip_for_show)
    print("\n")
    


def next_iteration(grid):

    temporal_grip = np.copy(grid)
    amount_neighbor_cells_alive = 0

    for row in range(1,BOARD_SIZE):
        for column in range(1,BOARD_SIZE):
            amount_neighbor_cells_alive += get_amount_neighbor_cells_alive(grid,(row,column))
        
            # now we apply the rules
            if(grid[row][column] == CELL_DEATED):
                if(amount_neighbor_cells_alive == 3):
                    temporal_grip[row][column] = CELL_ALIVE
            else:
                if(amount_neighbor_cells_alive == 2 or amount_neighbor_cells_alive == 3):
                    temporal_grip[row][column] = CELL_ALIVE
                else:
                    temporal_grip[row][column] = CELL_DEATED

            amount_neighbor_cells_alive = 0

    grid = temporal_grip # override the initial grip after all the iterations
    return grid
if __name__ == '__main__':
    main()