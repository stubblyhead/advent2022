with open('testcase') as f:
    data = f.read().split('\n')

grid = [ [ ord(i) - 96 for i in list(row) ] for row in data ]

for row in range(len(grid)):
    for col in range(len(grid[row])):
        if grid[row][col] == -13:
            grid[row][col] = 0
        elif grid[row][col] == -27:
            grid[row][col] = 27

