#------------------------------------------#
#                 HW #1                    #
#       Author: Justin Weigle              #
#       Edited: 02 Sept 2019               #
#------------------------------------------#
#    Breadth-first vs Depth-first Search   #
#------------------------------------------#

import numpy as np

sm = int(input("Please pick BFS(1) or DFS(2): "))
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
def dfs(csv_data):
    print("USING DFS")



csv_data = np.genfromtxt(fn, delimiter = ',')


if(sm == 1):
    bfs(csv_data)

if(sm == 2):
    dfs(csv_data)
