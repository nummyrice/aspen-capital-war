from war_game import Deck, Game

deck_a = Deck('cal')
deck_b = Deck('sam')
game_x = Game(deck_a, deck_b)
print(game_x.play())
