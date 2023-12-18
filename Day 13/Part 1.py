maps = [map.splitlines() for map in open("Day 13/inputs.txt").read().split("\n\n")]

def get_reflection_value(map: list[str]):
    for i in range(1, len(map)):
        if all(pair[1] == pair[0] for pair in zip(reversed(map[:i]), map[i:])):
            return i * 100 
        
    return int(((get_reflection_value(list(zip(*map)))) / 100))

values = list(map(lambda m: get_reflection_value(m), maps))
print(sum(values))
        