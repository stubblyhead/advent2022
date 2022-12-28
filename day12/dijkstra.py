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
                elif self.topo[i][j].height == 27:
                    self.dest = [i,j]

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


with open('testcase') as f:
    data = f.read().split('\n')

grid = [ [ i for i in list(row) ] for row in data ]



def bfs(grid):  # will flesh this out
    visited = [grid.start]
    while visited:
        subtree_root = visited.pop()
        if subtree_root == grid.dest:
            break # found the destination, so we don't need to keep looking
        (sub_row, sub_col) = subtree_root
        for d in grid.topo[sub_row][sub_col].moves:
            (next_row,next_col) = d
            if grid.topo[next_row][next_col].parent == None:
                grid.topo[next_row][next_col].parent = subtree_root
                visited.append(d)
    path_length = 0
    cur = grid.dest
    while cur != grid.start:
        path_length += 1
        (row,col) = cur
        cur = grid.topo[row][col].parent

    print(path_length)




puzzle = Grid(grid)

bfs(puzzle)