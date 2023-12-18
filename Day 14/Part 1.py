grid =  open("Day 14/inputs.txt").read().splitlines()
#Rotate grid by 90 to make manips easier 
grid = list(zip(*grid[::-1]))

#Want to move O rocks as far right as possible 
count = 0
for row in grid:
    #Get list of fixed and movable rock positions
    round_rocks = [i for i, char in enumerate(row) if char == 'O']
    fixed_rocks = [i for i, char in enumerate(row) if char == '#']

    #Add rock at end to mimic end of platform
    fixed_rocks.append(len(row))
    new_positions = []
    #For each of the furthest rocks, move them until they hit the closest fixed rock and then add that rock to the fixed list
    for rock in reversed(round_rocks):
        next_rock = min([fixed_rock for fixed_rock in fixed_rocks if fixed_rock > rock])
        new_positions.append(next_rock)
        fixed_rocks.append(next_rock - 1)
    count += sum(new_positions)

print(count)