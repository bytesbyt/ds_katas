
# Mad Libs Generator

## Overview
The Mad Libs Generator is a Python-based program that creates a fun and interactive experience where users provide various inputs (e.g., nouns, adjectives, verbs), which are then used to fill in the blanks of a prewritten story template. Inspired by the classic Mad Libs game, this program combines user creativity with automation to generate unique and entertaining stories.

## Features
- **Interactive Prompts**: The program asks the user for specific inputs, such as an adjective, a noun, or a verb.
- **Story Generation**: Inputs are dynamically placed into a predefined story template to create a custom story.
- **Input Validation**: Ensures that users do not leave inputs blank.
- **Replayability**: Easily extendable to include multiple story templates for a more diverse experience.

## How to Run
### Prerequisites
- Python 3.6 or higher installed on your system.

### Steps
1. Clone the repository or download the script file.
   ```bash
   git clone https://github.com/bytesbyt/ds_katas.git
   ```
2. Navigate to the script directory:
   ```bash
   cd src
   ```
3. Run the program:
   ```bash
   python mad_libs_generator.py
   ```

### Example Gameplay
```text
Enter an adjective: funny
Enter a noun: dog
Enter the name of a country: Italy
Enter a type of building: castle
Enter an item that you like: diamond
Enter another item that you like: ruby
Enter an emotion: excited
Enter a verb ending with -ing: dancing
Enter the name of a famous person: Albert Einstein
Enter an animal: dragon

Your Mad Libs story:

Once upon a time there was a funny dog. One day, the dog went to Italy and discovered a hidden castle with one diamond and one ruby.
Upon seeing the diamond and the ruby, the dog felt excited and started dancing.
Albert Einstein then walked in and saw the dog dancing, and told the dog that if they decided to stay in the castle, they could keep the diamond and the ruby but would need to fight against a dragon.
If the dog decided to leave then they would go back to Italy and never see a ruby again.
Since the dog didn't want to fight against a dragon, the dog decided to give up the ruby and return to Italy with a diamond.
```

## Code Structure
1. **`get_user_input(prompts)`**:
   - Collects user responses based on predefined prompts.
   - Ensures inputs are non-empty.
2. **`generate_story(responses)`**:
   - Takes the user inputs and generates a Mad Libs story by placing them into a predefined story template.
3. **`main()`**:
   - Controls the program flow by defining prompts, gathering inputs, generating the story, and printing the result.
4. **`if __name__ == "__main__":`**:
   - Ensures the script runs as a standalone program when executed directly.




# Text Based Adventure Game

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

