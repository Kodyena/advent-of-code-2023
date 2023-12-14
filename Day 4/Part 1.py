lines: list[str] = open("Day 4\input.txt").read().splitlines()
points = 0
for line in lines:
    card_value = 0
    nums = line.split(':')[1].split('|')
    winning_numbers = set([int(num) for num in nums[0].split()])
    numbers = set([int(num) for num in nums[1].split()])
    matches = len(winning_numbers & numbers)
    if matches:
        points += 2 ** (matches - 1)

print(points)

