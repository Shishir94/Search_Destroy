from landscapeGenerator import *
from stationaryTarget import *
import numpy as np


def searchDestroy(landscape_dimension, rule):
    target = random.randint(0,landscape_dimension),random.randint(0,landscape_dimension)
    lScape, beliefMatrix = landscape_generator(landscape_dimension)
    searches = stationaryTarget(lScape,beliefMatrix,target, rule)
    #print("The total number of searches = ")
    #print(searches)
    return searches


def averageSearches(maxDimension):
    minDimension = 2
    searches = np.zeros([2,maxDimension+1],dtype = np.int8)

    for rule in [1,2]:
        print("Rule execution ...",rule)
        for i in range(minDimension,maxDimension+1):
            print("Board :",i)
            searches[rule-1][i] = searchDestroy(i,rule)
            print(searches[rule-1][i])
            print("-------------------")

    print("Average searches for rule 1 :")
    print(np.sum(searches[0])/(maxDimension-2))
    print("-----------------------------------------")
    print("Average searches for rule 2 :")
    print(np.sum(searches[1])/(maxDimension-2))
    print("-----------------------------------------")


if __name__ == '__main__':
    #averageSearches(15)
    print(searchDestroy(3,1))
