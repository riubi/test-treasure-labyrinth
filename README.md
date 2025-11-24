# Treasure Labyrinth

Text adventure game "Treasure Labyrinth" - explore rooms, solve puzzles, collect items, and find the treasure!

## Description

Treasure Labyrinth is a simple console-based text game.

## Installation

```bash
make install
```

## Running

```bash
make project
```

## Gameplay

### Basic Commands

- `go <direction>` or `<direction>` - Move in a direction (north/south/east/west)
- `look` - Examine the current room
- `take <item>` - Pick up an item from the room
- `use <item>` - Use an item from your inventory
- `inventory` - Show your inventory
- `solve` - Attempt to solve a puzzle in the current room
- `help` - Show available commands
- `quit` - Exit the game

### Game Demo

[![asciicast](https://asciinema.org/a/MxBGTNzaom26KAyXYj73h1pwG.svg)](https://asciinema.org/a/MxBGTNzaom26KAyXYj73h1pwG)

## Project Structure

```
game/
├── __init__.py          # Package initialization
├── constants.py         # Game data (rooms, commands, constants)
├── main.py              # Entry point and game loop
├── player_actions.py    # Player-related functions
└── utils.py             # Utility functions (room descriptions, puzzles, events)
```

## Requirements

- Python 3.9+
- Poetry (for dependency management)