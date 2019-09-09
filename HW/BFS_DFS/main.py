#------------------------------------------#
#                 HW #1                    #
#       Author: Justin Weigle              #
#       Edited: 09 Sept 2019               #
#------------------------------------------#
#    Breadth-first vs Depth-first Search   #
#------------------------------------------#

import numpy as np
import csv

#sm = int(input("Please pick search method BFS(1) or DFS(2): "))
#while(sm != 1 and sm != 2):
#    print("Search method choices are 1 or 2")
#    sm = int(input("Please pick BFS(1) or DFS(2): "))
sm = 2

#sn = int(input("Please enter the starting node (1-200): "))
#while(sn < 1 or 200 < sn or type(sn) != int):
#    print("Starting node not integer from 1-200")
#    sn = int(input("Please enter the starting node (1-200): "))
sn = 1

#en = int(input("Please enter the ending node (1-200): "))
#while(en < 1 or 200 < en or type(en) != int):
#    print("Ending node not integer from 1-200")
#    en = int(input("Please enter the ending node (1-200): "))
en = 5


#fn = input("Please enter a csv filename: ")
#fn = fn + ".csv"
fn = "BFS_DFS.csv"


# Breadth-first search algorithm
def bfs(csv_data):
    None


# Depth-first search initialization
def dfs_init(csv_data):
    dfs(csv_data, int(csv_data[sn][0]))

path = []
# Depth-first search algorithm
def dfs(csv_data, cn, visited = [], path = []):
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
            bfs(csv_data, sn)

        if(sm == 2):
            print("USING DFS")
            dfs(csv_data, sn)
            print(path)


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
