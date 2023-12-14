lines = open("Day 5\input.txt").read().splitlines()
seeds = [int(seed) for seed in lines[0].split(':')[1].split()]

maps = []
for line in lines[2:]:
    if ':' in line:
        maps.append([])
    elif line != '':
        maps[-1].append([int(n) for n in line.split()])

#Applys a mapping consisting of a list of source ranges to destination ranges 
def apply_map(n: int, map: list[int, int, int]):
    for dest_start, source_start, number in map:
        if 0 < n - source_start < number:
            return n - source_start + dest_start
        
    return n 

locations = []
for seed in seeds:
    for map in maps:
        seed = apply_map(seed, map)
    locations.append(seed)

print(min(locations))