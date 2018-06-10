class PlayingCard():
    def __init__(self, card_code, ace_high=True):
        self.value = self.valueconverter(card_code[0], ace_high)
        self.suit = card_code[1]
    def valueconverter(self, value, ace_high):
        numerical = 0
        if value == "A":
            if ace_high is True:
                numerical = 14
            else:
                numerical = 1
        elif value == "K":
            numerical = 13
        elif value == "Q":
            numerical = 12
        elif value == "J":
            numerical = 11
        elif value == "T":
            numerical = 10
        else:
            numerical = int(value)
        return numerical

class PokerHand():
    def __init__(self, hand_codes, ace_high=True):
        card_codes = hand_codes.split(" ")
        self.cards = []
        for card in card_codes:
            self.cards.append(PlayingCard(card, ace_high))
        # Store the cards lowest to highest value
        self.cards.sort(key=lambda x: x.value)
        self.score = [0, 0, 0, 0]
        # First digit in score corresponds to hand type HC = 1, OP, TP, TK, S, F, FH, FK, SF = 9
        # Second, third and fourth  digits detail the hand and the interpretation is different for each hand
        # but the values can always be compare in a simple and meaningful way
        # examples:
        # [HC, 10, 0, 0] means high card 10
        # [OP, 2, 14, 0] means one pair 2's and high card value 14 (ace)
        # [TP, 8, 4, 3] means two pair 8's and 4's, high card 3
        # [TK, 7, 10, 0] means three-of-a-kind 7's with high card 10
        # [S, 9, 0, 0] means straight ending at 9
        # [F, 8, 0, 0] means flush with 8 as the high card
        # [FH, 9, 2, 0] means full-house with three 9's and two 2's
        # [FK, 3, 8, 0] means four-of-a-kind 3's with 8 high card
        # [SF, 14, 0, 0] means a straight flush ending on 14 (ace) i.e. a royal flush
        # Thus hands can be compared by simple numerical comparisons of each element until a winner is found
        self.handscore()

    def findgroups(self):
        # This relies on the cards being in value order from the constructor
        self.pairs = []
        self.triples = []
        self.quadruples = []
        i = 0
        while i < 4:
            value = self.cards[i].value
            if self.cards[i+1].value == value:
                if (i+2 < 5 and self.cards[i+2].value != value) or i+2 > 4:
                    # This is a pair and not a three of a kind/four of a kind
                    self.pairs.append(value)
                    i = i + 2
                    continue
                elif (i+3 < 5 and self.cards[i+3].value != value) or i+3 > 4:
                    # This is a three of a kind not a four of a kind
                    self.triples.append(value)
                    i = i + 3
                    continue
                else:
                    # This is a four of a kind
                    self.quadruples.append(value)
                    break  # We cannot find anymore pairs/3's
            else:
                i += 1
        return

    def isflush(self):
        suit = self.cards[0].suit
        self.flush = True  # Assume true and try to disprove it
        for card in self.cards[1:]:
            if card.suit != suit:
                self.flush = False
                break
        return

    def isstraight(self):
        # This relies on the fact we sorted the cards by value in the constructor
        count = self.cards[0].value
        self.straight = True  # Assume true and try to disprove it
        for card in self.cards[1:]:
            count += 1
            if card.value != count:
                self.straight = False
                break
        return

    def handscore(self):
        self.isstraight()
        self.isflush()
        self.findgroups()
        if self.straight is True:
            if self.flush is True:
                # Straight flush
                self.score[0] = 9
                self.score[1] = max(self.cards, key=lambda x: x.value).value
            else:
                # Straight
                self.score[0] = 5
                self.score[1] = max(self.cards, key=lambda x: x.value).value
        elif self.flush is True:
            # Flush
            self.score[0] = 6
            self.score[1] = max(self.cards, key=lambda x: x.value).value
        elif len(self.quadruples) == 1:
            # Four-of-a-kind
            self.score[0] = 8
            self.score[1] = self.quadruples[0]
            self.score[2] = max([card for card in self.cards if card.value != self.score[1]],
                                key=lambda x: x.value).value
        elif len(self.triples) == 1 and len(self.pairs) == 1:
            # Full house
            self.score[0] = 7
            self.score[1] = self.triples[0]
            self.score[2] = self.pairs[0]
        elif len(self.triples) == 1:
            # Three of a kind
            self.score[0] = 4
            self.score[1] = self.triples[0]
            self.score[2] = max([card for card in self.cards if card.value != self.score[1]],
                                key=lambda x: x.value).value
        elif len(self.pairs) == 2:
            # Two pair
            self.score[0] = 3
            self.score[1] = max(self.pairs)
            self.score[2] = min(self.pairs)
            self.score[3] = max([card for card in self.cards if card.value != self.score[1] and card.value != self.score[2]],
                                key=lambda x: x.value).value
        elif len(self.pairs) == 1:
            # One pair
            self.score[0] = 2
            self.score[1] = self.pairs[0]
            self.score[2] = max([card for card in self.cards if card.value != self.score[1]],
                                key=lambda x: x.value).value
        else:
            # High card
            self.score[0] = 1
            self.score[1] = max(self.cards, key=lambda x: x.value).value
        return
    
    def __gt__(self, other):
        if isinstance(other, PokerHand) is False:
            raise TypeError
        for i in range(len(self.score)):
            if self.score[i] > other.score[i]:
                return True
            elif self.score[i] < other.score[i]:
                return False
        return False

    def __lt__(self, other):
        if isinstance(other, PokerHand) is False:
            raise TypeError
        for i in range(len(self.score)):
            if self.score[i] < other.score[i]:
                return True
            elif self.score[i] > other.score[i]:
                return False
        return False

if __name__ == '__main__':
    p1_wins = 0
    f = open("pe0054_poker.txt")
    for showdown in f.readlines():
        p1 = PokerHand(showdown[:14])
        p2 = PokerHand(showdown[15:])
        if p1 > p2:
            p1_wins += 1
    f.close()
    print(p1_wins)
            
            