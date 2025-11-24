"""Utility functions for game mechanics."""

import math

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


def pseudo_random(seed: int, modulo: int) -> int:
    """Generate pseudo-random number based on seed."""
    value = math.sin(seed * 12.9898) * 43758.5453
    fractional_part = value - math.floor(value)
    result = int(fractional_part * modulo)
    return result


def trigger_trap(game_state: dict) -> None:
    """Trigger a trap that causes negative consequences."""
    from game.constants import DAMAGE_ROLL_MODULO, DAMAGE_THRESHOLD
    
    print("Trap activated! The floor starts shaking...")
    
    inventory = game_state['player_inventory']
    
    if inventory:
        # Randomly remove an item
        item_index = pseudo_random(game_state['steps_taken'], len(inventory))
        lost_item = inventory.pop(item_index)
        print(f"You lost {lost_item}!")
    else:
        # Player takes damage
        damage_roll = pseudo_random(game_state['steps_taken'], DAMAGE_ROLL_MODULO)
        if damage_roll < DAMAGE_THRESHOLD:
            print("You couldn't avoid the trap! Game over.")
            game_state['game_over'] = True
        else:
            print("You managed to avoid the worst of it, but you're shaken.")


def random_event(game_state: dict) -> None:
    """Trigger a random event during movement."""
    from game.constants import (
        EVENT_PROBABILITY_MODULO,
        EVENT_PROBABILITY_THRESHOLD,
        EVENT_TYPE_COUNT,
    )
    
    # Check if event occurs (10% chance)
    event_roll = pseudo_random(
        game_state['steps_taken'],
        EVENT_PROBABILITY_MODULO
    )
    
    if event_roll == EVENT_PROBABILITY_THRESHOLD:
        # Choose which event occurs
        event_type = pseudo_random(
            game_state['steps_taken'] + 1,
            EVENT_TYPE_COUNT
        )
        
        if event_type == 0:
            # Finding a coin
            room_name = game_state['current_room']
            room = ROOMS[room_name]
            if 'coin' not in room['items']:
                room['items'].append('coin')
                print("You found a coin on the floor!")
        
        elif event_type == 1:
            # Hearing a rustle
            print("You hear a rustle nearby...")
            inventory = game_state['player_inventory']
            if 'sword' in inventory:
                print("You brandish your sword and scare away the creature!")
            else:
                print("You feel uneasy, but nothing happens.")
        
        elif event_type == 2:
            # Trap trigger
            room_name = game_state['current_room']
            inventory = game_state['player_inventory']
            
            if room_name == 'trap_room' and 'torch' not in inventory:
                print(
                    "Danger! The trap room is especially treacherous "
                    "without light!"
                )
                trigger_trap(game_state)


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
    
    # Get valid answers from config (including alternatives)
    from game.constants import ANSWER_ALTERNATIVES
    
    # Check if correct answer belongs to any alternative group
    valid_answers = None
    for alternatives_set in ANSWER_ALTERNATIVES:
        if correct_answer_lower in alternatives_set:
            valid_answers = alternatives_set
            break
    
    # If no alternatives found, use only the correct answer
    if valid_answers is None:
        valid_answers = {correct_answer_lower}
    
    # Check if answer is correct (including alternatives)
    is_correct = user_answer in valid_answers
    
    if is_correct:
        print("Correct! You solved the puzzle!")
        room['puzzle'] = None
        
        # Room-specific rewards
        if room_name == 'hall':
            print("You feel a sense of accomplishment.")
        elif room_name == 'trap_room':
            print("The tiles stop moving. Safe passage is now open!")
        elif room_name == 'library':
            print("A hidden compartment opens! You found something useful.")
        else:
            print("You feel a sense of accomplishment.")
    else:
        print("Incorrect. Try again.")
        # Trigger trap if in trap_room
        if room_name == 'trap_room':
            trigger_trap(game_state)


def show_help() -> None:
    """Display available commands."""
    from game.constants import COMMANDS
    
    print("\nAvailable commands:")
    for command, description in COMMANDS.items():
        print(f"  {command:<16} - {description}")

