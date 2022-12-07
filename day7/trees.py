import anytree


lines = open('testcase').readlines(-1)
dirs = {'root': anytree.Node('root')}
cur = dirs['root']


for l in lines:
    parts = l.strip().split()
    if parts[0].isnumeric():
        continue # skipping files for now
    
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
        dirname = parts[1]
        print("looking at %s, parent is %s" % (dirname, cur.name))
        dirs[dirname] = anytree.Node(dirname, parent=cur)
        


for pre, fill, node in anytree.RenderTree(dirs['root']):
    print("%s%s" % (pre, node.name))

print(dirs)
for d in dirs.values():
    print(d.parent)
