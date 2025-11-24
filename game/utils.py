"""Utility functions for game mechanics."""

from game.constants import ROOMS
from game.player_actions import get_input


def describe_current_room(game_state: dict) -> None:
    """Describe the current room to the player."""
    room_name = game_state['current_room']
    room = ROOMS[room_name]
    
    print(f"\n== {room_name.upper().replace('_', ' ')} ==")
    print(room['description'])
    
    if room['items']:
        print("Notable items:")
        for item in room['items']:
            print(f"  - {item}")
    
    if room['exits']:
        print("Exits:")
        for direction, target_room in room['exits'].items():
            print(f"  - {direction}: {target_room.replace('_', ' ')}")
    
    if room['puzzle'] is not None:
        print("It seems there is a puzzle here (use the 'solve' command).")


def solve_puzzle(game_state: dict) -> None:
    """Attempt to solve the puzzle in the current room."""
    from game.constants import ROOMS
    
    room_name = game_state['current_room']
    room = ROOMS[room_name]
    
    if room['puzzle'] is None:
        print("There are no puzzles here.")
        return
    
    question, correct_answer = room['puzzle']
    print(f"\n{question}")
    
    user_answer = get_input("Your answer: ").strip().lower()
    correct_answer_lower = str(correct_answer).strip().lower()
    
    if user_answer == correct_answer_lower:
        print("Correct! You solved the puzzle!")
        room['puzzle'] = None
        
        # Add reward if applicable
        if room_name == 'treasure_room':
            # Special handling for treasure room puzzle
            pass
        else:
            print("You feel a sense of accomplishment.")
    else:
        print("Incorrect. Try again.")


def attempt_open_treasure(game_state: dict) -> None:
    """Attempt to open the treasure chest."""
    from game.constants import ROOMS
    
    room_name = game_state['current_room']
    room = ROOMS[room_name]
    
    if room_name != 'treasure_room' or 'treasure_chest' not in room['items']:
        print("There is no treasure chest here.")
        return
    
    inventory = game_state['player_inventory']
    
    # Check if player has the key
    if 'treasure_key' in inventory or 'rusty_key' in inventory:
        key_name = 'treasure_key' if 'treasure_key' in inventory else 'rusty_key'
        print(f"You use the {key_name}, and the lock clicks. The chest opens!")
        room['items'].remove('treasure_chest')
        print("There is treasure in the chest! You won!")
        game_state['game_over'] = True
        return
    
    # If no key, offer to enter code
    print("The chest is locked. You need a key or a code to open it.")
    response = get_input("Enter code? (yes/no): ").strip().lower()
    
    if response == 'yes':
        if room['puzzle'] is not None:
            question, correct_answer = room['puzzle']
            print(f"\n{question}")
            code = get_input("Enter code: ").strip().lower()
            correct_answer_lower = str(correct_answer).strip().lower()
            
            if code == correct_answer_lower:
                print("The code is correct! The chest opens!")
                room['items'].remove('treasure_chest')
                room['puzzle'] = None
                print("There is treasure in the chest! You won!")
                game_state['game_over'] = True
            else:
                print("Incorrect code. The chest remains locked.")
        else:
            print("The chest requires a key. The puzzle has already been solved.")
    else:
        print("You step back from the chest.")


def show_help() -> None:
    """Display available commands."""
    print("\nAvailable commands:")
    print("  go <direction>  - go in direction (north/south/east/west)")
    print("  look            - examine the current room")
    print("  take <item>     - pick up an item")
    print("  use <item>      - use an item from inventory")
    print("  inventory       - show inventory")
    print("  solve           - attempt to solve the puzzle in the room")
    print("  quit            - exit the game")
    print("  help            - show this message")

