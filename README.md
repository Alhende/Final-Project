# The Museum of Things That Never Happened

## Project Description
This is a text-based adventure game written in Python.
The player explores a mysterious museum, interacts with
characters, collects items, and makes choices that lead
to different endings.

## Game Objectives
- Explore the three museum exhibits.
- Interact with NPCs to discover hidden secrets.
- Collect inventory items to unlock different endings.
- Make choices that affect the player's journey.
- Discover the truth about the museum and choose
  your final fate.

## Core Game Features
- Three story paths
- Three different endings
- Five locations or major events
- Five NPC interactions
- Five inventory items
- Two interactive gameplay challenges
- Story branching using dictionaries and lists
- Input validation
- Inventory management system
- Timestamped audit logging
- Save and load game progress
- SHA-256 tamper detection
- Error handling for missing or modified save files

## Story Paths
1. Room of Unsent Letters: The player discovers a
   sealed letter and meets the Ghost Writer.
2. Hall of Missing Cities: The player meets the
   Map Keeper and discovers a hidden location.
3. Basement of Broken Clocks: The player meets the
   Clockmaker and learns about the broken clock.

## Story Endings
1. Escape the Museum: The player uses the Silver Key
   to escape.
2. Become the New Curator: The player collects the
   Sealed Letter and Missing City Map.
3. Destroy the Museum: The player collects the
   Broken Clock Hand and Memory Photograph.

## Locations and Major Events
1. Museum opening scene
2. Room of Unsent Letters
3. Hall of Missing Cities
4. Basement of Broken Clocks
5. Final Exhibition

## NPC Interactions
- Curator: Appears in the opening scene and introduces
  the museum.
- Ghost Writer: Appears in the Room of Unsent Letters
  and provides the Silver Key.
- Map Keeper: Appears in the Hall of Missing Cities
  and provides the Missing City Map.
- Clockmaker: Appears in the Basement of Broken Clocks
  and provides the Broken Clock Hand.
- Forgotten Visitor: Appears after visiting the three
  rooms and provides the Memory Photograph.

## Inventory Items
- Sealed Letter: Required for the New Curator ending.
- Silver Key: Required for the Escape ending.
- Missing City Map: Required for the New Curator ending.
- Broken Clock Hand: Required for the Destroy ending.
- Memory Photograph: Required for the Destroy ending.

## Team Members
- Sara Alhende
- Ariana Qasimzada

Both team members collaborated on story development,
Python programming, NPC interactions, inventory management,
story branching, game testing, and project documentation.

## How to Run the Game
1. Open the project folder in VS Code.
2. Open the terminal.
3. Run the following command:

```bash
python3 -m content.story
```

4. Follow the instructions displayed in the terminal.
5. Enter the numbers to explore rooms, interact with
   characters, collect items, and choose an ending.

## Gameplay Challenges

### Challenge 1: Missing Cities Puzzle
- Location: Hall of Missing Cities.
- The Map Keeper asks the player to solve a riddle.
- Success: The player receives the Missing City Map.
- Failure: The player does not receive the map but can return and try again.

### Challenge 2: Broken Clocks Puzzle
- Location: Basement of Broken Clocks.
- The Clockmaker asks the player to solve a time-based puzzle.
- Success: The player receives the Broken Clock Hand.
- Failure: The player does not receive the clock hand but can return and try again.

## Development Challenges

- Connecting the three story paths and NPC interactions.
- Managing inventory items and their requirements.
- Creating three different endings based on player choices.
- Handling invalid user input.
- Integrating Python files and resolving GitHub merge conflicts.
- Implementing and testing the save and load system.
- Testing all three endings and security features.

## Cyber Pack

### Input Validation
Invalid menu choices are handled safely, and players are prompted to enter a valid choice.

### Audit Logging
The game records important events in audit_log.txt with timestamps, event names, and results.

Recorded events include:
- Game start and end.
- Invalid user input.
- Challenge success and failure.
- Save and load success and failure.
- Detection of modified save files.

### Save and Load System
Players can save and load their inventory and story progress using options 5 and 6 in the room selection menu.

### Tamper Detection
The game uses SHA-256 hashing to check the integrity of saved game data. The save data is stored in save_game.txt, and its hash is stored in save_hash.txt.

If the saved data is modified without updating the original hash, the game displays a warning and rejects the modified save file.

## Testing

Sara and Ariana collaborated on developing and testing the game, including story paths, endings, NPC interactions, inventory management, gameplay challenges, and security features.