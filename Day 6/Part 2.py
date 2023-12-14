#Can compute the number of wins by calculating the difference of the roots of the equation x*(t-x)-d
from math import sqrt

lines: list[str] = open("Day 6\input.txt").read().splitlines()
t: int = int(lines[0].split(':')[1].replace(' ', ''))
d: int = int(lines[1].split(':')[1].replace(' ', ''))

root = sqrt(t**2 - 4*d)
root_nve = (t - root) // 2
root_pve = (t + root) // 2

print(root_pve - root_nve)