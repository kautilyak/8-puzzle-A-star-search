import collections
import numpy as np
from node import Node

# Function takes current node and return an array of all possible nodes that can be expanded
def expand(node):
    # Variable to store the location of the node
    currLoc = list(zip(*np.where(node.get_state() == 0)))
    x = currLoc[0][0]
    y = currLoc[0][1]
    
    nodeList = []
    #print("\n")
    #generate node if 0 moves up
    if(x != 0):
        newState = node.get_state().copy()
        newState[x-1][y], newState[x][y] = newState[x][y], newState[x-1][y]
        
        newNode = Node(newState, node.get_goal(), node.get_hFunc(), node.get_g() + 1)
        nodeList.append(newNode)

    #generate node if 0 moves down
    if(x != 2):
        newState = node.get_state().copy()
        newState[x+1][y], newState[x][y] = newState[x][y], newState[x+1][y]

        newNode = Node(newState, node.get_goal(), node.get_hFunc(), node.get_g() + 1)
        nodeList.append(newNode)

    #generate node if 0 moves right
    if(y != 2):
        newState = node.get_state().copy()
        newState[x][y+1], newState[x][y] = newState[x][y], newState[x][y+1]

        newNode = Node(newState, node.get_goal(), node.get_hFunc(), node.get_g() + 1)
        nodeList.append(newNode)
    #generate node if 0 moves left
    if(y != 0):
        newState = node.get_state().copy()
        newState[x][y-1], newState[x][y] = newState[x][y], newState[x][y-1]
        
        newNode = Node(newState, node.get_goal(), node.get_hFunc(), node.get_g() + 1)
        nodeList.append(newNode)
    return nodeList
    
# Function for input validation for user input when creating inital or goal states
def take_input(text):
    
    # Gets the user input and puts it into a list
    while(True):
        nums = list(input(text))
        if not validate(nums):
            print("Invalid input")
            continue
        else:
            break

    # Converts the list of strings into a list of num
    res = [int(i) for i in nums]

    return np.array(res).reshape(3,3)


# validate 8 puzzle input
def validate(arr):
    valid = set([1, 2, 3, 4, 5, 6, 7, 8, 0])
    
    if len(arr) < 9:
        return False


    for num in arr:
        num = int(num)
        
        if not num in valid:
            return False
        
        valid.remove(num)
    return True

def isNotSolvable(init, goal) :
    # Count inversions in given 8 puzzle
    inv_count = InvCount(init, goal)
    # return true if inversion count is even.
    return (inv_count % 2 == 0)


def InvCount(initial, goal):
    A = initial.ravel()
    B = goal.ravel()
    inversion_count = 0
    for i in range(0, 9):
        for j in range(i + 1, 9):
            if(A[i] > B[j]):
                inversion_count += 1
    print(inversion_count)
    return inversion_count