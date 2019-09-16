#-------------------------------------------#
#                 HW #2                     #
#       Author: Justin Weigle               #
#       Edited: 15 Sept 2019                #
#-------------------------------------------#
#           A* Search Algorithm             #
#-------------------------------------------#

import csv
from queue import PriorityQueue


def astar(graph, start, goal, h):
    open_set = PriorityQueue()
    open_set.put(start)
    came_from = set()

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

    astar(edgeweights, sn, goal, mincosts)
