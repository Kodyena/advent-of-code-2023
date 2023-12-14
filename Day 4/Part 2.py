import numpy as np

lines: list[str] = open("Day 4\input.txt").read().splitlines()
number_of_matches = []
for line in lines:
    card_value = 0
    nums = line.split(':')[1].split('|')
    winning_numbers = set([int(num) for num in nums[0].split()])
    numbers = set([int(num) for num in nums[1].split()])
    number_of_matches.append(len(winning_numbers & numbers))

scratchcard_count = np.ones(len(lines))
for n, matches in enumerate(number_of_matches):
    for i in range(matches):
        scratchcard_count[i + n + 1] += scratchcard_count[n]
        
print(sum(scratchcard_count))