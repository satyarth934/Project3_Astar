from __future__ import print_function, division
import os
import sys
import cv2
import copy
import time
import numpy as np
import heapq
import matplotlib.pyplot as plt
import pickle
sys.dont_write_bytecode = True

import actions_new as an
import obstacles
import node
import utils
import visualization as viz
# import univ


THETA_BIN_SIZE = 30
GOAL_REACH_THRESH = 0.2 	# units in meters

# ROBOT_RADIUS = 0.177
ROBOT_RADIUS = 0.105
OBSTACLE_CLEARANCE = 0.2


def a_star(start_rc, goal_rc, orientation, rpm1=10, rpm2=20, clearance=0.2, viz_please=False):
	"""
	params:
	start_rc
	goal_rc
	orientation
	"""

	# inputs
	# start_rc = (-3, -4)
	# goal_rc = (-3, 0)
	start_node = node.Node(current_coords=start_rc, parent_coords=None, orientation=0, parent_orientation=None, action=None, movement_cost=0, goal_cost=utils.euclideanDistance(start_rc, goal_rc))
	goal_node = node.Node(current_coords=goal_rc, parent_coords=None, orientation=None, parent_orientation=None, action=None, movement_cost=None, goal_cost=0)

	# rpm1 = 10
	# rpm2 = 20

	# clearance = 0.2

	"""
	Initializations
	"""
	action_set = [(0, rpm1),
				  (rpm1, 0),
				  (0, rpm2),
				  (rpm2, 0),
				  (rpm1, rpm2),
				  (rpm2, rpm1),
				  (rpm1, rpm1),
				  (rpm2, rpm2)]

	min_heap = [((start_node.movement_cost + start_node.goal_cost), start_node)]
	heapq.heapify(min_heap)

	visited = {}
	visited.update(
		{(utils.getKey(start_rc[0], start_rc[1], start_node.orientation)): start_node})

	visited_viz_nodes = []

	"""
	Initialize the plot figures if the visualization flag is true.
	Also mark the start and the goal nodes.
	"""
	if viz_please:
		fig, ax = plt.subplots()
		ax.set(xlim=(-5, 5), ylim = (-5, 5))
		ax.set_aspect('equal')

		obstacles.generateMap(plotter=ax)

		viz.markNode(start_node, plotter=ax, color='#00FF00', marker='o')
		viz.markNode(goal_node, plotter=ax, color='#FF0000', marker='^')

		plt.ion()

	"""
	Run the loop for A-star algorithm till the min_heap queue contains nodes.
	"""
	while (len(min_heap) > 0):
		_, curr_node = heapq.heappop(min_heap)

		# Consider all the action moves for all the selected nodes.
		for action in action_set:
			new_node = an.actionMove(current_node=curr_node, next_action=action, goal_position=goal_rc)

			# Check if all the nodes are valid or not.			
			if (new_node is not None) and (not obstacles.withinObstacleSpace(new_node.getXYCoords(), radius=ROBOT_RADIUS, clearance=OBSTACLE_CLEARANCE)):

				if viz_please:
					viz.plot_curve(new_node, plotter=ax)
					plt.show()
					plt.pause(0.001)

				# Check if the current node is a goal node.
				if new_node.goal_cost < GOAL_REACH_THRESH:
					path = an.backtrack(new_node, visited)
					print("Reached Goal!")
					if viz_please:
						viz.plotPath(path, rev=True, pause_time=0.5, plotter=ax, color="lime", linewidth=4)

						plt.ioff()
						plt.show()
					return path

				# Mark node as visited, 
				# Append to min_heap queue,
				# Update if already visited.
				node_key = (utils.getKey(new_node.current_coords[0], new_node.current_coords[1], new_node.orientation))

				if node_key in visited:
					if new_node < visited[node_key]:
						visited[node_key] = new_node

						h_idx = utils.findInHeap(node=new_node, node_list=min_heap)
						if h_idx > -1:
							min_heap[h_idx] = ((new_node.movement_cost + new_node.goal_cost), new_node)
				else:
					visited.update({node_key: new_node})
					min_heap.append(((new_node.movement_cost + new_node.goal_cost), new_node))

					visited_viz_nodes.append(new_node)

		# Heapify the min heap to update the minimum node in the list.
		heapq.heapify(min_heap)


def main():
	start_rc = (-3, -4)
	# goal_rc = (-3, 0)
	goal_rc = (-4.5, -4.5)
	theta = 0
	
	rpm1 = 10
	rpm2 = 20

	clearance = 0.2

	start_time = time.clock()
	a_star(start_rc=start_rc, goal_rc=goal_rc, orientation=theta, rpm1=10, rpm2=20, clearance=0.2, viz_please=True)
	print("Time taken for Astar:", time.clock() - start_time)


if __name__ == '__main__':
	main()
