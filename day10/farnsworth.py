lines = open('testcase').readlines(-1)

x = 1
clock = 0
sum = 0
pixels = ''

def overlap(clock, reg):
    clock = clock % 40
    if abs(clock-reg) <= 1:
        return True
    else:
        return False

for l in lines:
    if l[0:4] == 'noop':
        if overlap(clock, x):
            pixels += '#'
        else:
            pixels += '.'
        clock += 1
        if clock % 40 == 20:
            sum += x * clock
        elif clock % 40 == 0:
            print(pixels)
            pixels = ''
    else:
        arg = int(l.split()[1])
        if overlap(clock, x):
            pixels += '#'
        else:
            pixels += '.'
        clock += 1
        if clock % 40 == 20:
            sum += x * clock
        elif clock % 40 == 0:
            print(pixels)
            pixels = ''
        if overlap(clock, x):
            pixels += '#'
        else:
            pixels += '.'
        clock += 1
        if clock % 40 == 20:
            sum += x * clock
        elif clock % 40 == 0:
            print(pixels)
            pixels = ''
        x += arg

print(sum)