f = open('input')
lines = f.readlines(-1)

overlaps = 0

while lines:
    (elfA, elfB) = lines.pop().strip().split(',')
    (aStart, aEnd) = elfA.split('-')
    (bStart, bEnd) = elfB.split('-')
    aStart = int(aStart)
    aEnd = int(aEnd)
    bStart = int(bStart)
    bEnd = int(bEnd)

    if aStart <= bStart:
        if aEnd >= bEnd:
            overlaps += 1

    if bStart <= aStart:
        if bEnd >= aEnd:
            overlaps += 1

print(overlaps)
