f = open('testcase')
lines = f.readlines(-1)

overlaps = 0

while lines:
    (elfA, elfB) = lines.pop().strip().split(',')
    (aStart, aEnd) = elfA.split('-')
    (bStart, bEnd) = elfB.split('-')

    if aStart <= bStart:
        if aEnd >= bEnd:
            overlaps += 1

    if bStart <= aStart:
        if bEnd >= aEnd:
            overlaps += 1

print(overlaps)
