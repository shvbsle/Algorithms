# euler 54
import sys
# ip = sys.stdin.read().split('\n')
ip = open("ip.txt", 'r').read().split('\n')
wins = {1 : 0,
        2: 0}

ORDER = {'2':1, '3':2, '4':3, '5':4, '6':5, '7':6, '8':7, '9':8, 'T':9, 'J':10, 'Q':11, 'K':12, 'A':13}

def is_consecutive(cards):
        order = [ORDER[c] for c in cards]
        order.sort()
        spacing = [b-a for a,b in list(zip(order, order[1:]))]
        if max(spacing) == 1 and len(set(spacing)) == 1:return 1
        return False

def freq(cards):
        freq_d = {}
        for card in cards:
                if card in freq_d:freq_d[card]+=1
                else:freq_d[card] = 1
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
        if list(p1_freq.values()).count(2) == 2:
                p1_ranks.append(8)
        if list(p2_freq.values()).count(2) == 2:
                p2_ranks.append(8)
        
        # pair
        if list(p1_freq.values()).count(2) == 1:
                p1_ranks.append(9)
        if list(p2_freq.values()).count(2) == 1:
                p2_ranks.append(9)
        
        # highest card
        if max([ORDER[c] for c in p1_cards]) > max([ORDER[c] for c in p2_cards]):
                p1_ranks.append(10)
        elif max([ORDER[c] for c in p1_cards]) < max([ORDER[c] for c in p2_cards]):
                p2_ranks.append(10)
        
        p1_min,p2_min = min(p1_ranks),min(p2_ranks)

        if p1_min == p2_min:
                p1mags, p2mags = p1_min, p2_min
                if p1_min == 9:
                        p1mags = max([ORDER[c] for c in p1_cards if p1_freq[c] == 2])
                        p2mags = max([ORDER[c] for c in p2_cards if p2_freq[c] == 2])
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

# wins for p1
match_results_my = {}
for match in ip:
        match = match.split()
        p1, p2 = match[:5], match[5:]
        wins[evaluate(p1, p2)]+=1
print(wins[1])