"""Player actions and inventory management."""


def get_input(prompt="> ") -> str:
    """Get user input with error handling."""
    try:
        return input(prompt).strip()
    except (KeyboardInterrupt, EOFError):
        print("\nExiting the game.")
        return "quit"


def show_inventory(game_state: dict) -> None:
    """Display player inventory."""
    inventory = game_state['player_inventory']
    if inventory:
        print("Your inventory:")
        for item in inventory:
            print(f"  - {item}")
    else:
        print("Your inventory is empty.")


def move_player(game_state: dict, direction: str) -> None:
    """Move player to a new room in the specified direction."""
    from game.constants import ROOMS
    from game.utils import describe_current_room, random_event

    current_room_name = game_state['current_room']
    current_room = ROOMS[current_room_name]

    if direction in current_room['exits']:
        new_room_name = current_room['exits'][direction]

        # Check if trying to enter treasure_room
        if new_room_name == 'treasure_room':
            inventory = game_state['player_inventory']
            if 'rusty_key' not in inventory:
                print("The door is locked. You need a key to go further.")
                return
            else:
                print(
                    "You use the found key to open the path to the treasure room."
                )

        game_state['current_room'] = new_room_name
        game_state['steps_taken'] += 1
        print(f"You go {direction}.")
        describe_current_room(game_state)

        # Trigger random event after movement
        random_event(game_state)
    else:
        print("You cannot go in that direction.")


def take_item(game_state: dict, item_name: str) -> None:
    """Take an item from the current room."""
    from game.constants import ROOMS

    current_room_name = game_state['current_room']
    current_room = ROOMS[current_room_name]

    if item_name == 'treasure_chest':
        print("You cannot pick up the chest, it is too heavy.")
        return

    if item_name in current_room['items']:
        game_state['player_inventory'].append(item_name)
        current_room['items'].remove(item_name)
        print(f"You picked up: {item_name}")
    else:
        print("There is no such item here.")


def use_item(game_state: dict, item_name: str) -> None:
    """Use an item from inventory."""
    from game.utils import attempt_open_treasure

    inventory = game_state['player_inventory']

    if item_name not in inventory:
        print("You don't have such an item.")
        return

    current_room = game_state['current_room']

    # Check if using key on treasure chest
    if item_name in ('treasure_key', 'rusty_key') and current_room == 'treasure_room':
        attempt_open_treasure(game_state)
        return

    if item_name == 'torch':
        print("You light the torch. It becomes brighter around you.")
    elif item_name == 'sword':
        print("You feel more confident with the sword in your hands.")
    elif item_name == 'bronze_box':
        print("You open the bronze box.")
        if 'rusty_key' not in inventory:
            inventory.append('rusty_key')
            print("You found a rusty_key inside!")
        else:
            print("The box is empty.")
    else:
        print(f"You don't know how to use {item_name}.")
