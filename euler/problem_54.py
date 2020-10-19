import collections


class Solution:

    card_ranks = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
                  'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

    @classmethod
    def count_wins(cls, filename, hand):
        file = open(filename, 'r')
        count = 0
        for line in file.readlines():
            winner = Solution.get_winner(line)
            if winner == hand:
                count += 1
        return count

    @classmethod
    def get_winner(cls, cards):
        cards = cards.split(" ")
        c1 = []
        c2 = []
        for i in range(0, 5):
            c1.append((cls.card_ranks[cards[i][0]], cards[i][1]))
            c2.append((cls.card_ranks[cards[i + 5][0]], cards[i + 5][1]))
        c1 = list(map(list, zip(*sorted(c1))))
        c2 = list(map(list, zip(*sorted(c2))))
        r1 = cls.rank_cards(c1[0], c1[1])
        r2 = cls.rank_cards(c2[0], c2[1])
        return cls.compare_ranks(r1, r2)

    @classmethod
    def compare_ranks(cls, r1, r2):
        for i in range(0, len(r1)):
            if r1[i] > r2[i]:
                return 1
            elif r1[i] < r2[i]:
                return 2
        raise Exception("Equal hands")

    @classmethod
    def rank_cards(cls, p, s):
        counter = collections.Counter(p)
        counter_values = sorted(counter.values())
        mc = counter.most_common()
        single_suit = len(set(s)) == 1

        # Straight Flush / Royal Flush
        if single_suit and p[-1] - p[0] == 4 and mc[0][1] == 1:
            return [9, p[-1]]
        # Four of a Kind
        if mc[0][1] == 4:
            return [8, mc[0][0]] + [mc[1][0]]
        # Full House
        if counter_values == [2, 3]:
            return [7, mc[0][0], mc[1][0]]
        # Flush
        if single_suit == 1:
            return [6] + list(reversed(p))
        # Straight
        if p[-1] - p[0] == 4 and mc[0][1] == 1:
            return [5, p[-1]]
        # Three of a Kind
        if mc[0][1] == 3:
            return [4, mc[0][0]] + sorted([mc[1][0], mc[2][0]], reverse=True)
        # Two Pairs
        if counter_values == [1, 2, 2]:
            return [3] + sorted([mc[0][0], mc[1][0]], reverse=True) + [mc[2][0]]
        # One Pair
        if mc[0][1] == 2:
            return [2, mc[0][0]] + sorted([mc[1][0], mc[2][0], mc[3][0]], reverse=True)
        # High Card
        return [1] + list(reversed(p))
