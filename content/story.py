
# Story scenes for The Museum of Things That Never Happened

from systems.inventory import add_item, show_inventory, inventory
from content.npcs import map_keeper_interaction
from content.npcs import forgotten_visitor_interaction
from content.npcs import ghost_writer_interaction
from content.npcs import curator_interaction
from content.npcs import clockmaker_interaction
# Opening scene
opening_scene = {
    "title": "THE MUSEUM OF THINGS THAT NEVER HAPPENED",
    "location": "Main Museum Hall",
    "description": "You slowly open your eyes. The room is dark and silent.",
    "time": "2:17 AM",
    "character": "Curator",
    "choices": [
        "Room of Unsent Letters",
        "Hall of Missing Cities",
        "Basement of Broken Clocks"
    ]
}

# Story paths
story_paths = {
    "1": {
        "name": "Room of Unsent Letters",
        "description": "You enter a room filled with letters that were never delivered.",
        "clue": "A sealed letter contains a message about the museum."
    },
    "2": {
        "name": "Hall of Missing Cities",
        "description": "You enter a hallway showing maps of cities that disappeared.",
        "clue": "A missing city map reveals a hidden location."
    },
    "3": {
        "name": "Basement of Broken Clocks",
        "description": "You enter a basement filled with clocks frozen at different times.",
        "clue": "A broken clock hand may help you open a hidden passage."
    }
}


# Room of Unsent Letters
letters_scene = {
    "description": "You walk into a quiet room filled with hundreds of sealed letters.",
    "character": "Ghost Writer",
    "dialogue": "Some letters contain secrets that were never meant to be discovered.",
    "choices": [
        "Open the sealed letter",
        "Give the letter to the Ghost Writer"
    ]
}


# Hall of Missing Cities
cities_scene = {
    "description": "You enter a dark hallway covered with maps of cities that no longer exist.",
    "character": "Map Keeper",
    "dialogue": "Every missing city has a secret. Look carefully at the maps.",
    "choices": [
        "Study the missing city map",
        "Ask the Map Keeper about the hidden city"
    ]
}


# Basement of Broken Clocks
clocks_scene = {
    "description": "You enter a basement filled with clocks frozen at different times.",
    "character": "Clockmaker",
    "dialogue": "Time in this museum does not move like it does in the outside world.",
    "choices": [
        "Examine the broken clock",
        "Ask the Clockmaker to repair it"
    ]
}


# Story flags
story_flags = {
    "met_forgotten_visitor": False,
    "visited_letters": False,
    "visited_cities": False,
    "visited_clocks": False,
    "has_clue": False,
    "found_letter": False,
    "found_map": False,
    "found_clock_hand": False
}
intro_shown = False

# Opening scene function
def opening_Scene():
    global intro_shown

    if not intro_shown:

         # Display the opening scene
         print("=" * 50)
         print(opening_scene["title"])
         print("=" * 50)
         print(opening_scene["description"])
         print("The clock on the wall reads " + opening_scene["time"] + ".")
         print("You have no memory of how you arrived here.")
         print("Suddenly, you hear footsteps coming from behind you.")
         print("An old man wearing a black suit slowly approaches.")
         print(opening_scene["character"] + ": Welcome to the Museum. We have been expecting you.")
         print("Curator: There are three exhibits you may visit, but be careful.")
         print("Curator: Everything in this museum has a story.")
         curator_interaction()
         intro_shown = True
        # Display the available story paths
    print("\nWhere would you like to go?")
    for index, choice in enumerate(opening_scene["choices"]):
        print(str(index + 1) + ". " + choice)

    print("4. View inventory")

    # Validate the player's choice
    while True:
        choice = input("Enter 1, 2, 3, or 4: ")

        if choice in ["1", "2", "3"]:
            break

        elif choice == "4":
            show_inventory()

            print("\nWhere would you like to go?")
            for index, choice in enumerate(opening_scene["choices"]):
                print(str(index + 1) + ". " + choice)

            print("4. View inventory")

        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

    # Send the player to the selected story path
    if choice == "1":
        story_flags["visited_letters"] = True
        print("\n" + story_paths["1"]["name"])
        print(story_paths["1"]["description"])
        print(story_paths["1"]["clue"])

        # Meet the Ghost Writer
        print("\n" + letters_scene["description"])
        print(letters_scene["character"] + ": " + letters_scene["dialogue"])

        print("\nWhat would you like to do?")
        for index, letter_choice in enumerate(letters_scene["choices"]):
            print(str(index + 1) + ". " + letter_choice)

        while True:
            letter_choice = input("Enter 1 or 2: ")

            if letter_choice in ["1", "2"]:
                break
            else:
                print("Invalid choice. Please enter 1 or 2.")

        if letter_choice == "1":
            print("\nYou carefully open the sealed letter.")
            print("\nYou carefully unfold the letter and begin to read:")
            print("\nTO THE ONE WHO REMEMBERS")
            print("If you are reading this, then the Curator has failed to erase everything.")
            print("You were here before. You walked these halls and trusted the man in the black suit.")
            print("But you must not trust him again.")
            print("The museum collects memories, forgotten moments, and lives that never happened.")
            print("Find the three missing pieces before the clock reaches 2:18 AM.")
            print("Do not enter the Final Exhibition.")
            print("\nYou are not a visitor. You are the last exhibit.")
            print("\n- Someone who remembers you")
            # Add the sealed letter to the inventory
            add_item("Sealed Letter")
            story_flags["has_clue"] = True
            story_flags["found_letter"] = True

        elif letter_choice == "2":
            ghost_result = ghost_writer_interaction()

            if ghost_result == "letter_clue" or ghost_result == "curator_clue":
                add_item("Silver Key")
                story_flags["has_clue"] = True

    elif choice == "2":
        story_flags["visited_cities"] = True
        print("\n" + story_paths["2"]["name"])
        print(story_paths["2"]["description"])
        print(story_paths["2"]["clue"])

        # Meet the Map Keeper
        city_result = map_keeper_interaction()

        if city_result == "hidden_city_clue":
            add_item("Missing City Map")
            story_flags["has_clue"] = True
            story_flags["found_map"] = True
        elif city_result == "missing_cities_clue":
            story_flags["has_clue"] = True

    elif choice == "3":
        story_flags["visited_clocks"] = True
        clock_result = clockmaker_interaction()

        if clock_result == "clock_clue":
            add_item("Broken Clock Hand")
            story_flags["has_clue"] = True
            story_flags["found_clock_hand"] = True

        elif clock_result == "time_clue":
            story_flags["has_clue"] = True
# Three possible endings
def choose_ending():
    print("\nTHE FINAL EXHIBITION")
    print("You have discovered the museum's hidden memories.")
    print("\nChoose your fate:")
    print("1. Escape the Museum")
    print("2. Become the New Curator")
    print("3. Destroy the Museum")
    print("4. Return to exploring the museum")

    while True:
        choice = input("Enter 1, 2, 3, or 4: ")

        if choice == "1":
            if "Silver Key" in inventory:
                print("\nENDING 1: ESCAPE THE MUSEUM")
                print("You use the Silver Key to unlock the hidden exit.")
                print("You escape the museum and leave your forgotten memories behind.")
                return True
            else:
                print("\nYou need the Silver Key to escape the museum.")

        elif choice == "2":
            if "Sealed Letter" in inventory and "Missing City Map" in inventory:
                print("\nENDING 2: THE NEW CURATOR")
                print("You discover the truth about the Curator.")
                print("You take his place and become the guardian of the museum.")
                return True
            else:
                print("\nYou need the Sealed Letter and Missing City Map.")

        elif choice == "3":
            if "Broken Clock Hand" in inventory and "Memory Photograph" in inventory:
                print("\nENDING 3: THE MUSEUM DESTROYED")
                print("You use the memories you collected to destroy the museum.")
                print("As the museum collapses, you finally remember who you are.")
                return True
            else:
                print("\nYou need the Broken Clock Hand and Memory Photograph.")
        elif choice == "4":
            print("\nYou decide to continue exploring the museum.")
            return False
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")
# Run the story when this file is executed directly
if __name__ == "__main__":
    while True:
        opening_Scene()

        if (story_flags["visited_letters"] and
            story_flags["visited_cities"] and
            story_flags["visited_clocks"] and
            not story_flags["met_forgotten_visitor"]):

            visitor_result = forgotten_visitor_interaction()
            if visitor_result == "final_exhibition_clue":
                add_item("Memory Photograph")
                print("You received the Memory Photograph.")
                story_flags["met_forgotten_visitor"] = True
                

            elif visitor_result == "memory_clue":
                print("\nYou should continue exploring the museum.")
        if story_flags["met_forgotten_visitor"]:
            if choose_ending():
                break