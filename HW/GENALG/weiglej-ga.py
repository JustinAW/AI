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
    """ Snake class
    params:
        start: list, [x coordinate, y coordinate]
        max_steps: int, max distance snake can travel
    methods:
        hunt(), hunts for food by taking path of angles in alphas
        using cosine(x) and sine(y)
    """
    def __init__(self, start, max_steps):
        self.alphas = []
        for i in range(max_steps):
            self.alphas.append(
                    [random.uniform(0, pi), random.uniform(0, (pi/2))]
            )
        self.max_steps = max_steps
        self.start = start
        self.loc = start
        self.path = []
        self.eval = inf
        self.select_prob = 0
        self.selected = False

    def hunt(self):
        if self.path:
            self.loc = self.start
            self.path = []
        for i in range(self.max_steps):
            self.loc = [
                    self.loc[0] + cos(self.alphas[i][0]), 
                    self.loc[1] + sin(self.alphas[i][1])
            ]
            self.path.append(self.loc)


def gen_snakes(start, opts):
    """ Generates the initial population of snakes
    params:
        start: list, [x, y]
        opts: dict, contains hyperparameters
    returns:
        list of snakes generated
    """
    snakes = []
    for i in range(opts["PopulationSize"]):
        snakes.append(Snake(start, opts["MaxSteps"]))

    return snakes


def evaluate(snake, goal, playground):
    """ Evaluates a snake based on its distance from the goal
    params:
        snake: class, Snake
        goal: list, [x, y]
        playground: list of 2 tuples, [x(min, max), y(min, max)]
    returns:
        list of sorted distances of snake from goal, 
        boolean indicating if the goal was reached
    """
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
    """ Calculates the probability of a snake being selected for survival
    params:
        snake: class, Snake
        evals: list, evaluations of all snakes
    """
    snake.select_prob = 1 - (snake.eval / sum(evals))


def select_survivors(snakes, num_survivors, survival_thresh):
    """ Picks the survivors that stay for next generation of snakes
    params:
        snakes: list, current generation of snakes of class Snake
        num_survivors: int, how many survivors there should be
        survival_thresh: float, selection probability threshold that survivors
                            must meet
    returns:
        list of survivors of class Snake, 
        list of tuples of reverse sorted selection probabilities and 
            their indices
    """
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
    """ Picks parents from the current generation of snakes for crossover
    params:
        snakes: list, current generation of snakes of class Snake
        survivors: list, snakes of class Snake that survived
        opts: dict, contains hyperparamters
        num_survivors: int, how many survivors there should be
    returns:
        list of parents of class Snake
    """
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
    """ Crosses parents with one another to make children
    params:
        parents: list, snake parents of class Snake
        opts: dict, contains hyperparameters
        start: list, [x, y]
    returns:
        list of children of class Snake
    """
    children = []
    i = 0
    for pairs in range(0, len(parents), 2):
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
    """ Random chance at picking a random alpha for each snake to regenerate
    params:
        next_gen: list, next generation of snakes of class Snake
        opts: dict, contains hyperparameters
    """
    for snake in next_gen:
        mutate = random.uniform(0, 1)
        if (mutate < opts["MutProb"]):
            #print("mutation occured")
            selected_alpha = int(random.uniform(0, opts["MaxSteps"]))
            snake.alphas[selected_alpha] = [
                    random.uniform(0, pi), random.uniform(0, (pi/2))
            ]

def ga_soln_snakes():
    """ TODO
    """
    # set things up
    playground = [(0,32), (0,18)]
    start = [13, 1]
    goal = [13, 18]
    goal_distance = dist(start, goal)
    opts = dict()
    opts.update({
        "PopulationSize": 50,
        "Generations": 1000,
        "MaxSteps": 25,
        "MutProb": 0.05,
    })
    num_survivors = int(opts["PopulationSize"] * 0.04)
    snakes = gen_snakes(start, opts)
    total_generations = opts["Generations"]
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
                total_generations = generation + 1
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
        survivors, sp = select_survivors(
                snakes, num_survivors, survival_thresh)
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

    return total_generations


if __name__=="__main__":
    trials = 10
    s = 0
    for i in range(trials):
        s += ga_soln_snakes()
    print("Average number of generations to reach goal: ")
    print(s/trials)
