sum = 0
with open('input') as f:
    for line in f:
        line = line.strip()
        left = line[0:int(len(line)/2)]
        right = line[int(len(line)/2):]
        lset = {i for i in left}  # using sets here may come back to bite me in the ass
        rset = {i for i in right}

        dupe = (lset & rset).pop()
        
        if dupe.isupper():
            sum += (ord(dupe) - 38)
        else:
            sum += (ord(dupe) - 96)

print(sum)

sum = 0
f = open('testcase')
lines = f.readlines(-1)
while lines:
    aset = {i for i in lines.pop()}
    bset = {i for i in lines.pop()}
    cset = {i for i in lines.pop()}

    dupe = (aset & bset & cset).pop()
    
    if dupe.isupper():
        sum += (ord(dupe) - 38)
    else:
        sum += (ord(dupe) - 96)

print(sum)

