import re

digit_dict = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
def get_calibration_value(line: str):
    nums = re.findall(f"(?=(\d|{'|'.join(digit_dict.keys())}))", line)
    return int(digit_dict.get(nums[0], nums[0]) + digit_dict.get(nums[-1], nums[-1]))

calibration_values = []
with open('Day 1\input.txt') as f:
    for line in f:
        calibration_values.append(get_calibration_value(line))

print(sum(calibration_values))