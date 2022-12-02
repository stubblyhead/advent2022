f = open('testcase')

score = 0
while True:
    line = (f.readline()).strip()
    if len(line) == 0:
        break
    print(line)
    if line == 'A X':
        score = score + 3 + 1
    elif line == 'A Y':
        score = score + 6 + 2
    elif line == 'A Z':
        score += 3
    elif line == 'B X':
        score += 1
    elif line == 'B Y':
        score = score + 3 + 2
    elif line == 'B Z':
        score = score + 6 + 3
    elif line == 'C X':
        score = score + 6 + 1
    elif line == 'C Y':
        score += 2
    elif line == 'C Z':
        score = score + 3 + 3

print(score)
