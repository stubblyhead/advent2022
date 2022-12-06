signal = open('input').readline()
for i in range(len(signal)):
  chunk = signal[i:i+4]
  chunkset = {j for j in chunk}
  if len(chunkset) == 4:
      print(i+4)
      break

for i in range(len(signal)):
    chunk = signal[i:i+14]
    chunkset = {j for j in chunk}
    if len(chunkset) == 14:
        print(i+14)
        break
