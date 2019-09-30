#---------------------------------------#
#               HW #3                   #
#       Author: Justin Weigle           #
#       Edited: 30 Sep 2019             #
#---------------------------------------#
#       Genetic Algorithm               #
#---------------------------------------#

import random
from math import cos, sin, pi
from math import degrees as deg

def fitness(playground, loc, alpha):
    new_loc = [loc[0] + deg(cos(alpha)), loc[1] + deg(sin(alpha))]

class snake ():
    def __init__(self, playground, start, goal, max_steps):
        self.alphas = []
        for i in range(max_steps):
            self.alphas.append(random.uniform(0, (pi/2)))
        self.bounds = playground
        self.position = start
        self.food = goal
        self.path = []

    def hunt():
        for i in range(max_steps):
            self.path.append(fitness(bounds, position, alphas[i]))


def gen_snakes(playground, start, goal, opts):
    snakes = []
    for i in range(opts["PopulationSize"]):
        snakes.append(snake(playground, start, goal, opts["MaxSteps"]))

    return snakes

if __name__=="__main__":
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

    snakes = gen_snakes(playground, start, goal, opts)
#    print(snakes[49].alphas)


