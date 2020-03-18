import sys
import numpy as np
import matplotlib.pyplot as plt


# plot a vector in the direction for given steps
# direction in radians
def plotVector(start_coords, directions, steps, vector_colors):
	x, y = map(np.array, start_coords)

	if len(directions) != len(steps):
		print("Give %s directions" % (len(steps)))
		sys.exit(0)
	if len(vector_colors) != len(steps):
		print("Give %s colors" % (len(steps)))
		sys.exit(0)
	
	minx, maxx = 0 - 2, x + 2
	miny, maxy = 0 - 2, y + 2

	for i, step in enumerate(steps):
		xf = np.array(step * np.cos(directions[i] * np.pi / 180))
		minx = xf if xf < minx else minx
		maxx = xf if xf > maxx else maxx

		yf = np.array(step * np.sin(directions[i] * np.pi / 180))
		miny = yf if yf < miny else miny
		maxy = yf if yf > maxy else maxy

		q = plt.quiver(x, y, xf, yf, units='xy', scale=1, color=vector_colors[i])
	
	plt.gca().set_aspect('equal')
	plt.xlim(minx, maxx)
	plt.ylim(miny, maxy)

	plt.minorticks_on()
	plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
	plt.grid(which='minor', color='black')
	plt.title('Vector plot', fontsize=25)


def main():
	# dir_degrees = [0,30,45,60,90,135,180]
	dir_degrees = [0]
	directions = [degree*np.pi/180 for degree in dir_degrees]
	
	plt.figure("steps")
	plotVector(start_coords=(1,1), directions=directions, steps=[1]*len(dir_degrees), vector_colors=["black"]*len(dir_degrees))
	
	plt.show()
	plt.close()


if __name__ == '__main__':
	main()