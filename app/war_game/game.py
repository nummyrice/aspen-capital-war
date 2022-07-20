class Game:
    def __init__(self, deck_a, deck_b):
        self.deck_a = deck_a
        self.deck_b = deck_b
        self.play_script = []
        self.turns = 0

    def get_card_string(self, card: tuple):
        suit, val = card[0], card[1]
        card_string = suit
        if val > 10:
            if val == 11:
                card_string = f"Jack of {card_string}"
            elif val == 12:
                card_string = f"Queen of {card_string}"
            elif val == 13:
                card_string = f"King of {card_string}"
            else:
                card_string = f"Ace of {card_string}"
        else:
            card_string = f"{val} of {card_string}"
        return card_string

    def tie(self, tie_stack: list[tuple]) -> None:
        '''
            handles tie scenario
            breaks out if either deck runs out of cards
            recurses if tie continues
        '''
        self.turns += 1
        turn_record = {
            'turn': self.turns,
            'remaining_cards_a': len(self.deck_a.cards),
            'remaining_cards_b': len(self.deck_b.cards),
        }
        card_a, card_b = None, None
        for i in range(4):
            if not self.deck_a.cards or not self.deck_b.cards:
                return
            elif i == 3:
                card_a = self.deck_a.pop_card()
                card_b = self.deck_b.pop_card()
            else:
                tie_stack.append(self.deck_a.pop_card())
                tie_stack.append(self.deck_b.pop_card())
        turn_record['card_a_string'] = self.get_card_string(card_a)
        turn_record['card_b_string'] = self.get_card_string(card_b)
        turn_record['tie_stack'] = len(tie_stack)
        if card_a[1] > card_b[1]:
            turn_record['result'] = self.deck_a.player
            self.play_script.append(turn_record)
            tie_stack.extend([card_a, card_b])
            self.deck_a.add_to_bottom(tie_stack)
        elif card_a[1] < card_b[1]:
            turn_record['result'] = self.deck_b.player
            self.play_script.append(turn_record)
            tie_stack.extend([card_b, card_a])
            self.deck_b.add_to_bottom(tie_stack)
        else:
            turn_record['result'] = 'tie'
            self.play_script.append(turn_record)
            tie_stack.extend([card_a, card_b])
            self.tie(tie_stack)

    def turn(self) -> None:
        '''
            handles a single (card flip for both players)
            adds record to play_script or passes handling to self.tie
        '''
        self.turns += 1
        card_a = self.deck_a.pop_card()
        card_b = self.deck_b.pop_card()
        turn_record = {
            'turn': self.turns,
            'remaining_cards_a': len(self.deck_a.cards),
            'remaining_cards_b': len(self.deck_b.cards),
            'card_a_string': self.get_card_string(card_a),
            'card_b_string': self.get_card_string(card_b)
        }
        if card_a[1] > card_b[1]:
            turn_record['result'] = self.deck_a.player
            self.play_script.append(turn_record)
            self.deck_a.add_to_bottom([card_a, card_b])
        elif card_a[1] < card_b[1]:
            turn_record['result'] = self.deck_b.player
            self.play_script.append(turn_record)
            self.deck_b.add_to_bottom([card_b, card_a])
        else:
            turn_record['result'] = 'tie'
            self.play_script.append(turn_record)
            self.tie([card_a, card_b])

    def play(self) -> list[dict]:
        while self.deck_a.cards and self.deck_b.cards:
            self.turn()
        result = {
            'turns': self.turns
        }
        if not self.deck_a and not self.deck_b:
            result['result'] = 'tie'
            self.play_script.append(result)
            return self.play_script
        elif self.deck_a:
            result['result'] = self.deck_a.player
        else:
            result['result'] = self.deck_b.player
        self.play_script.append(result)
        return self.play_script
