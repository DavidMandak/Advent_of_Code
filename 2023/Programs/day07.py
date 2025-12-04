import time

lines = open("2023/Inputs/input07.txt").read().splitlines()
quintuplet_hand, quintuplet_bid = [], []
quadruplet_hand, quadruplet_bid = [], []
full_house_hand, full_house_bid = [], []
triplet_hand, triplet_bid = [], []
two_pair_hand, two_pair_bid = [], []
pair_hand, pair_bid = [], []
high_hand, high_bid = [], []

t = time.time()
total = 0
for line in lines:
    hand = line.split(" ")[0]
    bid = int(line.split(" ")[1])
    cards = {}
    for card in hand:
        if card not in cards:
            cards[card] = 1
        else:
            cards[card] += 1
    if "J" in cards:
        if len(cards) == 1:
            quintuplet_hand.append(hand)
            quintuplet_bid.append(bid)
            continue
        else:
            joker = cards["J"]
            cards.pop("J")
            high = 0
            high_card = None
            for number in cards:
                if cards[number] > high:
                    high = cards[number]
                    high_card = number
            cards[high_card] += joker
    if len(cards) == 1:
        quintuplet_hand.append(hand)
        quintuplet_bid.append(bid)
    elif len(cards) == 2:
        if 1 < cards[list(cards)[0]] < 4:
            full_house_hand.append(hand)
            full_house_bid.append(bid)
        else:
            quadruplet_hand.append(hand)
            quadruplet_bid.append(bid)
    elif len(cards) == 3:
        for x in cards:
            if cards[x] == 3:
                triplet_hand.append(hand)
                triplet_bid.append(bid)
                break
            elif cards[x] == 2:
                two_pair_hand.append(hand)
                two_pair_bid.append(bid)
                break
    elif len(cards) == 4:
        pair_hand.append(hand)
        pair_bid.append(bid)
    else:
        high_hand.append(hand)
        high_bid.append(bid)


def setup(card):
    if card.isdigit() is True:
        return int(card)
    elif card == "T":
        return 10
    elif card == "J":
        return 1
    elif card == "Q":
        return 12
    elif card == "K":
        return 13
    else:
        return 14


def check(other, hand):
    k = 0
    while hand[k] == other[k]:
        k += 1
    hand_comparison = setup(hand[k])
    other_comparison = setup(other[k])
    if hand_comparison == other_comparison:
        exit("lulw")
    elif hand_comparison < other_comparison:
        return True
    else:
        return False


rank = 1
for hands, bids in (high_hand, high_bid), (pair_hand, pair_bid), (two_pair_hand, two_pair_bid),\
        (triplet_hand, triplet_bid), (full_house_hand, full_house_bid), (quadruplet_hand, quadruplet_bid),\
        (quintuplet_hand, quintuplet_bid):
    for i in range(1, len(hands)):
        hand = hands[i]
        bid = bids[i]
        j = i
        while j > 0 and check(hands[j-1], hand):
            hands[j] = hands[j-1]
            hands[j-1] = hand
            bids[j] = bids[j-1]
            bids[j-1] = bid
            j -= 1
rank = 1
for bids in high_bid, pair_bid, two_pair_bid, triplet_bid, full_house_bid, quadruplet_bid, quintuplet_bid:
    for bid in bids:
        total += bid*rank
        rank += 1
print(total)
print(time.time()-t)
