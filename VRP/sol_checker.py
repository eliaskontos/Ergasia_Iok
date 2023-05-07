import random
import math

class Node:
    def __init__(self, id, dem, xx, yy):
        self.ID = id
        self.demand = dem
        self.x = xx
        self.y = yy


def build_model():
    random.seed(1)
    capacity = 16
    vehicles = 30
    tare_weight = 8
    all_nodes = []
    customers = []
    depot = Node(0, 0, 50, 50)
    all_nodes.append(depot)

    for i in range(0, 100):
        id = i + 1
        dem = random.randint(1, 6)
        xx = random.randint(0, 100)
        yy = random.randint(0, 100)
        cust = Node(id, dem, xx, yy)
        all_nodes.append(cust)
        customers.append(cust)

    return all_nodes, vehicles, capacity, tare_weight


def distance(from_node, to_node):
    dx = from_node.x - to_node.x
    dy = from_node.y - to_node.y
    dist = math.sqrt(dx ** 2 + dy ** 2)
    return dist


def calculate_route_details(nodes_sequence):
    rt_load = 0
    rt_cost = 0
    for i in range(len(nodes_sequence)):
        from_node = nodes_sequence[i]
        rt_load += from_node.demand

    tot_load = rt_load + tare_weight

    for i in range(len(nodes_sequence) - 1):
        from_node = nodes_sequence[i]
        to_node = nodes_sequence[i+1]
        rt_cost += tot_load * distance(from_node, to_node)
        tot_load = tot_load - to_node.demand
    return rt_cost, rt_load



def test_solution(file_name, all_nodes, vehicles, capacity):
    all_lines = list(open(file_name, "r"))
    line = all_lines[1]
    cost_reported = float(line.strip())
    cost_calculated = 0

    times_visited = {}
    for i in range(1, len(all_nodes)):
        times_visited[i] = 0

    line = all_lines[3]
    vehs_used = int(line.strip())

    if vehs_used > vehicles:
        print('More than', vehicles, 'used in the solution')
        return

    separator = ','
    line_counter = 4
    for i in range(vehs_used):
        ln = all_lines[line_counter]
        ln = ln.strip()
        no_commas = ln.split(sep=separator)
        ids = [int(no_commas[i]) for i in range(len(no_commas))]
        nodes_sequence = [all_nodes[idd] for idd in ids]
        rt_cost, rt_load = calculate_route_details(nodes_sequence)
        for nn in range(1,len(nodes_sequence)):
            n_in = nodes_sequence[nn].ID
            times_visited[n_in] = times_visited[n_in] + 1
        # check capacity constraints
        if rt_load > capacity:
            print('Capacity violation. Route', i, 'total load is', rt_load)
            return
        cost_calculated += rt_cost
        line_counter += 1
    # check solution objective
    if abs(cost_calculated - cost_reported) > 0.001:
        print('Cost Inconsistency. Cost Reported', cost_reported, '--- Cost Calculated', cost_calculated)
        return

    # Check number of times each customer is visited
    for t in times_visited:
        if times_visited[t] != 1:
            print('Error: customer', t, 'not present once in the solution')
            return

    # everything is ok
    print('Solution is ΟΚ. Total Cost:', cost_calculated)

all_nodes, vehicles, capacity, tare_weight = build_model()
test_solution(r"C:\Users\elias\source\repos\eliaskontos\Ergasia_Iok\VRP\example_solution.txt", all_nodes, vehicles, capacity)