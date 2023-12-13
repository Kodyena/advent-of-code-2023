import re 

lines = open("Day 3\input.txt").read().splitlines()

parts = []
gear_ratio_count = 0

#Get all parts
for i, line in enumerate(lines):
    parts.append([])
    for part in re.finditer(r"\d+", line):
        start = part.start(0) - 1
        end = part.end(0)
        num = int(part.group(0))
        parts[i].append((start, end, num))

#Iterate over each line
for i, line in enumerate(lines):
    for j, char in enumerate(line):
        #If no * skip
        if char != '*':
            continue

        gear_parts = []
    
        #Check neighbouring rows for part numbers
        for n in [-1, 0, 1]:
            if(i + n < 0 or i + n > len(lines)):
                continue

            for start, end, part_number in parts[i + n]:
                if start <= j <= end:
                    gear_parts.append(part_number)
        
        #If two adj parts add their gear ratio to count
        if len(gear_parts) == 2:
            gear_ratio_count += gear_parts[0] * gear_parts[1]

print(gear_ratio_count)