lines = open('testcase').readlines(-1)

above = below = left = right = 0
cur_x = cur_y = 0

for l in lines:
    (dir, num) = l.strip().split()
    num = int(num)
    if dir == 'U':
        cur_y += num
        above = max(cur_y, above)
    elif dir == 'D':
        cur_y -= num
        below = min(cur_y, below)
    elif dir == 'R':
        cur_x += num
        right = max(cur_x, right)
    elif dir == 'L':
        cur_x -= num
        left = min(cur_x, left)

print(left, right)
print(above, below)

grid = [ [False for i in range(left+right+1)] for j in range(above+below+1) ]
head_x = right
head_y = above
tail_x = right
head_y = above
grid[above][left] = True

for i in grid:
    print(i)
    
