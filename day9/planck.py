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
    
