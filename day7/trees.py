import anytree

class File(anytree.Node):
    def __init__(self,name,size,parent):
        super().__init__(name,parent=parent)
        self.size = size

fs = []
parent = None
cur = None

lines = open('testcase').readlines(-1)

for l in lines:
    parts = l.strip().split()
        
    if parts[1] == 'ls':
        continue # don't think we need to do anything here

    if parts[1] == 'cd':
        dest = parts[2]
        if dest == '..':
            cur = cur.parent
            parent = cur.parent
        else:
            parent = cur
            fs.append(File(dest, 0, parent = parent))
            cur = fs[-1]

    if parts[0] == 'dir':
        continue

    if parts[0].isnumeric():
        fs.append(File(parts[1],int(parts[0]),parent = cur))

def backfill(node):
    if node.children == None:
        return node.size
    else:
        for f in node.children:
            node.size += backfill(f)
        return node.size
            

#for pre, fill, node in anytree.RenderTree(fs[0]):
#    print("%s%s %i" % (pre, node.name, node.size))

backfill(fs[0])


smalldirs = 0
for f in fs:
    if f.size <= 100000 and len(f.children) > 0:
      smalldirs += f.size

print(smalldirs)

avail = 70000000 - fs[0].size
needed = 30000000 - avail

smallest = fs[0]

for f in fs:
    if f.size >= needed and len(f.children) > 0:
        if f.size < smallest.size:
            smallest = f

print(smallest.name)

