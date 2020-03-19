import sys
sys.dont_write_bytecode = True

import heapq
import numpy as np

import node
import actions
import utils


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
def aStar(start_pos, goal_pos, robot_radius, clearance, step_size, theta=30, duplicate_step_thresh=0.5, duplicate_orientation_thresh=30):

	start_r, start_c = start_pos
	goal_r, goal_c = goal_pos

	start_node = node.Node(current_coords=(start_r, start_c), parent_coords=None, orientation=0, movement_cost=0, goal_cost=utils.euclideanDistance(start_pos, goal_pos))
	goal_node = node.Node(current_coords=(goal_r, goal_c), parent_coords=None, orientation=None, movement_cost=None, goal_cost=0)

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


	# Saving a tuple with total cost and the state node
	minheap = [((start_node.movement_cost + start_node.goal_cost), start_node)]
	heapq.heapify(minheap)

	# # defining the visited node like this avoids checking if two nodes are duplicate. because there is only 1 position to store the visited information for all the nodes that lie within this area.
	# visited = np.zeros((int(actions.MAX_COORDS[1]/duplicate_step_thresh), int(actions.MAX_COORDS[0]/duplicate_step_thresh), int(360/duplicate_orientation_thresh)))
	# visited[start_r, start_c, 0] = 1	# marking the start node as visited
	visited = {}
	visited[(round(start_r), round(start_c), 0)] = start_node 	# marking the start node as visited


	viz_visited_coords = []

	while len(minheap) > 0:
		_, curr_node = heapq.heappop(minheap)

		if curr_node.isDuplicate(goal_node):
			print("Reached Goal!")

			#########################################
			# for k in visited:
			# 	print("KEY:", k)
			# 	visited[k].printNode()
			# 	print("----------------")
			
			for viz_node in viz_visited_coords:
				viz_node.printNode()
				print("----------------")
			#########################################

			# backtrack to get the path
			path = utils.backtrack(curr_node, visited, theta)

			return (path, viz_visited_coords)

		# for row_step, col_step in movement_steps:
		for angle in range(0, 360, theta):
			# Action Move
			# next_node = actions.actionMove(curr_node, row_step, col_step)
			next_node = actions.actionMove(current_node=curr_node, theta_step=angle, linear_step=step_size, goal_position=goal_node.current_coords)

			if next_node is not None:
				# if hit an obstacle, ignore this movement
				if hittingObstacle(next_node):
					continue

				# Check if the current node has already been visited.
				# If it has, then see if the current path is better than the previous one
				# based on the total cost = movement cost + goal cost
				node_state = (round(next_node.current_coords[0]), round(next_node.current_coords[1]), utils.orientationBin(next_node.orientation + angle, theta))
				
				if node_state in visited:
					# if current cost is a better cost
					if (next_node.movement_cost + next_node.goal_cost) < (visited[node_state].movement_cost + visited[node_state].goal_cost):
						visited[node_state].current_coords = next_node.current_coords
						visited[node_state].parent_coords = next_node.parent_coords
						visited[node_state].orientation = next_node.orientation
						visited[node_state].movement_cost = next_node.movement_cost
						visited[node_state].goal_cost = next_node.goal_cost

						h_idx = utils.findInHeap(next_node, minheap)
						if (h_idx > -1):
							minheap[h_idx] = ((next_node.movement_cost + next_node.goal_cost), next_node)
				else:
					# visited.append(next_node)
					visited[node_state] = next_node
					heapq.heappush(minheap, ((next_node.movement_cost + next_node.goal_cost), next_node))

					viz_visited_coords.append(next_node)
					# if visualize:
					# 	utils.drawOnMap(viz_map, next_node.current_coords, visualize=visualize)

		heapq.heapify(minheap)




def testMain():
	path, viz_nodes = aStar(start_pos=(1,1), goal_pos=(3,3), robot_radius=0, clearance=0, step_size=1, theta=30, duplicate_step_thresh=0.5, duplicate_orientation_thresh=30)


	pickle.dump( path, open( "optimum_path.pickle", "wb" ) )
	pickle.dump( viz_nodes, open( "viz_nodes.pickle", "wb" ) )


	# plt.figure("Explorations")
	# utils.visualizePaths(viz_nodes)

	# plt.figure("Optimal A* path")
	# utils.visualizePaths(path)

	# plt.show()
	# plt.close()


if __name__ == '__main__':
	testMain()