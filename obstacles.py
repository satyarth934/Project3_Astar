import sys
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
from matplotlib.patches import Ellipse
import matplotlib.pyplot as plt
import pickle

##
## Defining the obstacle space and checking if the point coordinate is within the obstacle space
##
## :param      x:          x-coordinate in cartesian space
## :type       x:          float
## :param      y:          y-coordinate in cartesian space
## :type       y:          float
## :param      radius:     The radius
## :type       radius:     float
## :param      clearance:  The clearance
## :type       clearance:  float
##
## :returns:   True if the point lies in the obstacle space. Otherwise False
## :rtype:     boolean
##
def withinObstacleSpace((x,y), radius, clearance, plotter=plt):

    flag = 0
    flag_1 = 0
    flag_2 = 0
    point = Point(x,y)
    rectangle_1 = Polygon([(-4.75,-0.75), (-3.25,-0.75), (-3.25,0.75), (-4.75,0.75)]) 
    rectangle_2 = Polygon([(-2.75,2.25), (-1.25,2.25), (-1.25,3.75), (-2.75,3.75)]) 
    rectangle_3 = Polygon([(4.75,-0.75), (3.25,-0.75), (3.25,0.75), (4.75,0.75)]) 

    if point.distance(rectangle_1) <= radius+clearance:
        flag = 1
    
    if point.distance(rectangle_2) <= radius+clearance:
        flag = 1

    if point.distance(rectangle_3) <= radius+clearance:
        flag = 1
    
    #circle
    p1 = Point(0, 0)
    circle_1 = p1.buffer(1.0)
    p2 = Point(-2,-3)
    circle_2 = p2.buffer(1.0)
    p3 = Point(2,-3)
    circle_3 = p3.buffer(1.0)
    p4 = Point(2,3)
    circle_4 = p4.buffer(1.0)
    
    # circle_1 = plt.Circle((0,0), 1, color='b')
    # circle_2 = plt.Circle((-2,-3), 1, color='b')
    # circle_3 = plt.Circle((2,-3), 1, color='b')
    # circle_4 = plt.Circle((2,3), 1, color='b')

    if point.distance(circle_1) <= radius+clearance:
        # print("In Rectangle 3")
        flag = 1
    if point.distance(circle_2) <= radius+clearance:
        # print("In Rectangle 3")
        flag = 1
    if point.distance(circle_3) <= radius+clearance:
        # print("In Rectangle 3")
        flag = 1
    if point.distance(circle_4) <= radius+clearance:
        # print("In Rectangle 3")
        flag = 1
    

    # if(((x - (0))**2 + (y - (0))**2 - (1+radius+clearance)**2) <= 0) :
    #     # print("In circle 1")
    #     flag = 1
    # if(((x - (-2))**2 + (y - (-3))**2 - (1+radius+clearance)**2) <= 0) :
    #     # print("In circle 2")
    #     flag = 1
    # if(((x - (2))**2 + (y - (-3))**2 - (1+radius+clearance)**2) <= 0) :
    #     # print("In circle 3")
    #     flag = 1
    # if(((x - (2))**2 + (y - (3))**2 - (1+radius+clearance)**2) <= 0) :
    #     # print("In circle 4")
    #     flag = 1

    return flag    


def withinObstacleSpaceFake((x,y),radius,clearance):
    return False


##
## Genarting the map for the obstacle space 
##
def generateMap(plotter=plt):
    circle_1 = plt.Circle((0,0), 1, color='b')
    circle_2 = plt.Circle((-2,-3), 1, color='b')
    circle_3 = plt.Circle((2,-3), 1, color='b')
    circle_4 = plt.Circle((2,3), 1, color='b')

    rectangle_1 = plt.Polygon([(-4.75,-0.75), (-3.25,-0.75), (-3.25,0.75), (-4.75,0.75)]) 
    rectangle_2 = plt.Polygon([(-2.75,2.25), (-1.25,2.25), (-1.25,3.75), (-2.75,3.75)]) 
    rectangle_3 = plt.Polygon([(4.75,-0.75), (3.25,-0.75), (3.25,0.75), (4.75,0.75)])

    plotter.add_artist(circle_1)
    plotter.add_artist(circle_2)
    plotter.add_artist(circle_3)
    plotter.add_artist(circle_4)
    plotter.add_line(rectangle_1)
    plotter.add_line(rectangle_2)
    plotter.add_line(rectangle_3)

    # pickle.dump(ax, file('map.pickle', 'wb'))


def testMain():
    x = float(sys.argv[1])
    y = float(sys.argv[2])

    fig, ax = plt.subplots()
    ax.set(xlim=(-10, 10), ylim = (-10, 10))
    ax.set_aspect('equal')
    ax.plot([x], [y], color="black", marker="+", markersize=3)

    print(withinObstacleSpace((x, y),0.105,0.2, plotter=ax))
    generateMap(ax)

    plt.show()
    

if __name__ == '__main__':
    testMain()