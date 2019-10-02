#---------------------------------------#
#               HW #3                   #
#       Author: Justin Weigle           #
#       Edited: 01 Oct 2019             #
#---------------------------------------#
#       Genetic Algorithm               #
#---------------------------------------#

import random
from math import cos, sin, pi, hypot, inf
import operator

"""
define the distance formula for determining the distance of a snake at a
location 'loc' from the goal
"""
def dist(loc, goal): return hypot(goal[0] - loc[0], goal[1] - loc[1])


class Snake():
    def __init__(self, start, max_steps):
        self.alphas = []
        for i in range(max_steps):
            self.alphas.append(
                    [random.uniform(0, pi), random.uniform(0, (pi/2))]
            )
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
    for i in range(len(snake.path)):
        if (playground[0][1] < snake.path[i][0]
            or snake.path[i][0] < playground[0][0]
            or playground[1][1] < snake.path[i][1]
            or snake.path[i][0] < playground[1][0]
        ):
            snake.eval = i + 38
            return
    for i in range(len(distances)):
        if (distances[i] < 0.5):
            snake.eval = i
            return
    snake.eval = 25 + distances[24]

def calc_select_prob(snake, evals):
    snake.select_prob = 1 - (snake.eval / sum(evals))
    
def select_survivors(snakes, select_probs, num_survivors, random_chance, children):
    sorted_probs = sorted(select_probs.items(), key = operator.itemgetter(1), reverse = True)
    count = 0
    for i in range(len(sorted_probs)):
        if (random_chance <= sorted_probs[i][1] and count < num_survivors):
            children.append(snakes[int(sorted_probs[i][0])])
            count += 1


if __name__=="__main__":
    random.seed(3293)
    # set things up
    playground = [(0,32), (0,18)]
    max_steps = 25
    start = [6, 1]
    goal = [23, 10]
    opts = dict()
    opts.update({
        "PopulationSize":50,
        "Generations":1000,
        "MaxSteps":25,
    })
    num_survivors = opts["PopulationSize"] * 0.04
    snakes = gen_snakes(start, opts)
    #end setup


    for snake in snakes:
        snake.hunt()

    for snake in snakes:
        evaluate(snake, goal, playground)

    evals = []
    for snake in snakes:
        evals.append(snake.eval)

    for snake in snakes:
        calc_select_prob(snake, evals)

    select_probs = dict()
    for i in range(len(snakes)):
        select_probs[str(i)] = snakes[i].select_prob

    children = []
    random_chance = random.uniform(0, 1)
    select_survivors(snakes, select_probs, num_survivors, random_chance, children)
