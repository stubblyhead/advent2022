import anytree

class File(anytree.Node):
    def __init__(self,name,size,parent):
        super().__init__(name,parent=parent)
        self.size = size




lines = open('testcase').readlines(-1)
dirs = {'root': File('root',0,parent=None)}
cur = dirs['root']

for l in lines:
    parts = l.strip().split()
    if parts[0].isnumeric():
        print("in dir %s new file of size %s, currently %i" % (cur.name, parts[0], cur.size))
        cur.size += int(parts[0])
        
    if parts[1] == 'ls':
        continue # don't think we need to do anything here

    if parts[1] == 'cd':
        dest = parts[2]
        if dest == '..':
            continue
        if dest == '/':
            continue
        cur = dirs[dest]

    if parts[0] == 'dir':
        print(dirs)
        dirname = parts[1]
        print("looking at %s, parent is %s" % (dirname, cur.name))
        dirs[dirname] = File(dirname, 0, parent=cur)

for pre, fill, node in anytree.RenderTree(dirs['root']):
    print("%s%s" % (pre, node.name))

for d in dirs.values():
    print(d.name, d.size)
    
def backfill(node):
    if node.children == None:
        return node.size
    else:
        for f in node.children:
            node.size += backfill(f)
        return node.size
            

backfill(dirs['root'])

for d in dirs.values():
    print(d.name, d.size)

smalldirs = 0
for d in dirs.values():
    if d.size <= 100000:
        smalldirs += d.size

print(smalldirs)
