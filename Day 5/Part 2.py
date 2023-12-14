lines = open("Day 5/input.txt").read().splitlines()
seeds = [int(seed) for seed in lines[0].split(':')[1].split()]
seed_ranges = [[seeds[2*i] , seeds[2*i] +  seeds[(2 * i) + 1] - 1] for i in range((len(seeds) + 1 )// 2)]
maps = []
for line in lines[2:]:
    if ':' in line:
        maps.append([])
    elif line != '':
        maps[-1].append([int(n) for n in line.split()])

#Applys a mapping consisting of a list of source ranges to destination ranges 
def apply_map(seed_ranges: list[list[int, int]], map: list[int, int, int]):
    mapped_ranges=[]
    for dest_start, source_start, range in map:
        source_end = source_start + range - 1
        unmapped_ranges=[]
        for seed_range_start, seed_range_end in seed_ranges:
            
            #Check ranges overlap
            if seed_range_end < source_start or seed_range_start > source_end: 
                unmapped_ranges.append([seed_range_start, seed_range_end])
                continue

            #Find intersections and break ranges 
            if seed_range_start < source_start and seed_range_end >= source_start:
                unmapped_ranges.append([seed_range_start, source_start - 1])
                seed_range_start = source_start
            if seed_range_end > source_end and seed_range_start <= source_end:
                unmapped_ranges.append([source_end + 1, seed_range_end])
                seed_range_end = source_start + range
            
            #map overlapping segments to new range
            if source_start <= seed_range_start and seed_range_end <= source_end:
                seed_destination = seed_range_start - source_start + dest_start
                #We don't want to further map already mapped ranges
                mapped_ranges.append([seed_destination, seed_destination + (seed_range_end - seed_range_start)])

        seed_ranges = unmapped_ranges
    seed_ranges.extend(mapped_ranges)
    return seed_ranges

#Go through each range and split according to mapping ranges
for map in maps:
    seed_ranges = apply_map(seed_ranges, map)

print(min([location[0] for location in seed_ranges]))