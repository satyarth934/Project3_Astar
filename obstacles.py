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
def withinObstacleSpace((x,y),radius,clearance):

    flag = 0
    flag_1 = 0
    flag_2 = 0
    point = Point(x,y)
    rectangle_1 = Polygon([(-1.25,2.25), (-1.25,3.75), (-2.75,3.75), (-2.75,2.25)]) 
    rectangle_2 = Polygon([(-3.25,-0.25), (-3.25,1.25), (-4.75,1.25), (-4.75,-0.25)]) 
    rectangle_3 = Polygon([(4.75,-0.25), (4.75,1.25), (3.25,1.25), (3.25,-0.25)]) 

    #rectangle 1
    rect_1_1 = (x+1.25)*(1.5)
    rect_1_2 = (y-3.75)*(-1.5)
    rect_1_3 = (x+2.75)*(-1.5)
    rect_1_4 = (y-2.25)*(-1.5)

    # print(rect_1_1)
    # print(rect_1_2)
    # print(rect_1_3)
    # print(rect_1_4)

    # print("-----------------------")

    #rectangle 2
    rect_2_1 = (x+4.75)*(1.5)
    rect_2_2 = (y+0.25)*(-1.5)
    rect_2_3 = (x+3.2)*(1.5)
    rect_2_4 = (y-1.25)*(-1.5)

    # print(rect_2_1)
    # print(rect_2_2)
    # print(rect_2_3)
    # print(rect_2_4)

    # print("-----------------------")

    #rectangle 3
    rect_3_1 = (y+0.25)*(1.5)
    rect_3_2 = (x-4.75)*(1.5)
    rect_3_3 = (y-1.25)*(-1.5)
    rect_3_4 = (x-3.25)*(1.5)

    # print(rect_3_1)
    # print(rect_3_2)
    # print(rect_3_3)
    # print(rect_3_4)

    # print("-----------------------")

    
    #check rectangle
    if rect_1_1 < 0 and rect_1_2 > 0 and rect_1_3 < 0 and rect_1_4 > 0 or point.distance(rectangle_1) <= radius+clearance:
        # print("In Rectangle 1")
        flag = 1
    
    if rect_2_1 > 0 and rect_2_2 < 0 and rect_2_3 < 0 and rect_2_4 > 0 or point.distance(rectangle_2) <= radius+clearance:
        # print("In Rectangle 2")
        flag = 1
    
    if rect_3_1 > 0 and rect_3_2 < 0 and rect_3_3 > 0 and rect_3_4 > 0 or point.distance(rectangle_3) <= radius+clearance:
        # print("In Rectangle 3")
        flag = 1
    

    #circle
    if(((x - (0))**2 + (y - (0))**2 - (1+radius+clearance)**2) <= 0) :
        # print("In circle 1")
        flag = 1
    if(((x - (-2))**2 + (y - (-3))**2 - (1+radius+clearance)**2) <= 0) :
        # print("In circle 2")
        flag = 1
    if(((x - (2))**2 + (y - (-3))**2 - (1+radius+clearance)**2) <= 0) :
        # print("In circle 3")
        flag = 1
    if(((x - (2))**2 + (y - (3))**2 - (1+radius+clearance)**2) <= 0) :
        # print("In circle 4")
        flag = 1


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
    
    rectangle_1 = plt.Polygon([(-1.25,2.25), (-1.25,3.75), (-2.75,3.75), (-2.75,2.25)]) 
    rectangle_2 = plt.Polygon([(-3.25,-0.25), (-3.25,1.25), (-4.75,1.25), (-4.75,-0.25)]) 
    rectangle_3 = plt.Polygon([(4.75,-0.25), (4.75,1.25), (3.25,1.25), (3.25,-0.25)]) 

    plotter.add_artist(circle_1)
    plotter.add_artist(circle_2)
    plotter.add_artist(circle_3)
    plotter.add_artist(circle_4)
    plotter.add_line(rectangle_1)
    plotter.add_line(rectangle_2)
    plotter.add_line(rectangle_3)

    # pickle.dump(ax, file('map.pickle', 'wb'))

def testMain():
    print(withinObstacleSpace((0,-2),0,0))

    fig, ax = plt.subplots()
    ax.set(xlim=(-5, 5), ylim = (-5, 5))
    ax.set_aspect('equal')

    generateMap()
    
    plt.show()
    

if __name__ == '__main__':
    testMain()