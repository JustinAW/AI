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
import numpy as np


def astar(edgeweights, start, goal, h):
    open_set = PriorityQueue()
    open_set.put(start)
    closed_set = PriorityQueue()
    came_from = []
    g_score = [math.inf] * 202
    g_score[int(start)] = 0
    f_score = [math.inf] * len(h)
    f_score[int(start)] = h[int(start)]

    current = math.inf
    while open_set:
        for node in open_set.queue:
            if int(node) < float(current):
                current = node
        if current == goal:
            return "Goal Reached"

        open_set.get(current)
        closed_set.put(current)


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
