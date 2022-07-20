from war_game import Deck, Game, Cards
from pprint import pprint
for i in range(100):
    cards = Cards()
    cards.shuffle()
    cards_tuple = cards.deal()
    deck_1 = Deck(cards_tuple[0], 'cal')
    deck_2 = Deck(cards_tuple[1], 'john')
    game = Game(deck_1, deck_2)
    # game.play()
    # pprint(game.play())
    pprint(game.play()[-1]['winner'])
