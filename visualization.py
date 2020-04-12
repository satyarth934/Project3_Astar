import matplotlib.pyplot as plt
import numpy as np
import math


def plot_curve(curr_node, plotter=plt, color="blue", linewidth=1):
    try:
        Xi, Yi = curr_node.getParentXYCoords()
        Thetai = curr_node.parent_orientation
        UL, UR = curr_node.action
    except Exception:
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
        plotter.plot([Xs, Xn], [Ys, Yn], color=color, linewidth=linewidth)

    # Thetan = 180 * (Thetan) / 3.14
    Thetan = math.degrees(Thetan)
    return Xn, Yn, Thetan


def markNodeXY(marker_node_xy, plotter=plt, color='#EE82EE', marker='o'):
    x, y = marker_node_xy
    plotter.plot(x, y, color=color, marker=marker, markersize=7)


def markNode(marker_node, plotter=plt, color='#EE82EE', marker='o'):
    x, y = marker_node.getXYCoords()
    plotter.plot(x, y, color=color, marker=marker, markersize=7)


def plotPath(path, rev=False, pause_time=0.001, plotter=plt, color="black", linewidth=2):
    if rev:
        path_plt = path[::-1]
    else:
        path_plt = path

    for node_itr in path_plt:
        plot_curve(node_itr, color=color, plotter=plotter, linewidth=linewidth)
        plt.pause(pause_time)
