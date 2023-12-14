import re
import numpy as np

lines = open("Day 8\input.txt").read().splitlines()
instructions = lines[0]
location_map = {matches[0]: [matches[1], matches[2]] for line in lines[2:] if (matches := re.findall(r"([A-Z]+)", line))}

#Get all locations ending in A
locations = list(filter(lambda l: l[-1] == 'A', location_map.keys()))

number_of_steps = 0
steps_to_reach = []

#Assume that the path is cyclical, find the path length for each location and determine the lcm
for location in locations:
    while location[-1] != 'Z':
        if(instructions[number_of_steps % len(instructions)] == 'R'):
            location = location_map.get(location)[1]
        else:
            location = location_map.get(location)[0]
        number_of_steps += 1
    
    steps_to_reach.append(number_of_steps)
    number_of_steps = 0

#Use object dtype to make sure return fits in int64
print(np.lcm.reduce(steps_to_reach, dtype=object))