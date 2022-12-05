import itertools
import re

lines = open('testcase').readlines(-1)

stacks = [[]] # putting something at the start will make move parsing easier
moves = []

for i in range(len(lines)):
  if lines[i][0] == 'm':  # find first line of moves
    moves = lines[i:]  # put that line to the end in a new list...
    lines = lines[0:i-2]  # and truncate the original to just the stacks
    break

lines = [list(i) for i in itertools.zip_longest(*lines)]  # transpose the array

for i in range(len(lines)):
  if i % 4 == 1:  # only index 1 and every 4th thereafter matters
    for c in lines[i]:
      lines[i][:] = [j for j in lines[i] if j != ' '] # remove all spaces
    stacks.append(lines[i])

for m in moves:
  match = re.search(r"(\d+).*(\d+).*(\d+)", m) # get the numbers out
  num = int(match.group(1))
  source = int(match.group(2))
  dest = int(match.group(3))

  stacks[dest] = stacks[source][0:num] + stacks[dest]
  stacks[source] = stacks[source][num:]

answer = ''
for s in stacks:
    if s == []:
        continue
    answer += s[0]
print(answer)
