import re 
import numpy as np

special_characters = "\"!@#$%^&*()-+?_=,<>/"
with open("Day 3\input.txt") as f:
    char_arr = np.array([[char for char in line] for line in f.readlines()])
    numbers = []
    engine_part = False
    current_number = ""

    for i in range(len(char_arr)):
        for j in range(len(char_arr)):
            char = char_arr[i][j]
            if(char.isdigit()):
                current_number += char
                adj_chars = char_arr[max(i-1,0):i+2,max(j-1,0):j+2].flatten()
                adj_chars = [char for char in adj_chars if char != '\n']
                if(any([char not in '.0123456789' for char in adj_chars])):
                    engine_part = True
            elif((current_number != '' or char_arr[i][j+1] == '\n') and engine_part):
                numbers.append(int(current_number))
                engine_part=False
            if(not char.isdigit()): 
                current_number=""

    print(sum(numbers))