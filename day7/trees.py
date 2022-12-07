import anytree


lines = open('testcase').readlines(-1)
dirs = {'root': [anytree.Node('root'),0]}
cur = dirs['root'][0]


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
        cur = dirs[dest][0]

    if parts[0] == 'dir':
        print(dirs)
        dirname = parts[1]
        print("looking at %s, parent is %s" % (dirname, cur.name))
        dirs[dirname] = []
        dirs[dirname].append(anytree.Node(dirname, parent=cur))
        dirs[dirname].append(0)


for pre, fill, node in anytree.RenderTree(dirs['root'][0]):
    print("%s%s" % (pre, node.name))

for d in dirs.values():
    print(d[0].parent)
