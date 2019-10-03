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
        self.selected = False

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
    goal_reached = False
    for coord in snake.path:
        distances.append(dist(coord, goal))
    for i in range(len(snake.path)):
        if (playground[0][1] < snake.path[i][0]
            or snake.path[i][0] < playground[0][0]
            or playground[1][1] < snake.path[i][1]
            or snake.path[i][0] < playground[1][0]
        ):
            snake.eval = i + 38
            return sorted(distances), goal_reached
    for i in range(len(distances)):
        if (distances[i] < 0.5):
            snake.eval = i
            goal_reached = True
            return sorted(distances), goal_reached
    snake.eval = 25 + distances[24]
    return sorted(distances), goal_reached


def calc_select_prob(snake, evals):
    snake.select_prob = 1 - (snake.eval / sum(evals))


def select_survivors(snakes, num_survivors, survival_thresh):
    survivors = []
    select_probs = dict()
    for i in range(len(snakes)):
        select_probs[str(i)] = snakes[i].select_prob
    sorted_probs = sorted(select_probs.items(), key = operator.itemgetter(1), 
            reverse = True)
    count = 0
    for i in range(len(sorted_probs)):
        if (survival_thresh <= sorted_probs[i][1]):
            if (count < num_survivors):
                survivors.append(snakes[int(sorted_probs[i][0])])
            snakes[int(sorted_probs[i][0])].selected = True
            count += 1
    return survivors, sorted_probs


def xover_selection(snakes, survivors, opts, num_survivors):
    parents = []
    max_num_parents = opts["PopulationSize"] - num_survivors
    while len(parents) < max_num_parents:
        for survivor in survivors:
            if (len(parents) < max_num_parents):
                parents.append(survivor)
        for snake in snakes:
            if snake not in survivors:
                if snake.selected:
                    if (len(parents) < max_num_parents):
                        parents.append(snake)
    return parents


def xover(parents, opts, start):
    children = []
    i = 0
    for pairs in range(0, len(parents)-1, 2):
        cut = int(random.uniform(2, opts["MaxSteps"]-2))
        p1_alphas = parents[i].alphas
        p2_alphas = parents[i+1].alphas
        p1_alphas_cut1 = p1_alphas[:cut]
        p1_alphas_cut2 = p1_alphas[cut:]
        p2_alphas_cut1 = p2_alphas[:cut]
        p2_alphas_cut2 = p2_alphas[cut:]
        combined_alphas1 = p1_alphas_cut1 + p2_alphas_cut2
        children.append(Snake(start, opts["MaxSteps"]))
        children[i].alphas = combined_alphas1
        combined_alphas2 = p2_alphas_cut1 + p1_alphas_cut2
        children.append(Snake(start, opts["MaxSteps"]))
        children[i+1].alphas = combined_alphas2
        i += 1
    return children


def mutation(next_gen, opts):
    for snake in next_gen:
        mutate = random.uniform(0, 1)
        if (mutate < opts["MutProb"]):
            print("mutation occured")
            selected_alpha = int(random.uniform(0, opts["MaxSteps"]))
            snake.alphas[selected_alpha] = [
                    random.uniform(0, pi), random.uniform(0, (pi/2)) ]


if __name__=="__main__":
#    random.seed(3291)  #make all snakes of first gen fail
    # set things up
    playground = [(0,32), (0,18)]
    max_steps = 25
    start = [6, 1]
    goal = [23, 10]
    goal_distance = dist(start, goal)
    #print("GOAL DISTANCE: "  + str(goal_distance))
    opts = dict()
    opts.update({
        "PopulationSize": 50,
        "Generations": 1000,
        "MaxSteps": 25,
        "MutProb": 0.05,
    })
    num_survivors = opts["PopulationSize"] * 0.04
    snakes = gen_snakes(start, opts)
    #end setup


    for generation in range(opts["Generations"]):
        for snake in snakes:
            snake.hunt()

        for snake in snakes:
            distances, goal_reached = evaluate(snake, goal, playground)
            if goal_reached: 
                print("GOAL")
                print("Generations elapsed: " + str(generation + 1))
                print("Distance from goal achieved: " + str(distances[0]))
                print("Starting distance from goal: " + str(goal_distance))
                break
        if goal_reached:
            break

        print("Closest snake of generation " 
                + str(generation + 1)
                + ": "
                + str(distances[0]))

        evals = []
        for snake in snakes:
            evals.append(snake.eval)

        for snake in snakes:
            calc_select_prob(snake, evals)

        survival_thresh = random.uniform(0, 1)
        survivors, sp = select_survivors(snakes, num_survivors, survival_thresh)
        if not survivors:
            for i in range(int(num_survivors)):
                survivors.append(snakes[int(sp[i][0])])
        next_gen = survivors

        parents = xover_selection(survivors, snakes, opts, num_survivors)

        children = xover(parents, opts, start)
        for child in children:
            next_gen.append(child)

        mutation(next_gen, opts)

        snakes = next_gen
