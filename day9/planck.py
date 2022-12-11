def move(dir, posn):
    (head_x, head_y, tail_x, tail_y) = posn
    if dir == 'U':
        head_y -= 1 # move up the grid one space
        if tail_y - head_y > 1: # tail only moves if direction to head and direction of travel are the same
            tail_y -= 1  # always move up a space
            tail_x = head_x # head and tail have to be orthogonal if tail moves
    
    if dir == 'D':
        head_y += 1
        if head_y - tail_y > 1:
            tail_y += 1
            tail_x = head_x

    if dir == 'R':
        head_x += 1
        if head_x - tail_x > 1:
            tail_x += 1
            tail_y = head_y

    if dir == 'L':
        head_x -= 1
        if tail_x - head_x > 1:
            tail_x -= 1
            tail_y = head_y

    return (head_x, head_y, tail_x, tail_y)

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
head_x = left
head_y = above
tail_x = left
tail_y = above
grid[above][left] = True

foo = move('U', [head_x, head_y, tail_x, tail_y])
