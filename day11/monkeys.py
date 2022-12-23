class Monkey:
    def __init__(self, items, operation, test): # items in list, operation is RHS of equation, test is array with comparison, true destination, and false destination
        self.items = items
        self.operation = operation.split()
        self.modulo = int(test[0])
        self.true_dest = int(test[1])
        self.false_dest = int(test[2])

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
            else:
                self.items[0] *= int(self.operation[2])
        elif op == '+':
            self.items[0] += int(self.operation[2])
        self.items[0] = int(self.items[0]/3) # always divide by three after monkey looks at item
    
    def test_item(self):
        if self.items[0] % self.modulo == 0:
            return self.true_dest
        else:
            return self.false_dest


with open('testcase') as f:
    data = f.read()

monkeys = []
monkey_list = data.split('\n\n')

for m in monkey_list:
    lines = m.split('\n')
    items = [int(i) for i in lines[1].split(': ')[1].split(',')]
    operation = lines[2].split('= ')[1]
    test = []
    test.append(lines[3].split()[-1])
    test.append(lines[4].split()[-1])
    test.append(lines[5].split()[-1])
    monkeys.append(Monkey(items, operation, test))


# going through one round for now
for m in monkey_list:  # every monkey gets a turn
    for i in len(m.items):  # iterating by item will probably cause issues since we're changing the list as we go
        m.change_worry()  # update the value of the current object
        receiver = m.test_item()  # figure out who gets the item next
        m.throw(monkey_list[receiver]) # throw it to that monkey

for m in monkey_list:
    print(m.items)