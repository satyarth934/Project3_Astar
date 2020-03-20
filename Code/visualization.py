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


def explorationQuiver(node_vector):
	plt.figure("exploration")

	colors = ['red', 'blue', 'green', 'yellow']
	color_i = 0

	old_parent = None
	for node in node_vector:
		xy = node.getParentXYCoords()
		uv = node.getXYCoords()
		if xy is None or uv is None:
			continue
		x,y = xy
		u,v = uv
		u -= x
		v -= y
		q = plt.quiver(x, y, u, v, units='xy', scale=1, color=colors[color_i%len(colors)])

		# plt.plot(x, y, 'ro')	

		print(str(old_parent) + "\t\t\t\t" + str(xy) + "\t\t\t\t" + str(uv) + "\t\t\t\t" + colors[color_i % len(colors)])

		if old_parent != xy:
			color_i += 1

		old_parent = xy

	plt.gca().set_aspect('equal')
	plt.xlim(-5, 5)
	plt.ylim(-5, 5)

	plt.minorticks_on()
	plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
	plt.grid(which='minor', color='black')
	plt.title('Vector plot', fontsize=25)

	plt.show()
	plt.close()