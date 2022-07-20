from flask import Blueprint, request
from .war_game import Cards, Deck, Game
from pprint import pprint
from .models import db, Player

api_routes = Blueprint('api_routes', __name__)

@api_routes.route('start-game', methods=['POST'])
def get_decks():
    '''
        when this route is reached:
            - add player1 and player2 names to the database
            - a deck for player_1 and player_2 are created and returned
    '''
    data = request.get_json()
    player_1 = data['player_1'].strip()
    player_2 = data['player_2'].strip()
    # make sure player name is not empty, trim white space
    if len(player_1) > 20 or len(player_2) > 20:
        return "player names must be under 20 characters", 400
    # get player name from database
    player_1_db_result = db.session.query(Player).filter(Player.name == player_1).first()
    player_2_db_result = db.session.query(Player).filter(Player.name == player_2).first()
    # or add to database if doesn't exist
    if not player_1_db_result:
        player_1_db_result = Player(name=player_1)
        db.session.add(player_1_db_result)
    if not player_2_db_result:
        player_2_db_result = Player(name=player_2)
        db.session.add(player_2_db_result)
    if not player_1_db_result or not player_2_db_result:
        db.session.commit()
    cards = Cards()
    cards.shuffle()
    delt_cards = cards.deal()
    player_1_deck = Deck(delt_cards[0], player_1)
    player_2_deck = Deck(delt_cards[1], player_2)
    game = Game(player_1_deck, player_2_deck)
    play_script = game.play()
    winner = play_script[-1]['winner']
    #update player records
    if winner == 'tie':
        player_1_db_result.ties += 1
        player_2_db_result.ties += 1
    elif winner == player_1_db_result.name:
        player_1_db_result.wins += 1
        player_2_db_result.losses += 1
    else:
        player_1_db_result.losses += 1
        player_2_db_result.wins += 1
    db.session.commit()
    return {'play_script': play_script}

@api_routes.route('/all-time-record')
def get_records():
    '''
        when this route is reached:
            - the records for player_1 and player_2 are returned

    '''
    return "Record"
