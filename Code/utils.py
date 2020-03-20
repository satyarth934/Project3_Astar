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


def valRound(x):
	return (int(x) if x < (int(x)+0.5) else int(x)+0.5)


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


def testMain():
	# print(euclideanDistance((10,10), (12,12)))

	# print((0.2), valRound(0.2))
	# print((0.7), valRound(0.7))
	# print((1.1), valRound(1.1))
	# print((5), valRound(5))
	# print((4.6), valRound(4.6))
	# print((4.5), valRound(4.5))
	
	pass


if __name__ == '__main__':
	testMain()
