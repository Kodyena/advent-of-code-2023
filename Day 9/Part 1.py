lines = open("Day 9/inputs.txt").read().splitlines()
histories = [[int(n) for n in line.split()] for line in lines]

#Recursively compute the differences between values, then sum the last results
def get_next(history):
    differences = [values[1] - values[0] for values in zip(history, history[1:])]
    if any(n != 0  for n in differences):
        return get_next(differences) + history[-1]
    else:
        return history[-1]
    


extrapolated_values = []
for h in histories:
    extrapolated_values.append(get_next(h))

print(sum(extrapolated_values))