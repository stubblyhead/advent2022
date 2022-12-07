class Dir:
    def __init__():
        contents = []

    def add(name, size=0):
        contents.append({'Name': name, 'Size': size})

    def calc():
        size = 0
        for o in contents:
            if isinstance(o, Dir):
                o['Size'] = o.calc()
            size += o['Size']



lines = open('testcase').readlines(-1)

