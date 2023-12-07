import re

with open('Day 2\input.txt') as f:
    id_count = 0
    game_powers = []
    for line in f:
        max_red = max([int(n) for n in re.findall('(\d+) red', line)], default=0)
        max_blue = max([int(n) for n in re.findall('(\d+) blue', line)], default=0)
        max_green = max([int(n) for n in re.findall('(\d+) green', line)], default=0)
        
        game_powers.append(max_red * max_blue * max_green)

print(sum(game_powers))