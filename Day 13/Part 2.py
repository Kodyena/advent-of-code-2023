maps = [map.splitlines() for map in open("Day 13/inputs.txt").read().split("\n\n")]
count = 0

#Check if there is a single difference in the reflection
def check_smudge(pairs):
    diffs = [sum([1 for i in range(len(pair[0])) if pair[0][i] != pair[1][i]]) for pair in pairs]
    return sum(diffs) == 1

def get_reflection_value(map: list[str]):
    for i in range(1, len(map)):
        if check_smudge(list(zip(reversed(map[:i]), map[i:]))):
            return i * 100 
        
    return int(((get_reflection_value(list(zip(*map)))) / 100))

values = list(map(lambda m: get_reflection_value(m), maps))
print(sum(values))