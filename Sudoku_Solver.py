def is_valid(grid, row, col, num):
    
    for i in range(9):
        if grid[row][i] == num:
            return False
    
    for i in range(9):
        if grid[i][col] == num:
            return False
        
    corner_row = row - row%3
    corner_col = col - col%3
    
    for i in range(3):
        for j in range(3):
            if(grid[corner_row+i][corner_col+j]==num):
                return False
            
    return True


def solver(grid, row, col):
    
    if col==9:
        if row==8:
            return True
        row+=1
        col=0
    
    if grid[row][col]>0:
        return solver(grid, row, col+1)
    
    for num in range(1,10):
        
        if is_valid(grid, row, col, num):
            
            grid[row][col]=num
            
            if solver(grid, row, col+1):
                return True
            
        grid[row][col]=0
        
    return False


grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 0, 0, 0, 6, 3, 0, 0]]

if solver(grid,0,0):
    for i in range(9):
        for j in range(9):
            print(grid[i][j], end=" ")
        print()
        
else: 
    print("No solution!!")