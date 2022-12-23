lines = open('testcase').readlines(-1)

x = 1
clock = 0
sum = 0

for l in lines:
    if l[0:4] == 'noop':
        clock += 1
        if clock % 40 == 20:
            print(l, clock, x)
            sum += x * clock
    else:
        arg = int(l.split()[1])
        clock += 1
        if clock % 40 == 20:
            print(l, clock, x)
            sum += x * clock
        clock += 1
        
        if clock % 40 == 20:
            print(l, clock, x)
            sum += x * clock
        x += arg

print(sum)