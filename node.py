import numpy as np
from queue import PriorityQueue

# Function returns the h-cost based on which method is used, current state and goal state
def getHeuristic(hFunc, curr, goal):
    h_val = 0
    if hFunc == 1:
        #Calculate Heuristic for Misplaced Tile
        for i in range(0,9):
            currLoc = list(zip(*np.where(curr == i)))
            goalLoc = list(zip(*np.where(goal == i)))

            if(currLoc != goalLoc):
                h_val += 1

    
    else:
        #Calculate Heuristic for Manhanttan Distance
        for i in range(0,9):
            currLoc = list(zip(*np.where(curr == i)))
            goalLoc = list(zip(*np.where(goal == i)))
            h_val += abs(currLoc[0][0]-goalLoc[0][0]) + abs(currLoc[0][1]-goalLoc[0][1])
    
    return h_val

# Class defines all the metadata of a node
class Node:
 
    def __init__(self, curr_state, goal, hFunc, g):
        self.g = g
        self.h = getHeuristic(hFunc, curr_state, goal)
        self.f = g + self.h
        self.state = curr_state
        self.goal =  goal
        self.hFunc = hFunc

    def __lt__(self, other):
        return self.get_f() < other.get_f()

    def get_f(self):
        return self.f

    def get_state(self):
        return self.state

    def get_goal(self):
        return self.goal
    
    def get_hFunc(self):
        return self.hFunc
    
    def get_g(self):
        return self.g



