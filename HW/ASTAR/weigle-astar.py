#-------------------------------------------#
#                 HW #2                     #
#       Author: Justin Weigle               #
#       Edited: 18 Sept 2019                #
#-------------------------------------------#
#           A* Search Algorithm             #
#-------------------------------------------#

import csv
from queue import PriorityQueue
import math


def astar(graph, start, goal, h):
    open_set = PriorityQueue()
    open_set.put(start)
    came_from = []
    g_score = [float("inf")] * len(graph)
    for i in range(1, len(graph)):
        if graph[i][0] == start:
            g_score[i] = 0
    f_score = [math.inf] * len(h)
    f_score[int(start)] = h[int(start)]

    current = math.inf
    while open_set:
        for node in open_set.queue:
            if int(node) < float(current):
                current = node
        if current == goal:
            return "Goal Reached"

        open_set.get()



if __name__=="__main__":
    fn = "EdgeWeights.csv"

    f = open(fn, 'r')
    reader = csv.reader(f)
    edgeweights = []
    for row in reader:
        edgeweights.append(row)

    fn = "minCosts.csv"

    f = open(fn, 'r')
    reader = csv.reader(f)
    mincosts = []
    for row in reader:
        mincosts.append(row)

    sn = "5"
    goal = "10"

    result = astar(edgeweights, sn, goal, mincosts)
    print(result)
