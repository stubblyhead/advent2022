f = open('input')

cals = [0]
i = 0
while True:
    line = f.readline()
    if line == '\n':
        i = i + 1
        cals.append(0)
        continue
    if len(line) == 0:
        break
    cals[i] = cals[i] + int(line)
    
print(max(cals))
cals.sort()
print(sum(cals[-3:]))
