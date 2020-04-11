import matplotlib.pyplot as plt
import numpy as np
import math


def plot_curve(curr_node, plotter=plt):
    try:
        Xi, Yi = curr_node.getXYCoords()
        Thetai = curr_node.orientation
        UL, UR = curr_node.action
    except Exception as e:
        print("Cannot plot the curve for this node.")
        return
    
    t = 0
    r = 0.038
    L = 0.354
    dt = 0.1
    Xn=Xi
    Yn=Yi
    # Thetan = 3.14 * Thetai / 180
    Thetan = math.radians(Thetai)

# Xi, Yi,Thetai: Input point's coordinates
# Xs, Ys: Start point coordinates for plot function
# Xn, Yn, Thetan: End point coordintes

    while t<1:
        t = t + dt
        Xs = Xn
        Ys = Yn
        Xn += 0.5*r * (UL + UR) * math.cos(Thetan) * dt
        Yn += 0.5*r * (UL + UR) * math.sin(Thetan) * dt
        Thetan += (r / L) * (UR - UL) * dt
        plotter.plot([Xs, Xn], [Ys, Yn], color="blue")

    # Thetan = 180 * (Thetan) / 3.14
    Thetan = math.degrees(Thetan)
    return Xn, Yn, Thetan


def markNode(marker_node, plotter=plt, color='#EE82EE', marker='o'):
    x, y = marker_node.getXYCoords()
    plotter.plot(x, y, color=color, marker=marker, markersize=7)
