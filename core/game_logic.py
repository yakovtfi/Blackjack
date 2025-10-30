from core.player_io import ask_player_action

def calculate_hand_value(hand: list[dict]) -> int:
    value_map = {
        '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
        '7': 7, '8': 8, '9': 9, '10': 10,
        'J': 10, 'Q': 10, 'K': 10, 'A': 11
    }
    
    total_value = 0
    ace_count = 0
    
    for card in hand:
        rank = card['rank']
        total_value += value_map[rank]
        if rank == 'Ace':
            ace_count += 1
    
    while total_value > 21 and ace_count:
        total_value -= 10
        ace_count -= 1
    
    return total_value

def deal_two_each(deck: list[dict], player: dict, dealer: dict) -> None:
    player['hand'] = [deck.pop(0), deck.pop(0)]
    dealer['hand'] = [deck.pop(0), deck.pop(0)]


def dealer_play(deck: list[dict], dealer: dict) -> bool:
    while calculate_hand_value(dealer['hand']) < 17:
        dealer['hand'].append(deck.pop(0))
    
    return calculate_hand_value(dealer['hand']) > 21



def run_full_game(deck: list[dict], player: dict, dealer: dict) -> None:
    deal_two_each(deck, player, dealer)

    print("\nDealer's upcard:", f"{dealer['hand'][0]['rank']} of {dealer['hand'][0]['suit']}")
    print("Your hand:", [f"{card['rank']} of {card['suit']}" for card in player['hand']])
    print("Your total:", calculate_hand_value(player['hand']))


    while True:
        player_value = calculate_hand_value(player['hand'])
        if player_value > 21:
            print(" Your total is", player_value)
            break

        action = ask_player_action()
        if action == 'hit':
            new_card = deck.pop(0)
            player['hand'].append(new_card)
            print("You drew:", f"{new_card['rank']} of {new_card['suit']}")
            print("Your total:", calculate_hand_value(player['hand']))
        else:
            break

    if player_value <= 21:
        print("\nDealer's turn...")
        print("Dealer's full hand:", [f"{card['rank']} of {card['suit']}" for card in dealer['hand']])
        
        dealer_busted = dealer_play(deck, dealer)
        dealer_value = calculate_hand_value(dealer['hand'])
        
        print("Dealer's final hand:", [f"{card['rank']} of {card['suit']}" for card in dealer['hand']])
        print("Dealer's total:", dealer_value)
        
        if dealer_busted:
            print("Dealer busts!")
            player['status'] = 'win'
        elif player_value > dealer_value:
            player['status'] = 'win'
        elif player_value < dealer_value:
            player['status'] = 'lose'
        else:
            player['status'] = 'push'
    else:
        player['status'] = 'bust'