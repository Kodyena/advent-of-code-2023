from functools import reduce
#Units: 1 mm, 1 ms
lines: list[str] = open("Day 6\input.txt").read().splitlines()
times: list[int] = [int(n) for n in lines[0].split(':')[1].split()]
distances: list[int] = [int(n) for n in lines[1].split(':')[1].split()]

number_of_wins = []
for time, distance in zip(times, distances):
    win_count = 0
    for n in range(1, time):
        if n * (time - n) > distance:
            win_count += 1
    number_of_wins.append(win_count)
print(number_of_wins)
print(reduce(lambda x, y: x*y, number_of_wins))