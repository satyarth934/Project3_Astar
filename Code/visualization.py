import matplotlib.pyplot as plt


def plainPlot(node_vector):
	plt.figure("plot")

	for node in node_vector:
		x,y = node.getXYCoords()
		plt.plot(x, y, 'ro')

	plt.show()
	plt.close()


def plainQuiver(node_vector):
	plt.figure("QuiverPlot")

	x,y = node_vector[0].getXYCoords()
	for node in node_vector[1:]:
		u,v = node.getXYCoords()
		u -= x
		v -= y
		q = plt.quiver(x, y, u, v, units='xy', scale=1, color='black')

		x,y = node.getXYCoords()
		# plt.plot(x, y, 'ro')

	plt.gca().set_aspect('equal')
	plt.xlim(-5, 5)
	plt.ylim(-5, 5)

	plt.minorticks_on()
	plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
	plt.grid(which='minor', color='black')
	plt.title('Vector plot', fontsize=25)

	plt.show()
	plt.close()


def explorationQuiver(visited_node_vector):
	pass