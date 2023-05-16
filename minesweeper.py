def minesweeper(grid):
    """ 
    A function that takes a grid of # and -, where each hash (#) represents a
    mine and each dash (-) represents a mine-free spot. Function will return a
    grid where a dash is replaced by the number of mines adjacent to the spot.
    Note: the function will work with any grid size. 
    Parameters:
        grid (list): A grid (a list of lists)
    Returns:
        list: a grid which shows the number of mines nearby each spot.
    """
    
    # 2 loops that go through each position of the grid one by one.
    for row in range(len(grid)): 
        for col in range(len(grid[row])):
            
            if grid[row][col] == "#":
                continue
            # If the position contains a bomb, there's no action needed.
            
            bomb_count = 0
            # The variable that will count the numbers of bombs nearby.
            
            # Out of bounds locations: 'row-1' and 'col-1' equal to -1; 
            # 'col+1' and 'row+1' equal to the length of the grid.
            
            # 'row-1' check (positions NW, N, NE)
            if row-1 != -1:
                if col-1 != -1 and grid[row-1][col-1] == "#":
                    bomb_count += 1
                if grid[row-1][col] == "#":
                    bomb_count += 1
                if col+1 != len(grid) and grid[row-1][col+1] == "#":
                    bomb_count += 1
            
            # 'row' check (positions W, E)
            if col-1 != -1 and grid[row][col-1] == "#":
                bomb_count += 1     
            if col+1 != len(grid) and grid[row][col+1] == "#":
                bomb_count += 1
            
            # 'row+1' check (position SW, S, SE)
            if row+1 != len(grid):
                if col-1 != -1 and grid[row+1][col-1] == "#":
                    bomb_count += 1
                if grid[row+1][col] == "#":
                    bomb_count += 1
                if col+1 != len(grid) and grid[row+1][col+1] == "#":
                    bomb_count += 1
            
            # The if statements check for bombs in each location adjacent to
            # the current position, while also checking if it's out of bounds.
            
            grid[row][col] = str(bomb_count)
            # Replacing the dash '-' with bomb count of the current position.
    
    return grid


my_grid = [ ["-", "-", "-", "#", "#"],
            ["-", "#", "-", "-", "-"],
            ["-", "-", "#", "-", "-"],
            ["-", "#", "#", "-", "-"],
            ["-", "-", "-", "-", "-"] ]

counted_bombs = minesweeper(my_grid)
# Calling the minesweeper function which will return bomb counts. 

for row in counted_bombs:
    print(row)
# This will print our grid in the desired output format.