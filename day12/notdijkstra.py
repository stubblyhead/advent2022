from copy import deepcopy

class Cell:
    def __init__(self, height):
        if height == 'E':
            self.height = 27
        else:
            self.height = ord(height) - 96

        self.parent = None
        self.moves = []

class Grid(list):
    def __init__(self, grid):  # grid as matrix of values
        self.topo = []
        thisrow = []
        self.dest = []
        for row in grid:
            for col in row:
                thisrow.append(Cell(col))
            self.topo.append(thisrow)
            thisrow = []
    
        for i in range(len(self.topo)):
            for j in range(len(self.topo[i])):
                # not sure if these will be useful, but why not
                if self.topo[i][j].height == 27:
                    self.dest = [i,j]
                    self.topo[i][j].height = 26

                # check above
                if i > 0:
                    if self.topo[i-1][j].height - self.topo[i][j].height >= -1: # changing these to go backwards
                        self.topo[i][j].moves.append([i-1,j])
                #check below
                if i < len(self.topo) - 1:
                    if self.topo[i+1][j].height - self.topo[i][j].height >= -1:
                        self.topo[i][j].moves.append([i+1,j])
                #check right
                if j < len(self.topo[i]) - 1:
                    if self.topo[i][j+1].height - self.topo[i][j].height >= -1:
                        self.topo[i][j].moves.append([i,j+1])
                #check left
                if j > 0:
                    if self.topo[i][j-1].height - self.topo[i][j].height >= -1:
                        self.topo[i][j].moves.append([i,j-1])

with open('input') as f:
    data = f.read().split('\n')

grid = [ [ i for i in list(row) ] for row in data ]



def bfs(grid): 
    frontier = [grid.dest]
    i = 1
    level = { tuple(grid.dest) : 0}  # easiest way is to start at the top and go backwards 
    while frontier: 
        next = []
        for subtree_root in frontier:
            (row,col) = subtree_root
            if grid.topo[row][col].height == 1:
                print(level[(row,col)])
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

    
 



puzzle = Grid(grid)

bfs(puzzle)

