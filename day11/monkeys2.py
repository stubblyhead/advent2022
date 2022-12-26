class Monkey:
    def __init__(self, items, operation, test, onering): # items in list, operation is RHS of equation, test is array with comparison, true destination, and false destination
        self.items = items
        self.operation = operation.split()
        self.modulo = int(test[0])
        self.true_dest = int(test[1])
        self.false_dest = int(test[2])
        self.count = 0
        self.onering = onering

    def catch(self, new_item):
        self.items.append(new_item)

    def throw(self, receiver):
        cur_item = self.items.pop(0)
        receiver.catch(cur_item)

    def change_worry(self):
        op = self.operation[1]
        if op == '*':
            if self.operation[2] == 'old':  # second operand can only be old for multiplication
                self.items[0] *= self.items[0]
                self.items[0] %= onering
            else:
                self.items[0] *= int(self.operation[2])
                self.items[0] %= onering

        elif op == '+':
            self.items[0] += int(self.operation[2])
            self.items[0] %= onering

        #self.items[0] = int(self.items[0]/3) # always divide by three after monkey looks at item
        self.count += 1 # increment inspection counter
    
    def test_item(self):
        if self.items[0] % self.modulo == 0:
            return self.true_dest
        else:
            return self.false_dest


with open('input') as f:
    data = f.read()

monkeys = []
monkey_list = data.split('\n\n')
lines = data.split('\n')
onering = 1
for l in lines:
    if l[2:6] == 'Test':
        onering *= int(l.split()[-1])

for m in monkey_list:
    lines = m.split('\n')
    items = [int(i) for i in lines[1].split(': ')[1].split(',')]
    operation = lines[2].split('= ')[1]
    test = []
    test.append(lines[3].split()[-1])
    test.append(lines[4].split()[-1])
    test.append(lines[5].split()[-1])
    monkeys.append(Monkey(items, operation, test, onering))


for n in range(10000):  # go through 20 rounds
    for m in monkeys:  # every monkey gets a turn
        for i in range(len(m.items)):  # iterating by item will probably cause issues since we're changing the list as we go
            m.change_worry()  # update the value of the current object
            receiver = m.test_item()  # figure out who gets the item next
            m.throw(monkeys[receiver]) # throw it to that monkey

counts = []
for m in monkeys:
    counts.append(m.count)
counts.sort()
print(counts)
print(counts[-1] * counts[-2])