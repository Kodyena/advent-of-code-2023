lines = open("Day 9/inputs.txt").read().splitlines()
histories = [[int(n) for n in line.split()] for line in lines]

#Compute the same but take the first values and remove them recursively 
def get_next(history):
    differences = [values[1] - values[0] for values in zip(history, history[1:])]
    if any(n != 0  for n in differences):
        return  history[0] - get_next(differences)
    else:
        return history[0]
    


extrapolated_values = []
for h in histories:
     extrapolated_values.append(get_next(h))

print(sum(extrapolated_values))