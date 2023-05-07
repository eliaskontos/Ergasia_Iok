import random

class Node:
    def __init__(self, id, dem, xx, yy):
        self.ID = id
        self.demand = dem
        self.x = xx
        self.y = yy

# seed
random.seed(1)
all_nodes = []
customers = []
depot = Node(0, 0, 50, 50)
all_nodes.append(depot)

for i in range(0, 100):
    id= i + 1
    dem= random.randint(1, 6)
    xx = random.randint(0, 100)
    yy = random.randint(0, 100)
    cust = Node(id, dem, xx, yy)
    all_nodes.append(cust)
    customers.append(cust)



