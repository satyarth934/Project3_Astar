import os
import sys
import math
import numpy as np
import matplotlib.pyplot as plt
sys.dont_write_bytecode = True

import sattu
import obstacles


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
    markNodeXY(marker_node.getXYCoords(), plotter=plotter, color=color, marker=marker)


def plotPath(path, rev=False, pause_time=0.001, plotter=plt, color="black", linewidth=2, write_path_prefix=-1, show=False, skip_frames=8):
    if rev:
        path_plt = path[::-1]
    else:
        path_plt = path

    for i, node_itr in enumerate(path_plt):
        plot_curve(node_itr, color=color, plotter=plotter, linewidth=linewidth)
        if i % skip_frames == 0:
            if write_path_prefix > -1:
                write_path = os.path.join(sattu.OUTPUT_DIR, str(write_path_prefix) + ".png")
                plt.savefig(write_path)
                write_path_prefix += 1

            if show:
                plt.show()
                plt.pause(pause_time)

    return write_path_prefix

# def plotNodes(node_list, plotter=plt):
#     pass


def initPlot(start_xy, goal_xy, title=""):
    fig, ax = plt.subplots()
    fig.suptitle(title, fontsize=16)

    ax.set(xlim=(-5, 5), ylim = (-5, 5))
    ax.set_aspect('equal')

    obstacles.generateMap(plotter=ax)

    markNodeXY(start_xy, plotter=ax, color='#00FF00', marker='o')
    markNodeXY(goal_xy, plotter=ax, color='#FF0000', marker='^')

    return ax
