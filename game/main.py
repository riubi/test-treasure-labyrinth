#!/usr/bin/env python3

"""Main game entry point and game loop."""

from game.player_actions import (
    get_input,
    move_player,
    show_inventory,
    take_item,
    use_item,
)
from game.utils import (
    attempt_open_treasure,
    describe_current_room,
    show_help,
    solve_puzzle,
)


def process_command(game_state: dict, command: str) -> None:
    """Process user command."""
    command_parts = command.lower().strip().split()
    
    if not command_parts:
        return
    
    cmd = command_parts[0]
    
    # Check for single-word direction commands
    directions = ['north', 'south', 'east', 'west', 'n', 's', 'e', 'w']
    direction_map = {'n': 'north', 's': 'south', 'e': 'east', 'w': 'west'}
    
    if cmd in directions:
        direction = direction_map.get(cmd, cmd)
        move_player(game_state, direction)
    elif cmd == 'look':
        describe_current_room(game_state)
    elif cmd == 'go':
        if len(command_parts) > 1:
            direction = command_parts[1]
            move_player(game_state, direction)
        else:
            print("Go where? Specify a direction (north/south/east/west).")
    elif cmd == 'take':
        if len(command_parts) > 1:
            item_name = ' '.join(command_parts[1:])
            take_item(game_state, item_name)
        else:
            print("Take what? Specify an item name.")
    elif cmd == 'use':
        if len(command_parts) > 1:
            item_name = ' '.join(command_parts[1:])
            use_item(game_state, item_name)
        else:
            print("Use what? Specify an item name.")
    elif cmd in ('inventory', 'inv'):
        show_inventory(game_state)
    elif cmd == 'solve':
        room_name = game_state['current_room']
        
        # In treasure_room, always call attempt_open_treasure
        if room_name == 'treasure_room':
            attempt_open_treasure(game_state)
        else:
            solve_puzzle(game_state)
    elif cmd == 'help':
        show_help()
    elif cmd in ('quit', 'exit'):
        print("Thanks for playing!")
        game_state['game_over'] = True
    else:
        print(f"Unknown command: {cmd}. Type 'help' for available commands.")


def main() -> None:
    """Game entry point."""
    # Initialize game state
    game_state = {
        'player_inventory': [],
        'current_room': 'entrance',
        'game_over': False,
        'steps_taken': 0
    }
    
    # Welcome message
    print("Welcome to the Treasure Labyrinth!")
    print("Type 'help' for available commands.\n")
    
    # Describe starting room
    describe_current_room(game_state)
    
    # Main game loop
    while not game_state['game_over']:
        command = get_input("\n> ")
        
        if command:
            process_command(game_state, command)
    
    print(f"\nGame over! Steps taken: {game_state['steps_taken']}")


if __name__ == "__main__":
    main()
