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
from collections import defaultdict

def astar(edgeweights, start, goal, h):
    open_set = PriorityQueue()
    closed_set = []
    open_set.put(start)

    print(edgeweights[start])
    for path in edgeweights[start]:
        if(int(path[0]) < int(goal)):
            f_score = float(path[1]) + float(h[path[0]][0][int(goal)-1])
            print(h[path[0]][0][int(goal)-1])
        else:
            f_score = float(path[1]) + float(h[goal][0][int(path[0])-1])
        print(f_score)

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
    #mincosts = []
    mincosts = defaultdict(list)
    for row in reader:
        if row:
            mincosts[row[0]].append(row[1:])
    f.close()

    sn = "5"
    goal = "10"

    result = astar(edgeweights, sn, goal, mincosts)
    print(result)
