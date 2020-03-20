from shapely.geometry import Point
from shapely.geometry.polygon import Polygon


def obstacleSpace(x,y,radius,clearance):

    flag = 0
    flag_1 = 0
    flag_2 = 0
    point = Point(x,y)
    rectangle = Polygon([(35, 76), (100, 39),(95, 30), (30, 68)])
    complex_polygon = Polygon([(25, 185), (75, 185),(100, 150), (75, 120), (50,150), (20,120)])
    kite = Polygon([(225, 40), (250, 25),(225, 10), (200, 25)])
    
    #kite
    kite_line_1 = ((y-25)*25) + ((x-200)*15)
    kite_line_2 = ((y-10)*25) - ((x-225)*15)
    kite_line_3 = ((y-25)*25) + ((x-250)*15)
    kite_line_4 = ((y-40)*25) - ((x-225)*15)
    
    #rectangle
    rect_line_1 = ((y-76)*65) + ((x-35)*37)
    rect_line_2 = ((y-39)*5) - ((x-100)*9)
    rect_line_3 = ((y-30)*65) + ((x-95)*38)
    rect_line_4 = ((y-68)*5) - ((x-30)*8)
    
    #complex polygon
    quad_1_1 = 5*y+6*x-1050
    quad_1_2 = 5*y-6*x-150
    quad_1_3 = 5*y+7*x-1450
    quad_1_4 = 5*y-7*x-400
    
    quad_2_1 = ((y-185)*5) - ((x-25)*65)
    quad_2_2 = ((y-120)*30) - ((x-20)*30)
    quad_2_3 = ((y-150)*25) - ((x-50)*35)
    quad_2_4 = ((y-185)*(-50))
    
    #check kite
    if kite_line_1 > 0 and kite_line_2 > 0 and kite_line_3 < 0 and kite_line_4 < 0 or point.distance(kite) <= radius+clearance:
        flag = True
    
    #check rectangle
    if rect_line_1 < 0 and rect_line_2 > 0 and rect_line_3 > 0 and rect_line_4 < 0 or point.distance(rectangle) <= radius+clearance:
        flag = True
    
    #check polygon
    if quad_1_1>0 and quad_1_2>0 and quad_1_3<0 and quad_1_4<0:
        flag_1 = True
    else:
        flag_1 = 0

    if quad_2_1 < 0 and quad_2_2 > 0 and quad_2_3 > 0 and quad_2_4 > 0:
        flag_2 = True
    else:
        flag_2 = 0

    if flag_1 == 1 or flag_2 == 1 or point.distance(complex_polygon) <= radius+clearance:
        flag = True
    
    #circle
    if(((x - (225))**2 + (y - (150))**2 - (25+radius+clearance)**2) <= 0) :
        flag = True
        
    #ellipse
    if (((x - (150))/(40+radius+clearance))**2 + ((y - (100))/(20+radius+clearance))**2 - 1) <= 0:
        flag = True    
    return flag


print(obstacleSpace(100,75,0,0))