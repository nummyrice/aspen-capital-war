from random import shuffle
from collections import deque
# Define a class to categorize each card, provide shuffle
class Deck:
    def __init__(self, name: str) -> dict:
        self.player = name
        global values, suites
        values = [v for v in range(2, 15)]
        suites = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        card_list = []
        for s in suites:
            for v in values:
                card = (s, v)
                card_list.append(card)
        self.cards = deque(card_list)

    def pop_card(self) -> tuple:
        return self.cards.pop()

    def add_to_bottom(self, card_or_cards: list[tuple]) -> None:
        self.cards.extendleft(card_or_cards)

    def draw_three(self) -> list:
        return [self.cards.pop(), self.cards.pop(), self.cards.pop()]

    def print_deck(self) -> None:
        print(self.cards)
        print(len(self.cards))
        print(self.player)

# objDeck = Deck('nick')
# objDeck.print_deck()
# print(objDeck.draw_three())
