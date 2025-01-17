# Text Game: Room Navigation

## Overview
This is a Python-based text game where users can navigate through a virtual house using simple text commands. The house consists of multiple rooms, each with a unique description. Users can move left, right, up, or down within the house, with boundaries and limits enforced. The game provides feedback on movements, tracks the number of steps taken, and allows users to stop the game at any time.

## Features
- Navigate through a grid of rooms.
- Receive descriptions of each room.
- Enforced boundaries to prevent moving outside the grid.
- Tracks the number of steps taken by the user.
- Option to stop the game at any time.

## How to Play
1. Run the game using Python:
   ```bash
   python adventure_game.py
   ```
2. A welcome message and the house's floor plan will be displayed.
3. You will start in the **kitchen**. The game will prompt you to enter a direction:
   - `left`
   - `right`
   - `up`
   - `down`
   - `stop` to exit the game.
4. Move through the rooms by typing a direction. If a move is invalid (e.g., hitting a wall), you will be notified.
5. The game will display the description of the current room and the total number of steps taken after each valid move.
6. Type `stop` to end the game.

## Room Descriptions
- **Kitchen**: "kitchen, where the spice of life comes alive."
- **Bedroom**: "bedroom, where the magic happens."
- **Office**: "office, the source of wealth."
- **Toilet**: "toilet, you know what happens here."
- **Storage**: "storage, where there are all sorts of stuff."
- **Guest Room**: "guest room, where you have friends."

## Floor Plan
```
 -------------------------------------------
|   Kitchen   |   Bedroom    |   Office     |
 -------------------------------------------
|   Toilet    |   Storage    |  Guest Room  |
 -------------------------------------------
```

## Code Structure
1. **`welcome_message()`**: Prints the welcome message and the house's floor plan.
2. **`move(current_row_index, current_column_index, direction, room)`**: Handles movement logic, checks boundaries, and returns the updated position.
3. **`main()`**: Main function that initializes the game, tracks user input, and manages the game loop.

## Example Gameplay
```
Welcome to my house! You can stop any time by typing 'stop'.

Here is the floor plan of the house:

 -------------------------------------------
|   Kitchen   |   Bedroom    |   Office     |
 -------------------------------------------
|   Toilet    |   Storage    |  Guest Room  |
 -------------------------------------------

You are in kitchen, where the spice of life comes alive.
Which direction would you like to move to?
Please enter left/right/up/down/stop: right

You moved to the bedroom, where the magic happens.

Total walks taken: 1
```

## Requirements
- Python 3.6 or higher

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/bytesbyt/ds_katas.git
   ```
2. Navigate to the directory:
   ```bash
   cd src
   ```
3. Run the game:
   ```bash
   python adventure_game.py
   ```

