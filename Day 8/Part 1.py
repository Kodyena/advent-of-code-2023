import re
lines = open("Day 8\input.txt").read().splitlines()
instructions = lines[0]
location_map = {matches[0]: [matches[1], matches[2]] for line in lines[2:] if (matches := re.findall(r"([A-Z]+)", line))}

current_location = 'AAA'
number_of_steps = 0
while current_location != 'ZZZ':
    if(instructions[number_of_steps % len(instructions)] == 'R'):
        current_location = location_map.get(current_location)[1]
    else:
        current_location = location_map.get(current_location)[0]
    number_of_steps += 1

print(number_of_steps)