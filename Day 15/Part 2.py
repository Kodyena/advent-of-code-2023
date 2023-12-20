import re 

sequence = open("Day 15/inputs.txt").read().split(",")

def apply_hashmap(label: str) -> int:
    current_value = 0
    for char in label:
        current_value = (ord(char) + current_value) * 17
        current_value %= 256
        
    return current_value

def remove_lens(boxes: dict[int, list[tuple[str, int]]], box_number: int, lens_label: str):
    if not box_number in boxes:
        return
    
    box = boxes.get(box_number)
    box = [lens for lens in box if lens[0] != lens_label]
    if len(box) == 0:
        boxes.pop(box_number)
    else:
        boxes[box_number] = box

def add_lens(boxes: dict[int, list[tuple[str, int]]], box_number: int, lens_label: str, lens_focal: int):
    box = boxes.get(box_number, [])
    labels = [lens[0] for lens in box]

    if lens_label in labels:
        i = labels.index(lens_label)
        box[i] = (lens_label, lens_focal)
    else:
        box.append((lens_label, lens_focal))

    boxes[box_number] = box

def slot_lenses(sequence: list[str]) -> list[list[str]]:
    boxes = {}
    for step in sequence:
        label, op = re.match("([a-z]+)([-,=])", step).groups()
        box_number = apply_hashmap(label)
        if op == '-':
            remove_lens(boxes, box_number, label)
        else:
            add_lens(boxes, box_number, label, int(step[-1]))

    return boxes

boxes = slot_lenses(sequence)
focal_powers = [sum([(j + 1) * f[1] for j, f in enumerate(box)]) * (box_number + 1) for box_number, box in boxes.items()]

print(sum(focal_powers))