f = open('input')

wrongscore = 0
rightscore = 0
while True:
    line = (f.readline()).strip()
    if len(line) == 0:
        break
    if line == 'A X':
        wrongscore = wrongscore + 3 + 1
        rightscore += 3
    elif line == 'A Y':
        wrongscore = wrongscore + 6 + 2
        rightscore += 4
    elif line == 'A Z':
        wrongscore += 3
        rightscore += 8
    elif line == 'B X':
        wrongscore += 1
        rightscore += 1
    elif line == 'B Y':
        wrongscore = wrongscore + 3 + 2
        rightscore += 5
    elif line == 'B Z':
        wrongscore = wrongscore + 6 + 3
        rightscore += 9
    elif line == 'C X':
        wrongscore = wrongscore + 6 + 1
        rightscore += 2
    elif line == 'C Y':
        wrongscore += 2
        rightscore += 6
    elif line == 'C Z':
        wrongscore = wrongscore + 3 + 3
        rightscore += 7

print(wrongscore)
print(rightscore)
