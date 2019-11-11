import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import random
import time

nb = np.zeros((4,1))

# continous ploting in MATLAB
x = np.linspace(0,10*np.pi,100)
y = np.sin(x)

plt.ion()

rows = 100
cols = 100

start_coords = (1,1)
goal_coords = (80,90)

map = np.zeros((rows,cols))
distanceFromStart = np.full((rows,cols), np.inf)
parent = np.zeros((rows,cols))
display_map = np.zeros((rows,cols))

map[0:5,5] = 1

np.place(display_map, map==0,1)
np.place(display_map, map==1,2)

#sub2ind
start_c = np.ravel_multi_index(start_coords,(rows,cols),order = 'C')
goal_c  = np.ravel_multi_index(goal_coords,(rows,cols),order = 'C')
current = start_c

distanceFromStart.flat[current] = 0

fig = plt.figure()
ax = fig.add_subplot(111)

show_map = False;

while 1:
    display_map.flat[start_c] = 5
    display_map.flat[goal_c]  = 6

    if(show_map):
        ax.matshow(display_map)
        fig.canvas.draw()

    display_map.flat[current] = 3

    [min_dist,current]=[distanceFromStart.min(),distanceFromStart.argmin()]

    if(current == goal_c):
        break

    #ind2sub
    (i,j) =  np.unravel_index(current,(rows,cols))

    nb = np.zeros((4,1))

    if i>0:
        up = np.ravel_multi_index((i-1,j),(rows,cols),order = 'C')
        if(display_map.flat[up] == 1 or display_map.flat[up] == 4 or display_map.flat[up] == 6):
            nb[0] = 1

    if j>0:
        left = np.ravel_multi_index((i,j-1),(rows,cols),order = 'C')
        if(display_map.flat[left] == 1 or display_map.flat[left] == 4 or display_map.flat[left] == 6):
            nb[1] = 1

    if i<rows-1:
        down = np.ravel_multi_index((i+1,j),(rows,cols),order = 'C')
        if(display_map.flat[down] == 1 or display_map.flat[down] == 4 or display_map.flat[down] == 6):
            nb[2] = 1

    if j<cols-1:
        right = np.ravel_multi_index((i,j+1),(rows,cols),order = 'C')
        if(display_map.flat[right] == 1 or display_map.flat[right] == 4 or display_map.flat[right] == 6):
            nb[3] = 1

    if nb[0]==1:
        display_map.flat[up]=4;
        if(distanceFromStart.flat[up]>distanceFromStart[i,j]+1):
            distanceFromStart.flat[up]=distanceFromStart[i,j]+1
        parent.flat[up] = current

    if nb[1]==1:
        display_map.flat[left]=4;
        if(distanceFromStart.flat[left]>distanceFromStart[i,j]+1):
            distanceFromStart.flat[left]=distanceFromStart[i,j]+1
        parent.flat[left] = current

    if nb[2]==1:
        display_map.flat[down]=4;
        if(distanceFromStart.flat[down]>distanceFromStart[i,j]+1):
            distanceFromStart.flat[down]=distanceFromStart[i,j]+1
        parent.flat[down] = current

    if nb[3]==1:
        display_map.flat[right]=4;
        if(distanceFromStart.flat[right]>distanceFromStart[i,j]+1):
            distanceFromStart.flat[right]=distanceFromStart[i,j]+1
        parent.flat[right] = current

    distanceFromStart.flat[current] = np.inf

route = []

route.append(goal_c)

while (parent.flat[int(route[0])] != 0):
    route = [int(parent.flat[route[0]])] + route

for k in range(1,len(route)-1):
    display_map.flat[route[k]] = 7
    ax.matshow(display_map)
    fig.canvas.draw()
