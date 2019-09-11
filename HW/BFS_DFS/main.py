#-------------------------------------------#
#                  W #1                     #
#       Author: Justin Weigle               #
#       Edited: 11 Sept 2019                #
#-------------------------------------------#
#    Breadth-first vs Depth-first Search    #
#-------------------------------------------#

import numpy as np
import csv
import queue

#sm = int(input("Please pick search method BFS(1) or DFS(2): "))
#while(sm != 1 and sm != 2):
#    print("Search method choices are 1 or 2")
#    sm = int(input("Please pick BFS(1) or DFS(2): "))
sm = 1

sn = int(input("Please enter the starting node (1-200): "))
while(sn < 1 or 200 < sn or type(sn) != int):
    print("Starting node not integer from 1-200")
    sn = int(input("Please enter the starting node (1-200): "))

en = int(input("Please enter the ending node (1-200): "))
while(en < 1 or 200 < en or type(en) != int):
    print("Ending node not integer from 1-200")
    en = int(input("Please enter the ending node (1-200): "))


#fn = input("Please enter a csv filename: ")
#fn = fn + ".csv"
fn = "BFS_DFS.csv"


# Breadth-first search algorithm
def bfs(csv_data, cn, visited = None):
    q = queue.Queue()
    if(visited is None):
        visited = []
    q.put(cn)
    while not q.empty():
        cn = q.get()
        if cn == en:
            print("goal")
            return visited
        for n in csv_data[int(cn)]:
            if n not in visited:
                print("dang it bobby")
                visited.append(n)
                q.put(int(n))


# Depth-first search algorithm
def dfs(csv_data, cn, visited = None): 
    if(visited is None):
        visited = []
    else:
        visited.append(cn)

    for n in csv_data[int(cn)]:
        if n not in visited:
            visited = dfs(csv_data, n, visited)
        
    return visited


# Calls bfs or dfs if sn != en
def check_start_end():
    if(sn == en):
        print("Path = " + str(sn))
    else:
        if(sm == 1):
            print("USING BFS")
            path = bfs(csv_data, sn)
            print(path)

        if(sm == 2):
            print("USING DFS")
            traversal = dfs(csv_data, sn)
            print("DFS traversal")
            path = ''
            found = False
            for i in traversal:
                path = path + str(i) + " - "
                if(int(i) == en):
                    found = True
                    path = path.rstrip("- ") 
                    break
            if(found):
                print(path)
            else:
                print("No path between nodes")


f = open(fn, 'r')
reader = csv.reader(f)
csv_data = []
for row in reader:
    csv_data.append(row)

for row in csv_data:
    blankcount = row.count('')
    for i in range(0, blankcount):
        row.pop()

# Stack for DFS
stack = list()
# Start program
check_start_end()
