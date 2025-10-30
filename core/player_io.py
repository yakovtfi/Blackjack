def ask_player_action() -> str:
    while True:
        action = input("Would you like to 'H' or 'S'? ").strip()
        if action in ['H', 'S']:
            return action
        print("Invalid input. Please enter 'hit' or 'stand'.")
