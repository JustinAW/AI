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
    print("USING BFS")


# Depth-first search algorithm
def dfs(csv_data, visited = None):
    print("USING DFS")
    #print(csv_data[sn][0])
    #print(csv_data[sn])
    visited.append(csv_data[sn][0])
    stack.append(csv_data.pop(sn))


# Calls bfs or dfs if sn != en
def check_start_end():
    if(sn == en):
        print("Path = " + str(sn))
    else:
        if(sm == 1):
            bfs(csv_data,)

        if(sm == 2):
            dfs(csv_data)

f = open(fn, 'r')
reader = csv.reader(f)
csv_data = []
for row in reader:
    csv_data.append(row)

# Stack for DFS
stack = list()
# Start program
check_start_end()
