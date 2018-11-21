from landscapeGenerator import *
from stationaryTarget import *
import numpy as np
import sys

# prints avrage over 1000 trials for each all rules
def search_destroy(dimension, typ="stationary"):
    rules=[1,2,3]
    searches=[[] for _ in range(len(rules))]
    for i in range(1000):
        landscape, target=landscape_generator(dimension)
        for rule_no, rule in enumerate(rules):
            sys.stdout.write("\r maze_no: "+ str(i) + ", rule_no: "+ str(rule)+"                  ")
            if typ=="stationary":
                search_count=findTarget(landscape, target, rule)
            else:
                search_count=findTarget(landscape, target, rule, "moving")
            searches[rule_no].append(search_count)
    for rule_no in range(len(rules)):
        print("\n Average number of searches for rule no. "+str(rule_no+1)+" = "+str(np.mean(searches[rule_no])))

if __name__ == '__main__':
    search_destroy(10)
