from core.deck import build_standard_deck, shuffle_by_suit
from core.game_logic import *
from core.player_io import ask_player_action



if __name__ == "__main__":
    deck = build_standard_deck()
    shuffled_deck = shuffle_by_suit(deck)

    player = {'hand': [], 'status': ''}
    dealer = {'hand': []}
    run_full_game(shuffled_deck, player, dealer)


    run_full_game(shuffled_deck, player, dealer)


