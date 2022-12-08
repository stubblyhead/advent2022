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

for i in range(len(grid)):
    visible[i][0] = True  # first and last items are always visible
    visible[i][-1] = True
    for j in range(1,len(grid[i])):
        if grid[i][j] > max(grid[i][0:j]): # current item is larger than the tallest thing to the left
            visible[i][j] = True 
    for j in range(len(grid[i])-1):
        if grid[i][j] > max(grid[i][j+1:]): # current item is larger than the tallest thing to the right
            visible[i][j] = True

for i in range(len(grid[0])):
    visible[0][i] = True
    visible[-1][i] = True
    col = get_col(grid, i)
    for j in range(1,len(col)):
        if col[j] > max(col[0:j]):
            visible[i][j] = True
    for j in range(len(col)-1):
        if col[j] > max(col[j+1:]):
            visible[i][j] = True

for row in visible:
    thisrow = ''
    for col in row:
        if col:
            thisrow += 'T'
        else:
            thisrow += ' '
    print(thisrow)


count = 0
for row in visible:
    for col in row:
        if col:
            count += 1

print(count)

