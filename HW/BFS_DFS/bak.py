#------------------------------------------#
#                 HW #1                    #
#       Author: Justin Weigle              #
#       Edited: 04 Sept 2019               #
#------------------------------------------#
#    Breadth-first vs Depth-first Search   #
#------------------------------------------#

import numpy as np
import csv

sm = int(input("Please pick search method BFS(1) or DFS(2): "))
while(sm != 1 and sm != 2):
    print("Search method choices are 1 or 2")
    sm = int(input("Please pick BFS(1) or DFS(2): "))

sn = int(input("Please enter the starting node (1-200): "))
while(sn < 1 or 200 < sn or type(sn) != int):
    print("Starting node not integer from 1-200")
    sn = int(input("Please enter the starting node (1-200): "))

en = int(input("Please enter the ending node (1-200): "))
while(en < 1 or 200 < en or type(en) != int):
    print("Ending node not integer from 1-200")
    en = int(input("Please enter the ending node (1-200): "))


fn = input("Please enter a csv filename: ")
fn = fn + ".csv"


# Breadth-first search algorithm
def bfs(csv_data):
    None

# Depth-first search algorithm
def dfs(csv_data, cn = None, root = None, visited = list()):
    if(int(csv_data[cn][0]) not in visited):
        visited.append(int(csv_data[cn][0]))
    i = 1
    if(cn != en):
        tmp = int(csv_data[cn][i])
        stack.append(csv_data[cn])
        while(tmp in visited):
            if(i >= len(csv_data[cn])-1):
                root = root + 1
                dfs(csv_data, root, root, visited)
                break
            i = i + 1
            tmp = int(csv_data[cn][i])
        cn = int(tmp)
        print(cn)
        dfs(csv_data, cn, root, visited)
    else:
        print(visited)
        return


# Calls bfs or dfs if sn != en
def check_start_end():
    if(sn == en):
        print("Path = " + str(sn))
    else:
        if(sm == 1):
            print("USING BFS")
            bfs(csv_data, sn)
            print(csv_data[sn])

        if(sm == 2):
            print("USING DFS")
            dfs(csv_data, sn, int(csv_data[sn][0]))

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
