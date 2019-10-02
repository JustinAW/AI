#---------------------------------------#
#               HW #3                   #
#       Author: Justin Weigle           #
#       Edited: 30 Sep 2019             #
#---------------------------------------#
#       Genetic Algorithm               #
#---------------------------------------#

import random
from math import cos, sin, pi, hypot, inf

"""
define the distance formula for determining the distance of a snake at a
location 'loc' from the goal
"""
dist = lambda loc, goal : hypot(goal[0] - loc[0], goal[1] - loc[1])

class Snake ():
    def __init__(self, start, max_steps):
        self.alphas = []
        for i in range(max_steps):
            self.alphas.append([random.uniform(0, pi), random.uniform(0, (pi/2))])
        self.loc = start
        self.path = []
        self.eval = inf
        self.select_prob = 0

    def hunt(self):
        #if the path already exists, reset it
        if self.path:
            self.loc = start
            self.path = []
        for i in range(max_steps):
            self.loc = [
                    self.loc[0] + cos(self.alphas[i][0]), 
                    self.loc[1] + sin(self.alphas[i][1])
            ]
            self.path.append(self.loc)

def gen_snakes(start, opts):
    snakes = []
    for i in range(opts["PopulationSize"]):
        snakes.append(Snake(start, opts["MaxSteps"]))

    return snakes

def evaluate(snake, goal, playground):
    distances = []
    for coord in snake.path:
        distances.append(dist(coord, goal))
    print(distances[24])

if __name__=="__main__":
    random.seed(3295)
    # set things up
    playground = [(0,32), (0,18)]

    max_steps = 25

    start = [1, 1]
    goal = [23, 10]

    opts = dict()
    opts.update({
        "PopulationSize":50,
        "Generations":1000,
        "MaxSteps":25,
    })

    snakes = gen_snakes(start, opts)

#    snake0_hunt = snakes[0].hunt()
#    print(snake0_hunt)

    for snake in snakes:
        snake.hunt()

    for snake in snakes:
        evaluate(snake, goal, playground)
