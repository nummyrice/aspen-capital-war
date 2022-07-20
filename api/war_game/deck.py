from random import shuffle
from collections import deque
from pprint import pprint
# Define a class to categorize each card, provide shuffle
class Cards:
    def __init__(self):
        global values, suites
        values = [v for v in range(2, 15)]
        suites = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.card_list = []
        for s in suites:
            for v in values:
                card = (s, v)
                self.card_list.append(card)

    def shuffle(self) -> None:
        shuffle(self.card_list)

    def deal(self) -> tuple[list]:
        divided_a = []
        divided_b = []
        for i in range(52):
            if i % 2 > 0:
                divided_a.append(self.card_list[i])
            else:
                divided_b.append(self.card_list[i])
        return (divided_a, divided_b)


class Deck:
    def __init__(self, card_list:list[tuple], name:str) -> None:
        self.cards = deque(card_list)
        self.player = name

    def pop_card(self) -> tuple:
        return self.cards.pop()

    def add_to_bottom(self, card_or_cards: list[tuple]) -> None:
        self.cards.extendleft(card_or_cards)
        # print('---------------------')
        # print(card_or_cards)
        # print(self.cards)

    def draw_three(self) -> list:
        return [self.cards.pop(), self.cards.pop(), self.cards.pop()]

    def print_deck(self) -> None:
        print(self.cards)
        print(len(self.cards))

# objDeck = Deck('nick')
# objDeck.print_deck()
# print(objDeck.draw_three())
