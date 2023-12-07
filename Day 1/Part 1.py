import re

def get_calibration_value(line: str):
    nums = re.findall("\d", line)
    return int(nums[0] + nums[-1])

calibration_values = []
with open('Day 1\input.txt') as f:
    for line in f:
        calibration_values.append(get_calibration_value(line))

print(sum(calibration_values))