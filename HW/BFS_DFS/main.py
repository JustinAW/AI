#------------------------------------------#
#                 HW #1                    #
#       Author: Justin Weigle              #
#       Edited: 02 Sept 2019               #
#------------------------------------------#
#    Breadth-first vs Depth-first Search   #
#------------------------------------------#

import numpy as np

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
def dfs(csv_data, current_y = None, current_x = None, visited = None):
    print("USING DFS")
    #print(csv_data[:,0])
    #print(csv_data[0:2])
    #print(csv_data[sn][0])


# Calls bfs or dfs if sn != en
def check_start_end():
    if(sn == en):
        print("Path = " + str(sn))
    else:
        if(sm == 1):
            bfs(csv_data, sn, 1)

        if(sm == 2):
            dfs(csv_data, sn, 1)

# Read in csv file fn
csv_data = np.genfromtxt(fn, delimiter = ',')

# Start program
check_start_end()
