sequence = open("Day 15/test.txt").read().split(",")

sequence_values = []
for token in sequence:
    current_value = 0
    for char in token:
        current_value = (ord(char) + current_value) * 17
        current_value %= 256
    
    sequence_values.append(current_value)
    
print(sum(sequence_values))