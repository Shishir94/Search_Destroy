import random
import numpy as np

def stationaryTarget(landscape, belief, target, rule):
    searches = 0
    probability = [0.1,0.3,0.7,0.9]
    while True:
        searches += 1
        xrange, yrange = np.where(belief == belief.max())
        idx = random.sample(range(xrange.size),1).pop()
        i = xrange[idx]
        j = yrange[idx]
        if((i,j) == target):
            if(random.uniform(0,1) < (1-probability[landscape[i][j]])):
                return searches
        belief[i][j] = belief[i][j] * probability[landscape[i][j]]
        beta = 1 / np.sum(belief)
        belief = belief * beta


def maxBelief(landscape, belief, rule):
    """
    The function accepts the landscape and belief matrix and returns the index
    of the cell with the maximum belief to be considered for exploration
    in the next iteration
    Rule 1 : The terrain type won't matter --> P(cell containing a target)
    Rule 2 : The terrain type will matter --> P(finding a target in a cell)
    """
    max = -1
    x,y = 0,0
    terrain = [0.1,0.3,0.7,0.9]
    if(rule == 1):
        for i in range(0, len(landscape)):
            for j in range(0, len(landscape)):
                if belief[i][j] > max:
                    max = belief[i][j]
                    x = i
                    y = j
    else:
        for i in range(0, len(landscape)):
            for j in range(0, len(landscape)):
                if((belief[i][j] * (1 - terrain[landscape[i][j]])) > max):
                    max = (belief[i][j] * (1 - terrain[landscape[i][j]]))
                    x = i
                    y = j
    return x,y
