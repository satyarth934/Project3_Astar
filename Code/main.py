import sys
import numpy as np

import node
import actions


def hittingObstacle(node):
	return False

	# yet to write the logic to check obstacle


##
## Computes the path from the starting node to the goal node
##
## :param      start_node:    The start node (Xs,Ys,Theta_s)
## :type       start_node:    A tuple of starting coordinates and orientation
## :param      goal_node:     The goal node (Xs,Ys,Theta_g)
## :type       goal_node:     A tuple of the GOAL coordinates and orientation
## :param      robot_radius:  Radius of the circular robot
## :type       robot_radius:  float
## :param      clearance:     Clearance gap between the robot and the obstacle
## :type       clearance:     float
## :param      step_size:     The atomic linear movement step size
## :type       step_size:     float
## :param      theta:         The atomic angular movement in terms of theta in degrees
## :type       theta:         float
##
def aStar(start_node, goal_node, robot_radius, clearance, step_size, theta=30):
	# check if the start node lies withing the map and not on obstacles
	if (start_node.current_coords[0] < actions.MIN_COORDS[1]) or (start_node.current_coords[0] >= actions.MAX_COORDS[1]) or (start_node.current_coords[1] < actions.MIN_COORDS[0]) or (start_node.current_coords[1] >= actions.MAX_COORDS[0]) or hittingObstacle(start_node):
		print("ERROR: Invalid start node. It either lies outside the map boundary or within the obstacle region.")
		sys.exit(0)

	# check if the goal node lies withing the map and not on obstacles
	if (goal_node.current_coords[0] < actions.MIN_COORDS[1]) or (goal_node.current_coords[0] >= actions.MAX_COORDS[1]) or (goal_node.current_coords[1] < actions.MIN_COORDS[0]) or (goal_node.current_coords[1] >= actions.MAX_COORDS[0]) or hittingObstacle(goal_node):
		print("ERROR: Invalid goal node. It either lies outside the map boundary or within the obstacle region.")
		sys.exit(0)

	# check is step size lies between 0 and 10
	if step_size < 1 or step_size > 10:
		print("ERROR: Invalid step_size. It must lie within 1 and 10.")
		sys.exit(0)



	# write code to find the actual path using a star




def main():
	pass


if __name__ == '__main__':
	main()