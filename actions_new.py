import sys
import math
sys.dont_write_bytecode = True

import node
import sattu
import utils
import obstacles
import matplotlib.pyplot as plt


MIN_COORDS = (-5, -5)
MAX_COORDS = (5, 5)


def backtrack(node, visited_nodes, rev=False):
	# put the goal node in the path
	path = [node]

	# backtrack all the parent nodes from the list of visited nodes
	temp = visited_nodes[utils.getKey(node.parent_coords[0], node.parent_coords[1], node.parent_orientation)]

	while temp.parent_coords is not None:
		if rev:
			path.append(temp)
		else:
			path.insert(0, temp)
		# print("=====================================BACKTRACKING=============")
		# temp.printNode()
		# print("==================")
		temp = visited_nodes[utils.getKey(temp.parent_coords[0], temp.parent_coords[1], temp.parent_orientation)]

	# put the start node in the path
	if rev:
		path.append(temp)
	else:
		path.insert(0, temp)

	return path


def actionMove(current_node, next_action, goal_position, plotter=plt):
	Xi, Yi = current_node.getXYCoords()
	Thetai = current_node.orientation
	UL, UR = next_action

	mc = current_node.movement_cost

	t = 0
	r = 0.038
	L = 0.354
	dt = 0.1
	Xn=Xi
	Yn=Yi
	Thetan = math.radians(Thetai)

# Xi, Yi,Thetai: Input point's coordinates
# Xs, Ys: Start point coordinates for plot function
# Xn, Yn, Thetan: End point coordintes

	# curved_path = [(Xn,Yn)]

	while t<1:
		t = t + dt
		Xs = Xn
		Ys = Yn
		Xn += 0.5*r * (UL + UR) * math.cos(Thetan) * dt
		Yn += 0.5*r * (UL + UR) * math.sin(Thetan) * dt
		Thetan += (r / L) * (UR - UL) * dt
		plotter.plot([Xs, Xn], [Ys, Yn], color="blue")
		mc += utils.euclideanDistance((Xs,Ys), (Xn,Yn))

		# if the intermediate step hits a boundary
		if (Yn < MIN_COORDS[0]) or (Yn >= MAX_COORDS[0]) or (Xn < MIN_COORDS[1]) or (Xn >= MAX_COORDS[1]):
			# print("out of bound")
			return None 

		# if the intermediate step hits an obstacle
		if (obstacles.withinObstacleSpace((Xn, Yn), radius=sattu.ROBOT_RADIUS, clearance=sattu.OBSTACLE_CLEARANCE)):
			# print("In obstacle")
			return None

		# curved_path.append((Xn, Yn))

	cc = (Yn, Xn)
	pc = current_node.current_coords
	ori = math.degrees(Thetan)
	pori = current_node.orientation
	gc = utils.euclideanDistance(cc, goal_position)
	
	ret_val = node.Node(current_coords=cc, parent_coords=pc, orientation=ori, parent_orientation=pori, action= next_action, movement_cost=mc, goal_cost=gc)

	# return (ret_val, curved_path)
	return ret_val