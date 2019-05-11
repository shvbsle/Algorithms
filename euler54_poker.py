# euler 54

'''
rank rules (low to highest):

10 High Card: Highest value card.
9 One Pair: Two cards of the same value.
8 Two Pairs: Two different pairs.
7 Three of a Kind: Three cards of the same value.
6 Straight: All cards are consecutive values.
5 Flush: All cards of the same suit.
4 Full House: Three of a kind and a pair.
3 Four of a Kind: Four cards of the same value.
2 Straight Flush: All cards are consecutive values of same suit.
1 Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.


compute wins for p1

'''

import sys
# ip = sys.stdin.read().split('\n')
ip = open("ip.txt", 'r').read().split('\n')

# ip = """
# 5H 5C 6S 7S KD 2C 3S 8S 8D TD,
# 5D 8C 9S JS AC 2C 5C 7D 8S QH,
# 2D 9C AS AH AC 3D 6D 7D TD QD,
# 4D 6S 9H QH QC 3D 6D 7H QD QS,
# 2H 2D 4C 4D 4S 3C 3D 3S 9S 9D,
# KH JS 4H 5D 9D 2D 3D 4D 5D 6D""".split(',')

# wins of player 1 and 2
wins = {1 : 0,
        2: 0,
        3: 0}

ORDER = {'2':1, '3':2, '4':3, '5':4, '6':5, '7':6, '8':7, '9':8, 'T':9, 'J':10, 'Q':11, 'K':12, 'A':13}
ORDER_IN = {v:k for k,v in ORDER.items()}

def is_consecutive(cards):
        order = [ORDER[c] for c in cards]
        order.sort()
        # count spacing between 2 elements in a sorted lists
        spacing = [b-a for a,b in list(zip(order, order[1:]))]
        # print(spacing, order)
        if max(spacing) == 1 and len(set(spacing)) == 1:
                return 1
        return False

def freq(cards):
        freq_d = {}
        for card in cards:
                if card in freq_d:
                        freq_d[card]+=1
                else:
                        freq_d[card] = 1
        return freq_d

def evaluate(p1, p2):
        p1_ranks, p2_ranks = [99], [99]
        p1_cards = [s[0] for s in p1]
        p2_cards = [s[0] for s in p2]

        p1_suit = [s[1] for s in p1]
        p2_suit = [s[1] for s in p2]
        
        p1_freq = freq(p1_cards)
        p2_freq = freq(p2_cards)

        # royal flush
        if set(p1_cards) == {'T', 'J', 'K', 'Q', 'A'} and len(set(p1_suit)) ==1:
                p1_ranks.append(1)
        if set(p2_cards) == {'T', 'J', 'K', 'Q', 'A'} and len(set(p1_suit)) == 1:
                p2_ranks.append(1)

        # straight flush
        if len(set(p1_suit)) == 1 and is_consecutive(p1_cards):
                p1_ranks.append(2)
        if len(set(p2_suit)) == 1 and is_consecutive(p2_cards):
                p2_ranks.append(2)
        
        # four of a kind
        if 4 in p1_freq.values():
                p1_ranks.append(3)
        if 4 in p2_freq.values():
                p2_ranks.append(3)
        
        # four of a kind
        if 3 in p1_freq.values() and 2 in p1_freq.values():
                p1_ranks.append(4)
        if 3 in p2_freq.values() and 2 in p2_freq.values():
                p2_ranks.append(4)
        
        # flush
        if len(set(p1_suit)) == 1:
                p1_ranks.append(5)
        if len(set(p2_suit)) == 1:
                p2_ranks.append(5)
        
        # straight
        if is_consecutive(p1_cards):
                p1_ranks.append(6)
        if is_consecutive(p2_cards):
                p2_ranks.append(6)
        
        # three of a kind
        if 3 in p1_freq.values():
                p1_ranks.append(7)
        if 3 in p2_freq.values():
                p2_ranks.append(7)
        
        # two pairs
        if 2 in p1_freq.values() and list(p1_freq.values()).count(2) == 2:
                p1_ranks.append(8)
        if 2 in p2_freq.values() and list(p2_freq.values()).count(2) == 2:
                p2_ranks.append(8)
        
        # pair
        if 2 in p1_freq.values() and list(p1_freq.values()).count(2) == 1:
                p1_ranks.append(9)
        if 2 in p2_freq.values() and list(p2_freq.values()).count(2) == 1:
                p2_ranks.append(9)
        
        # highest card
        if max([ORDER[c] for c in p1_cards]) > max([ORDER[c] for c in p2_cards]):
                p1_ranks.append(10)
        elif max([ORDER[c] for c in p1_cards]) < max([ORDER[c] for c in p2_cards]):
                p2_ranks.append(10)
        
        p1_min = min(p1_ranks)
        p2_min = min(p2_ranks)

        if p1_min == p2_min:
                # print('Tie :(')
                p1mags, p2mags = p1_min, p2_min
                seen = []
                while p1mags == p2mags:
                        p1mags = max([ORDER[c] for c in p1_cards if ORDER[c] not in seen])
                        p2mags = max([ORDER[c] for c in p2_cards  if ORDER[c] not in seen])
                        seen.append(p1mags)
                if p1mags > p2mags: return 1
                else: return 2

        if p1_min<p2_min:
                return 1
        else: return 2


for match in ip:
        match = match.split()
        p1, p2 = match[:5], match[5:]
        winner = evaluate(p1, p2)
        wins[winner]+=1

        # print(wins)

print(wins[1])

