"""
This generates a landscape of the given dimensions based on the
entered dimension for the maze and the probability values of the terrain.

0 --> Flat
1 --> Hilly
2 --> Forested
3 --> Caves
"""

import random
import numpy as np

def landscape_generator(landscape_dimension):
    landscape = np.zeros((landscape_dimension, landscape_dimension), dtype = np.int8)
    belief = np.zeros((landscape_dimension, landscape_dimension), dtype = np.float64)
    prior_probability = 1/(landscape_dimension*landscape_dimension)

    for i in range(landscape_dimension):
        for j in range(landscape_dimension):
            num = random.uniform(0,1)
            if num >= 0 and num < 0.2:
                landscape[i][j] = 0
            elif num >= 0.2 and num < 0.5:
                landscape[i][j] = 1
            elif num >= 0.5 and num < 0.8:
                landscape[i][j] = 2
            else:
                landscape[i][j] = 3
            belief[i][j] = prior_probability
    return landscape, belief
