import os
import cv2
import copy
import numpy as np


##
## To find the euclidean distance between two coordinates.
## Used in the A_star algorithm
##
## :param      state1:  coordinate 1
## :type       state1:  (row, col)
## :param      state2:  coordinate 2
## :type       state2:  (row, col)
##
## :returns:   euclidean distance between the two coordinates
## :rtype:     float
##
def euclideanDistance(state1, state2):
	return np.sqrt(((state1[0] - state2[0]) ** 2) + ((state1[1] - state2[1]) ** 2))


##
## Finds a node in heap based on only the current coordinate values.
##
## :param      node:       The node to be searched
## :type       node:       Node
## :param      node_list:  The list of nodes where we look for the node
## :type       node_list:  List of nodes
##
## :returns:   index position of where the node is found (-1 if not found)
## :rtype:     int
##
def findInHeap(node, node_list):
	node_list_coords = [item[1].current_coords for item in node_list]
	if node.current_coords in node_list_coords:
		return node_list_coords.index(node.current_coords)
	return -1


##
## Finds the optimum path from the list of visited nodes 
## by backtracking to the parents of each nodes.
##
## :param      node:           The current node that is the same as the goal node
## :type       node:           Node
## :param      visited_nodes:  The visited nodes dictionary with current coordinates as the key
## :type       visited_nodes:  dictionary
##
## :returns:   List of coordinates that give the path from the start node to end node
## :rtype:     list
##
def backtrack(node, visited_nodes, theta_bin_size):
	# put the goal node in the path
	path = [node]

	# backtrack all the parent nodes from the list of visited nodes
	temp = visited_nodes[round(node.parent_coords[0]), round(node.parent_coords[1]), orientationBin(node.orientation, theta_bin_size)]
	while temp.parent_coords is not None:
		path.insert(0, temp)
		temp = visited_nodes[int(round(temp.parent_coords[0])), int(round(temp.parent_coords[1])), orientationBin(temp.orientation, theta_bin_size)]

	# put the start node in the path
	path.insert(0, temp)

	return path


##
## Returns the bin for the given angle
##
## :param      angle:     The angle
## :type       angle:     float
## :param      bin_size:  The bin size
## :type       bin_size:  float
##
## :returns:   The bin to which the angle belongs in the visited dictionary
## :rtype:     float
##
def orientationBin(angle, bin_size):
	return (((angle % 360) // bin_size) * bin_size)


##
## Function to draw an individual point on the map for visualization purposes
##
## :param      input_map:  The input map
## :type       input_map:  numpy matrix
## :param      coords:     The coordinate to mark on the map
## :type       coords:     (row, col)
## :param      visualize:  Visualize only if this argument is True
## :type       visualize:  boolean
##
def drawOnMap(input_map, coords, visualize=False):
	input_map[coords] = 255

	if visualize:
		cv2.imshow("exploration", input_map)
		cv2.waitKey(10)


# def visualizePaths(input_map, optimal_path, exploration_coords=None):

# 	if len(exploration_coords) > 0:
# 		exp_map = copy.deepcopy(input_map)

# 		for coord in exploration_coords:
# 			exp_map[coord] = 255
# 			cv2.imshow("Exploration Map", exp_map)
# 			cv2.waitKey(1)

# 		print "Done with exploration"


# 	for n in optimal_path:
# 		input_map[n.current_coords] = 255
# 		cv2.imshow("Exploration Map", input_map)
# 		cv2.waitKey(50)


def visualizePaths(node_list):
	pass


# def main():
# 	print(euclideanDistance((10,10), (12,12)))


# if __name__ == '__main__':
# 	main()
