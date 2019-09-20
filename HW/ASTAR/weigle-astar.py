#-------------------------------------------#
#                 HW #2                     #
#       Author: Justin Weigle               #
#       Edited: 19 Sept 2019                #
#-------------------------------------------#
#           A* Search Algorithm             #
#-------------------------------------------#

import csv
from queue import PriorityQueue
import math
from collections import defaultdict

def reconstruct_path(came_from, current):
    total_path = [current]
    while current in came_from.keys():
        current = came_from[current]
        total_path.insert(0, current)
    return total_path

def astar(edgeweights, start, goal, h):
    # Create needed structures
#    open_set = PriorityQueue()
    open_set = set()
    closed_set = set()
    came_from = {}
    g_score = {}
    f_score = {}

    for node in edgeweights:
        g_score[node] = math.inf

    for node in edgeweights:
        f_score[node] = math.inf

    open_set.add(start)
    g_score[start] = 0
    if(int(start) < int(goal)):
        f_score[start] = h[start][0][int(goal)-1]
    else:
        f_score[start] = h[goal][0][int(start)-1]

    # find the best path
    while open_set:
        min_score = math.inf
        for node in open_set:
            if float(f_score[node]) < min_score:
                min_score = f_score[node]
                current = node
        if(current == goal):
            return reconstruct_path(came_from, current)

        open_set.remove(current)
        closed_set.add(current)
        for neighbor in edgeweights[current]:
            if neighbor[0] in closed_set:
                continue

            tentative_g_score = float(g_score[current]) + float(neighbor[1])
            if tentative_g_score < g_score[neighbor[0]]:
                came_from[neighbor[0]] = current
                g_score[neighbor[0]] = tentative_g_score
                if(int(neighbor[0]) < int(goal)):
                    f_score[neighbor[0]] = g_score[neighbor[0]] + float(h[neighbor[0]][0][int(goal)-1])
                else:
                    f_score[neighbor[0]] = g_score[neighbor[0]] + float(h[goal][0][int(neighbor[0])-1])
                if(neighbor[0] not in open_set):
                    open_set.add(neighbor[0])

    return "Failure"

def calc_cost(edgeweights, path, goal):
    cost = 0
    for node in path:
        if node != goal:
            cost += float(edgeweights[node][0][1])
            print(float(edgeweights[node][0][1]))

    return cost


if __name__=="__main__":
    fn = "EdgeWeights.csv"

    f = open(fn, 'r')
    reader = csv.reader(f)
    edgeweights = defaultdict(list)
    for row in reader:
        if row:
            edgeweights[row[0]].append([row[1], row[2]])
    f.close()
    """
    print(edgeweights['1']) #prints the whole set of lists tied to 1
    print(edgeweights['1'][0]) #prints the list tied to 1 at 0
    print(edgeweights['1'][0][0]) #prints the 0th element of ^
    """

    fn = "minCosts.csv"

    f = open(fn, 'r')
    reader = csv.reader(f)
    mincosts = defaultdict(list)
    for row in reader:
        if row:
            mincosts[row[0]].append(row[1:])
    f.close()

    start = "5"
    goal = "10"

    path = astar(edgeweights, start, goal, mincosts)
    cost = calc_cost(edgeweights, path, goal)
    print(path)
    print(cost)
