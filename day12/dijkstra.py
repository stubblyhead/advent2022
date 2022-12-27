with open('testcase') as f:
    data = f.read().split('\n')

grid = [ [ ord(i) - 96 for i in list(row) ] for row in data ]
root = []
target = []
for row in range(len(grid)):
    for col in range(len(grid[row])):
        if grid[row][col] == -13:
            grid[row][col] = 0
            root = [row, col]
        elif grid[row][col] == -27:
            grid[row][col] = 27
            target = [row,col]

def bfs(grid, root):  # will flesh this out
    pass

def get_moves(grid, node):  # node in [row, col] format
    (row, col) = node
    moves = ''
    # check above
    if cur_row > 0:
        if grid[row-1][col] - grid[row][col] <= 1:
            moves += 'U'
    # check below
    if row < len(grid) - 1:
        if grid[row+1][col] - grid[row][col] <= 1:
            moves += 'D'
    # check right
    if col < len(grid[row] -1):
        if grid[row][col+1] - grid[row][col] <= 1:
            moves += 'R'
    # check left
    if col > 0:
        if grid[row][col-1] - grid[row][col] <= 1:
            moves += 'L'

    return moves
