from copy import deepcopy

class Cell:
    def __init__(self, height):
        if height == 'S':
            self.height = 0
        elif height == 'E':
            self.height = 27
        else:
            self.height = ord(height) - 96

        self.parent = None
        self.moves = []

class Grid(list):
    def __init__(self, grid):  # grid as matrix of values
        self.topo = []
        thisrow = []
        self.start = []
        self.dest = []
        for row in grid:
            for col in row:
                thisrow.append(Cell(col))
            self.topo.append(thisrow)
            thisrow = []
    
        for i in range(len(self.topo)):
            for j in range(len(self.topo[i])):
                # not sure if these will be useful, but why not
                if self.topo[i][j].height == 0:
                    self.start = [i,j]
                    self.topo[i][j].height = 1
                elif self.topo[i][j].height == 27:
                    self.dest = [i,j]
                    self.topo[i][j].height = 26

                # check above
                if i > 0:
                    if self.topo[i-1][j].height - self.topo[i][j].height <= 1:
                        self.topo[i][j].moves.append([i-1,j])
                #check below
                if i < len(self.topo) - 1:
                    if self.topo[i+1][j].height - self.topo[i][j].height <= 1:
                        self.topo[i][j].moves.append([i+1,j])
                #check right
                if j < len(self.topo[i]) - 1:
                    if self.topo[i][j+1].height - self.topo[i][j].height <= 1:
                        self.topo[i][j].moves.append([i,j+1])
                #check left
                if j > 0:
                    if self.topo[i][j-1].height - self.topo[i][j].height <= 1:
                        self.topo[i][j].moves.append([i,j-1])

    def print(self):
        thisline = ''
        for i in self.topo:
            for j in i:
                thisline += chr(j.height + 96)

            print(thisline)
            thisline = ''

    def printpath(self):
        path = []
        cur = self.dest
        while cur != self.start:
            (cur_row, cur_col) = cur
            path.append(cur)
            cur = self.topo[cur_row][cur_col].parent
        temp = deepcopy(self)
        
        for step in range(len(path)):
            (cur_row, cur_col) = path[step]
            if temp.topo[cur_row][cur_col].height == 27:
                temp.topo[cur_row][cur_col].height = 'E'
            elif temp.topo[cur_row][cur_col].height == 0:
                temp.topo[cur_row][cur_col].height = 'S'
            else:
                (prev_row, prev_col) = temp.topo[cur_row][cur_col].parent
                if prev_row > cur_row:
                    temp.topo[prev_row][prev_col].height = '↑'
                elif prev_row < cur_row:
                    temp.topo[prev_row][prev_col].height = '↓'
                elif prev_col > cur_col:
                    temp.topo[prev_row][prev_col].height = '←'
                elif prev_col < cur_col:
                    temp.topo[prev_row][prev_col].height = '→'
        thisline = ''
        for i in temp.topo:
            for j in i:
                if str(j.height).isnumeric():
                    thisline += '.'
                else:
                    thisline += j.height
            print(thisline)
            thisline = ''
        


with open('input') as f:
    data = f.read().split('\n')

grid = [ [ i for i in list(row) ] for row in data ]



def bfs(grid): 
    frontier = [grid.start]
    i = 1
    level = { tuple(grid.start) : 0}
    while frontier:
        next = []
        for subtree_root in frontier:
            (row,col) = subtree_root
            if subtree_root == grid.dest:
                next = []
                break
            for d in grid.topo[row][col].moves:
                d = tuple(d)
                if d not in level:
                    level[d] = i
                    next.append(d)
                    grid.topo[d[0]][d[1]].parent = subtree_root
        frontier = next
        i += 1
    print(level[tuple(grid.dest)])
    
 



puzzle = Grid(grid)

bfs(puzzle)

#puzzle.printpath()