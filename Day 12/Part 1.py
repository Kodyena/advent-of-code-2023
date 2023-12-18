import re 
lines = open("Day 12/test.txt").read().splitlines()
spring_sets = [line.split()[0] for line in lines]
spring_sizes = [[int(d) for d in re.findall("\d+", line.split()[1])] for line in lines]

for sizes, spring_set in zip(spring_sizes, spring_sets):
    start = 1
    #Add dots to start and end for pre and post char checks
    sizes.append('.')
    sizes.insert(0, '.')
    table = [[0] * len(spring_set)] * len(sizes)
    for j, size in enumerate(sizes):
        count = 0
        #Determine number of positions to check based on group size
        possible_placements = len(spring_set) - sum(sizes) - len(sizes) + 1

        for i in range(start, start + possible_placements):
            if '.' not in sizes[i:i+size] and '#' != sizes[i-1] and sizes[i+size+1]:
                count += 1
            
            table[j][i] = count
