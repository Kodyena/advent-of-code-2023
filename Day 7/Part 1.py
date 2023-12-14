from operator import itemgetter
from functools import cmp_to_key
card_value_map = {
    'T': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14, 
    '1': 1, 
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9
}

number_rank_map = {6: "FIVE OF A KIND", 5: "FOUR OF A KIND", 4: "FULL HOUSE", 3: "THREE OF A KIND", 2: "TWO PAIR", 1: "ONE PAIR", 0: "HIGH CARD"}

def check_rank(card: str):
    char_set = set(card)
    num_of_chars = len(char_set)
    char_freqs = [card.count(char) for char in char_set]
    match num_of_chars:
        case 1: 
            return 6
        case 4: 
            return 1
        case 5: 
            return 0
        case 2:
            if 4 in char_freqs:
                return 5
            else:
                return 4
        case 3:
            if 3 in char_freqs:
                return 3
            else:
                return 2
        case default:
            return

def check_high_card(card1:list[int, str, int], card2:list[int, str, int]):
    for char1, char2 in zip(card1[1], card2[1]):
        if char1 != char2:
            return card_value_map.get(char1) - card_value_map.get(char2)
    
    return 0

card_and_bid = [[line.split()[0], line.split()[1]] for line in open("Day 7\input.txt").read().splitlines()]
rank_highcard_bid = []
for card, bid in card_and_bid:
    rank_highcard_bid.append([check_rank(card), card, int(bid)])
rank_highcard_bid.sort(key=cmp_to_key(check_high_card))
rank_highcard_bid.sort(key=itemgetter(0))

count = 0
for i, bid in enumerate(rank_highcard_bid):
    count += (i + 1) * bid[2]

print(count)