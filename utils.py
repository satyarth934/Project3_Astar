from __future__ import division
import os
import cv2
import sys
import copy
import numpy as np
sys.dont_write_bytecode = True

import sattu


##
## Used to round off the coordinate value with a threshold of 0.5
## USed to cjeck for duplicate points
##
## :param      x:    Value to be rounded off
## :type       x:    float
##
## :returns:   The rounded value with 0.5 threshold
## :rtype:     float
##
def valRound(x):
	return (np.round(x, 2) if x < (np.round(x, 2) + 0.005) else np.round(x, 2) + 0.005)
	# return (int(x) if x < (int(x)+0.5) else int(x)+0.5)




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


def getKey(x, y, theta):
	x_new = int(np.floor(x*10))/10
	y_new = int(np.floor(y*10))/10
	t_bin = orientationBin(theta, sattu.THETA_BIN_SIZE)

	# print("ori:", x, y, theta)
	# print("key:", x_new, y_new, t_bin)
	# print("------------------")

	return ((x_new, y_new, t_bin))



def testMain():
	# print(euclideanDistance((10,10), (12,12)))

	print((0.2), valRound(0.2))
	print((0.7), valRound(0.7))
	print((1.1), valRound(1.1))
	print((5), valRound(5))
	print((4.6), valRound(4.6))
	print((4.5), valRound(4.5))
	
	pass


if __name__ == '__main__':
	testMain()