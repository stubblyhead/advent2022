from copy import deepcopy

def dist(a, b):
    distance = abs(a[0]-b[0]) + abs(a[1]-b[1])
    return distance

def move(dir, rope):
    if dir == 'U':
        rope[0][1] -= 1
    elif dir == 'D':
        rope[0][1] += 1
    elif dir == 'R':
        rope[0][0] += 1
    elif dir == 'L':
        rope[0][0] -= 1

    for k in range(1,len(rope)):
        cur = rope[k]
        prev = rope[k-1]
        distance = dist(cur, prev)
        if distance == 4:
            cur[0] = int((cur[0] + prev[0])/2)
            cur[1] = int((cur[1] + prev[1])/2)
        elif distance == 2:
            if cur[0] == prev[0] or cur[1] == prev[1]:
                cur[0] = int((cur[0] + prev[0])/2)
                cur[1] = int((cur[1] + prev[1])/2)
        elif distance == 3:
            if prev[0] > cur[0]:
                cur[0] += 1
            else:
                cur[0] -= 1
            if prev[1] > cur[1]:
                cur[1] += 1
            else:
                cur[1] -= 1
    return rope

def print_grid(grid, rope):
    draw = deepcopy(grid)
    for i in range(len(draw)):
        for j in range(len(draw[i])):
            if draw[i][j]:
                draw[i][j] = '#'
            else:
                draw[i][j] = '.'
    epor = deepcopy(rope)
    epor.reverse()
    for i in range(len(epor)):
        (knot_x, knot_y) = epor[i]
        draw[knot_y][knot_x] = 9-i
    draw[knot_y][knot_x] = 'H'

    for row in range(len(draw)):
        thisrow = ''
        for col in range(len(draw[row])):
            thisrow += str(draw[row][col])
        print(thisrow)
        
    print('\n')
        
lines = open('input').readlines(-1)

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


grid = [ [False for i in range(-left+right+1)] for j in range(above-below+1) ]
rope = [ [-left,above] for i in range(10) ]
grid[above][-left] = True

for l in lines:
    (dir, steps) = l.strip().split()
    steps = int(steps)

    for i in range(steps):
        rope = move(dir, rope)
        grid[rope[-1][1]][rope[-1][0]] = True

count = 0
for i in grid:
    count += i.count(True)

print(count)