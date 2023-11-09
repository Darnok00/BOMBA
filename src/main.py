from __future__ import print_function
from ortools.graph import pywrapgraph

"""
Constants, which shouldn't me modify
"""
CAPACITY_1 = 1
CAPACITY_2 = 2
COST_0 = 0
COST_LOAD = 20
ID_0 = 0
SUPPLIE_0 = 0
"""
Constants, which can be me modify as parameters 
"""
MAX_MARK = 5
NUMBER_ANGELS = 10
NUMBER_BABIES = 20
WEIGHT_MENTORS_MARK = 2
WEIGHT_BABIES_MARK = 3


def create_start_nodes(number_angels, number_baybes):
    nodes = []
    for i in range(number_angels):
        nodes.append(ID_0)
    for i in range(1, number_angels + 1):
        for j in range(0, number_baybes):
            nodes.append(i)
    for i in range(number_angels + 1, number_angels * 3 + 1):
        nodes.append(i)
    return nodes


def create_end_nodes(number_angels, number_baybes):
    nodes = []
    for i in range(1, number_angels + 1):
        nodes.append(i)
    for i in range(0, number_angels):
        for j in range(number_angels + 1, number_angels + number_baybes + 1):
            nodes.append(j)
    for i in range(number_baybes):
        nodes.append(number_angels + number_baybes + 1)
    return nodes


def create_capacities(number_angels, number_baybes):
    nodes = []
    for i in range(number_angels):
        nodes.append(CAPACITY_2)
    for i in range(number_angels * number_baybes + number_baybes):
        nodes.append(CAPACITY_1)
    return nodes


def create_supplies(number_angels, number_baybes):
    nodes = [number_baybes]
    for i in range(number_angels + number_baybes):
        nodes.append(SUPPLIE_0)
    nodes.append(-number_baybes)
    return nodes


def create_costs(number_angels, number_baybes, angels_marks, beybes_marks):
    nodes = []
    for i in range(number_angels):
        nodes.append(COST_0)
    for i in range(number_angels):
        for j in range(number_baybes):
            # This line cause that if mentor give 1 baybes or baybe give 1 or 2 mentors this match will never exist
            if angels_marks[i * number_baybes + j] == 1 or beybes_marks[j * number_angels + i] == 1 or beybes_marks[j * number_angels + i] == 2:
                nodes.append(100000)
            else:
                nodes.append(WEIGHT_MENTORS_MARK * (MAX_MARK - angels_marks[i * number_baybes + j]) +
                             WEIGHT_BABIES_MARK * (MAX_MARK - beybes_marks[j * number_angels + i]))
    for i in range(number_baybes):
        nodes.append(COST_0)
    return nodes

"""
Inputs form google scripts
If u wanna generate a matching with specify pair you should change baybe or mentor mark on 1 below
"""
angels_marks = [4, 3, 4, 3, 3, 3, 3, 3, 3, 4, 4, 3, 4, 3, 3, 4, 3, 4, 4, 1,
                3, 5, 2, 3, 5, 5, 3, 3, 2, 5, 3, 1, 3, 2, 3, 5, 2, 2, 1, 1,
                4, 5, 3, 4, 4, 4, 3, 3, 3, 5, 5, 2, 2, 2, 3, 5, 2, 3, 1, 1,
                3, 1, 3, 5, 1, 1, 5, 3, 3, 5, 5, 1, 4, 3, 3, 5, 1, 5, 1, 1,
                4, 1, 4, 2, 5, 3, 1, 3, 4, 4, 2, 4, 4, 1, 3, 4, 1, 5, 4, 1,
                4, 4, 2, 5, 5, 3, 4, 3, 2, 5, 3, 3, 4, 2, 5, 3, 3, 3, 4, 1,
                3, 3, 3, 5, 5, 3, 2, 3, 4, 5, 4, 4, 3, 2, 3, 3, 3, 3, 4, 1,
                1, 1, 4, 3, 1, 2, 1, 3, 5, 4, 5, 5, 4, 1, 4, 5, 1, 2, 2, 1,
                4, 2, 5, 5, 5, 2, 2, 3, 4, 5, 4, 4, 1, 3, 3, 5, 3, 5, 2, 1,
                1, 1, 1, 5, 5, 1, 1, 3, 5, 5, 5, 1, 5, 1, 3, 1, 1, 1, 1, 5]

babies_marks = [4, 4, 5, 4, 4, 5, 4, 5, 4, 4,
                4, 5, 4, 4, 5, 5, 5, 4, 4, 5,
                3, 4, 4, 3, 3, 4, 4, 2, 4, 5,
                3, 4, 3, 2, 3, 5, 5, 3, 3, 3,
                2, 3, 5, 3, 4, 4, 5, 3, 3, 4,
                4, 3, 5, 3, 3, 5, 5, 4, 3, 3,
                4, 4, 4, 5, 4, 5, 4, 3, 5, 5,
                3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
                3, 3, 4, 3, 4, 2, 4, 3, 4, 3,
                2, 2, 3, 1, 4, 4, 5, 2, 5, 5,
                4, 5, 5, 3, 3, 3, 5, 4, 3, 4,
                1, 3, 4, 1, 2, 1, 5, 5, 2, 3,
                3, 5, 4, 2, 5, 4, 4, 3, 2, 4,
                3, 3, 4, 2, 5, 5, 5, 3, 2, 4,
                3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
                3, 5, 4, 4, 3, 4, 5, 5, 3, 3,
                3, 5, 5, 3, 4, 4, 5, 4, 4, 5,
                5, 5, 5, 5, 5, 4, 5, 5, 5, 4,
                4, 3, 4, 2, 3, 4, 5, 3, 2, 3,
                1, 1, 1, 1, 1, 1, 1, 1, 1, 5]

start_nodes = create_start_nodes(NUMBER_ANGELS, NUMBER_BABIES)
end_nodes = create_end_nodes(NUMBER_ANGELS, NUMBER_BABIES)
capacities = create_capacities(NUMBER_ANGELS, NUMBER_BABIES)
supplies = create_supplies(NUMBER_ANGELS, NUMBER_BABIES)
unit_costs = create_costs(NUMBER_ANGELS, NUMBER_BABIES, angels_marks, babies_marks)
min_cost_flow = pywrapgraph.SimpleMinCostFlow()

for i in range(0, len(start_nodes)):
    min_cost_flow.AddArcWithCapacityAndUnitCost(start_nodes[i], end_nodes[i], capacities[i], unit_costs[i])

for i in range(0, len(supplies)):
    min_cost_flow.SetNodeSupply(i, supplies[i])

if min_cost_flow.Solve() == min_cost_flow.OPTIMAL:
    for i in range(min_cost_flow.NumArcs()):
        if i >= NUMBER_ANGELS and i < NUMBER_ANGELS * NUMBER_BABIES + NUMBER_ANGELS and min_cost_flow.Flow(i) == 1:
            x = int(min_cost_flow.Tail(i))
            y = int(min_cost_flow.Head(i) - NUMBER_ANGELS)
            print("Mentor: ", x - 1, " Baby: ", y - 1, " Mentor  ocenił bejbika na: ",
                  str(angels_marks[(x - 1) * NUMBER_BABIES + y - 1]), " Bejbik oceniał mentora na: ",
                  str(babies_marks[(y - 1) * NUMBER_ANGELS + x - 1]))


else:
    print('There was an issue with the min cost flow input.')

print(min_cost_flow.OptimalCost())
