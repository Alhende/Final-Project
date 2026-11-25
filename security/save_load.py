import json
import hashlib
from security.security import audit_log

# Save the player's game progress
def save_game(inventory, story_flags):
    try:
        game_data = {
            "inventory": inventory,
            "story_flags": story_flags
        }

        save_data = json.dumps(game_data)

        save_hash = hashlib.sha256(save_data.encode()).hexdigest()

        with open("save_game.txt", "w") as file:
            file.write(save_data)

        with open("save_hash.txt", "w") as file:
            file.write(save_hash)

        print("Game saved successfully.")
        audit_log("Save Game", "Success")

    except Exception:
        print("Unable to save the game.")
        audit_log("Save Game", "Failure")

# Load the player's saved progress
def load_game():
    try:
        with open("save_game.txt", "r") as file:
            save_data = file.read()

        with open("save_hash.txt", "r") as file:
            saved_hash = file.read()

        current_hash = hashlib.sha256(save_data.encode()).hexdigest()

        if current_hash != saved_hash:
            print("Warning: Save file has been modified.")
            audit_log("Load Game", "Failure - Tampering Detected")
            return None

        game_data = json.loads(save_data)

        print("Game loaded successfully.")
        audit_log("Load Game", "Success")

        return game_data

    except Exception:
        print("Unable to load the game.")
        audit_log("Load Game", "Failure")
        return None