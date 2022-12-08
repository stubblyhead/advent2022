lines = open('testcase')
grid = []

for l in lines:
    grid.append(list(l.strip()))

def get_col(a, col):
    col = []
    for r in a:
        col.apend(r)
    return col

def get_row(a,row):
    return row[a]



