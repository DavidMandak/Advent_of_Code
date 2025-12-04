import copy
from PIL import Image
import time

lines = open("2024/Inputs/input14.txt").read().splitlines()

t = time.time()
total = 1
map_size = (101, 103)
time = 100
quadrants = [0]*4
for line in lines:
    line = line.split()
    pos = list(map(int, line[0][2:].split(",")))
    vel = list(map(int, line[1][2:].split(",")))
    final_pos = (pos[0]+time*vel[0]) % map_size[0], (pos[1]+time*vel[1]) % map_size[1]
    quadrant = 0
    if final_pos[0] != map_size[0]//2 and final_pos[1] != map_size[1]//2:
        if final_pos[0] > map_size[0]//2:
            quadrant += 1
        if final_pos[1] > map_size[1]//2:
            quadrant += 2
        quadrants[quadrant] += 1
for quadrant in quadrants:
    total *= quadrant
print(total)

save = [256]*map_size[0]*map_size[1]
for time in range(52, 10**4, 101):
    graph = copy.deepcopy(save)
    for line in lines:
        line = line.split()
        pos = list(map(int, line[0][2:].split(",")))
        vel = list(map(int, line[1][2:].split(",")))
        final_pos = (pos[0]+time*vel[0]) % map_size[0], (pos[1]+time*vel[1]) % map_size[1]
        graph[final_pos[1]*map_size[0]+final_pos[0]] = 0
    output = Image.new("L", (map_size[0], map_size[1]))
    output.putdata(graph)
    output.save("Advent_of_Code_14_images/AoC_"+str(time)+".jpg")
print(time.time()-t)
