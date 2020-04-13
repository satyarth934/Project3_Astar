#!/usr/bin/env python
# license removed for brevity
import os
import sys
import rospy
import numpy as np 
import math
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Point
import time 
import rospkg
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion
sys.dont_write_bytecode = True

import utils



x = 0.0
y = 0.0
theta = 0.0

goal = Point()
goal.x = x
goal.y = y

path_itr = 1

def newOdom(msg, args):
	global x
	global y
	global theta
	
	global goal
	global path_itr

	path_list = args[0]
	cmd_vel_pub = args[1]

	x = msg.pose.pose.position.x
	y = msg.pose.pose.position.y

	rot_q = msg.pose.pose.orientation
	roll, pitch, theta = euler_from_quaternion((rot_q.x, rot_q.y, rot_q.z, rot_q.w))

	if utils.euclideanDistance((goal.x, goal.y), (x, y)) < 0.2:
		goal.x, goal.y = path_list[path_itr].getXYCoords()
		path_itr += 1

		if path_itr >= len(path_list):
			speed = Twist()
			speed.linear.x = 0.0
			speed.angular.z = 0.0
			cmd_vel_pub.publish(speed)
			rospy.signal_shutdown("Reached the last node of the path_list!!! Yayyy!")


def main():
	rospy.init_node("test_move")

	rospack = rospkg.RosPack()
	npy_path = os.path.join(rospack.get_path('turtlebot_astar'), 'paths/path_n4zz.npy')
	robot_path_list = np.load(npy_path, allow_pickle=True)

	global goal
	goal.x, goal.y = robot_path_list[0].getXYCoords()

	pub = rospy.Publisher("/cmd_vel", Twist, queue_size=1)
	sub = rospy.Subscriber("/odom", Odometry, newOdom, (robot_path_list, pub))

	r = rospy.Rate(4)
	speed = Twist()

	while not rospy.is_shutdown():
		# for node in values[1:]:
		# 	goal.x, goal.y = node.getXYCoords()

		inc_x = goal.x - x
		inc_y = goal.y - y

		angle_to_goal = math.atan2(inc_y, inc_x)
		rospy.loginfo(angle_to_goal)

		# while(utils.euclideanDistance((goal.x, goal.y), (x, y)) > 0.2):
			
		print("abs(angle_to_goal - theta):", abs(angle_to_goal - theta))
		if abs(angle_to_goal - theta) < 0.1:
			print("inside if")
			speed.linear.x = 0.5
			speed.angular.z = 0.0
		elif (angle_to_goal - theta) < 0:
			speed.linear.x = 0.0
			speed.angular.z = -0.3
		else:
			print("inside else")
			speed.linear.x = 0.0
			speed.angular.z = 0.3
	
		# speed.linear.x = 0.0
		# speed.angular.z = 0.0

		pub.publish(speed)
		r.sleep()


if __name__ == '__main__':
	main()
