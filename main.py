from node import Node
import numpy as np
import heapq
from func import expand, take_input, isNotSolvable


def main():
    # Gets what heuristic function that user wants to use
    while(True):
        heuristic = int(input("1. Misplaced Tiles\n2. Manhanttan Distance\nEnter: "))
        if heuristic not in [1, 2]:
            print("Not valid heuristic function")
            continue
        else:
            break
    fringe = [] # Array for storing expanded nodes
    visited = [] # Array for storing visited nodes

    # Variables to keep track of the number of nodes created and expanded
    numOfNodes = 1
    numOfExpanded = 0

    # Get initial and Goal state values
    initial = take_input("Enter values for Initial State (Ex. 123456780): ")
    goal = take_input("Enter values for Goal State (Ex. 123456780): ")
    
    
    # if isNotSolvable(initial, goal):
    #     print("not solvableeeeeeeeeee")
    #     return

    #Put the intial value in PQ
    initialNode = Node(initial, goal, heuristic, 0)
    heapq.heappush(fringe, (initialNode.get_f(), initialNode))

    #Start the loop
    while fringe:
        print(len(fringe))
        currNode = heapq.heappop(fringe)
        # add to visited set, so we dont get the same state twice
        visited.append(currNode[1].get_state())

        print(currNode[1].get_state())
        #Do some sort of check here

        # np.all([[True,False],[True,True]])
        if np.array_equal(currNode[1].get_goal(), currNode[1].get_state()):
            break

        #Expands the node to get the possible moves
        nodeList = expand(currNode[1])
        numOfExpanded += 1

        # Loop through the expanded nodes to see if they have already existed
        for node in nodeList:
            exists = False
            # Compares the current node to the nodes that have been visited
            for n in visited:
                # print(n, node)
                if np.array_equal(node.get_state(), n):
                    exists = True
            if not exists:
                f_value = node.get_f()
                heapq.heappush(fringe, (f_value, node))
                numOfNodes += 1

    # Print the Results
    print("Number of Expanded Nodes: ", numOfExpanded)
    print("Number of Nodes: ", numOfNodes)
    if not np.array_equal(currNode[1].get_goal(), currNode[1].get_state()):
        print("No solution found")

main()