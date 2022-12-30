with open('input') as f:
    data = f.read()

pairs = data.split('\n\n')

def cmp(l, r):
    result = 0  # pass through until we know we can do otherwise
    while l:
        if abs(result) == 1:  # a later invocation determined if the pair is in order
            return result
        
        if type(l) == int and type(r) == int: # comparing ints to ints
            if l < r:
                return 1
            elif l > r:
                return -1
            else:
                return 0
        elif type(l) == list and type(r) == list: # comparing lists to lists
            if len(r) == 0: # if RHS runs out first it's not in the right order
                return -1
            else:
                result = cmp(l.pop(0),r.pop(0)) # compare the first values in LHS and RHS
        else:
            if type(l) == int:  # one int and one list; need to reinvoke with the int in a list
                result = cmp([l], r)
            else:
                result = cmp(l, [r])
    else:
        if type(r) == list and len(r) > 0 and result != -1:  # determined correct order on l[-1] but r still had some values
            return 1
    return result
    

sum = 0

for i in range(len(pairs)):
    (left, right) = pairs[i].split('\n')
    left = eval(left)  # this seems like cheating, but probably will come back to bite me
    right = eval(right)
    
    thispair = cmp(left,right)
    if thispair == 1:
        sum += i + 1

print(sum)
