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
        if aEnd >= bStart:
            overlaps += 1
            continue  # ranges could be identical, need to avoid double-counting

    if bStart <= aStart:
        if bEnd >= aStart:
            overlaps += 1

print(overlaps)
