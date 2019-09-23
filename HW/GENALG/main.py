#---------------------------------------#
#               HW #3                   #
#       Author: Justin Weigle           #
#       Edited: 23 Sep 2019             #
#---------------------------------------#
#       Genetic Algorithm               #
#---------------------------------------#

import numpy as np

def set_start_goal(playground, start, goal):
    """
    Sets the start and goal locations for a playground
    
    playground
        :type: numpy.zeros()
        :param: multidimensional numpy array of all zeros
    start
        :type:  list
        :param: list of 2 integers [x, y], coords for playground start

    goal
        :type: list
        :param: list of 2 integers [x, y], coords for playground goal
    """
    playground[start[0], start[1]] = 2
    playground[goal[0], goal[1]] = 3
    print(playground)
    return playground

def get_playground(width, height):
    """
    Returns a playground of dimensions width x height
    """
    playground = np.zeros((width, height))
    return playground

if __name__=="__main__":
    # set things up
    playground = get_playground(width = 32, height = 18)

    max_steps = 22

    start = [1, 1]
    goal = [23, 10]

    playground = set_start_goal(playground, start, goal)

    # obstacles
#    obst1 = None
#    obst2 = None
#    obst3 = None

    opts = dict()
    opts.update({
        "PopulationSize":30,
        "Generations":500,
        "EliteCount":0,
        "TolFun":0.001,
        "StallGenLimit":5000,
        })
