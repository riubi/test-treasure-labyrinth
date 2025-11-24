"""Game constants and room definitions."""

ROOMS = {
    'entrance': {
        'description': (
            'You are in a dark entrance to the labyrinth. '
            'The walls are covered with moss. '
            'An old torch lies on the floor.'
        ),
        'exits': {'north': 'hall', 'east': 'trap_room'},
        'items': ['torch'],
        'puzzle': None
    },
    'hall': {
        'description': (
            'A large hall with an echo. '
            'In the center stands a pedestal with a sealed chest.'
        ),
        'exits': {'south': 'entrance', 'west': 'library', 'north': 'treasure_room'},
        'items': [],
        'puzzle': (
            'There is an inscription on the pedestal: '
            '"Name the number that comes after nine." '
            'Enter the answer as a digit or word.',
            '10'
        )
    },
    'trap_room': {
        'description': (
            'A room with a tricky tile floor. '
            'There is an inscription on the wall: "Beware - trap".'
        ),
        'exits': {'west': 'entrance'},
        'items': ['rusty_key'],
        'puzzle': (
            'The tile system is active. To pass, say the word "step" '
            'three times in a row (enter "step step step")',
            'step step step'
        )
    },
    'library': {
        'description': (
            'A dusty library. Old scrolls on the shelves. '
            'There might be a key to the treasury somewhere here.'
        ),
        'exits': {'east': 'hall', 'north': 'armory'},
        'items': ['ancient_book'],
        'puzzle': (
            'In one scroll there is a riddle: '
            '"What grows when it is eaten?" (answer one word)',
            'resonance'
        )
    },
    'armory': {
        'description': (
            'An old armory. A sword hangs on the wall, '
            'next to it is a small bronze box.'
        ),
        'exits': {'south': 'library'},
        'items': ['sword', 'bronze_box'],
        'puzzle': None
    },
    'treasure_room': {
        'description': (
            'A room with a large chest on the table. '
            'The door is locked - a special key is needed.'
        ),
        'exits': {'south': 'hall'},
        'items': ['treasure_chest'],
        'puzzle': (
            'The door is protected by a code. Enter the code '
            '(hint: this is the number of a fivefold step, 2*5= ? )',
            '10'
        )
    }
}

COMMANDS = {
    "go <direction>": "go in direction (north/south/east/west)",
    "north/south/east/west": "move in direction (shortcut)",
    "look": "examine the current room",
    "take <item>": "pick up an item",
    "use <item>": "use an item from inventory",
    "inventory": "show inventory",
    "solve": "attempt to solve the puzzle in the room",
    "quit": "exit the game",
    "help": "show this message",
}

# Valid answer alternatives for puzzles
# List of sets, where each set contains equivalent answers
ANSWER_ALTERNATIVES = [
    {'10', 'ten', 'десять'},
]

# Game mechanics constants
EVENT_PROBABILITY_MODULO = 10  # For random event probability (10% chance)
EVENT_PROBABILITY_THRESHOLD = 0  # Event occurs when roll equals this
EVENT_TYPE_COUNT = 3  # Number of different event types

DAMAGE_ROLL_MODULO = 10  # For trap damage calculation
DAMAGE_THRESHOLD = 3  # Player dies if damage roll is below this

