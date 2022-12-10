from copy import deepcopy

lines = open('input')
grid = []


for l in lines:
    grid.append(list(l.strip()))

visible = deepcopy(grid)

for i in range(len(grid)):
    for j in range(len(grid[i])):
        visible[i][j] = False

def get_col(a, c):
    col = []
    for r in a:
        col.append(r[c])
    return col

def get_row(a,row):
    return row[a]

def rotate(a):
    rotated = []
    for i in range(len(a[0])):
        newrow = get_col(a,i)
        newrow.reverse()
        rotated.append(newrow)
    return rotated

def print_grid(a):
    for row in range(len(grid)):
        thisrow = str(row+1) + '\t'
        for col in range(len(grid[row])):
            thisrow += grid[row][col]
        print(thisrow)
    print('\n')

for h in range(4):
    for i in range(len(grid)):
        visible[i][0] = True  # first and last items are always visible
        visible[i][-1] = True
        for j in range(1,len(grid[i])):
            if grid[i][j] > max(grid[i][0:j]): # current item is larger than the tallest thing to the left
                visible[i][j] = True 
        for j in range(len(grid[i])-1):
            if grid[i][j] > max(grid[i][j+1:]): # current item is larger than the tallest thing to the right
                visible[i][j] = True
    grid = rotate(grid)
    visible = rotate(visible)


count = 0
for row in visible:
    for col in row:
        if col:
            count += 1

print(count)


