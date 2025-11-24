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

