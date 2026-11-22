
# Story scenes for The Museum of Things That Never Happened

from systems.inventory import add_item, show_inventory

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
            print("\nYou give the letter to the Ghost Writer.")
            print("The Ghost Writer thanks you and reveals a hidden clue.")
            add_item("Silver Key")
            story_flags["has_clue"] = True


    elif choice == "2":
        story_flags["visited_cities"] = True
        print("\n" + story_paths["2"]["name"])
        print(story_paths["2"]["description"])
        print(story_paths["2"]["clue"])

        # Meet the Map Keeper
        print("\n" + cities_scene["description"])
        print(cities_scene["character"] + ": " + cities_scene["dialogue"])

        print("\nWhat would you like to do?")
        for index, city_choice in enumerate(cities_scene["choices"]):
            print(str(index + 1) + ". " + city_choice)

        while True:
            city_choice = input("Enter 1 or 2: ")

            if city_choice in ["1", "2"]:
                break
            else:
                print("Invalid choice. Please enter 1 or 2.")

        if city_choice == "1":
            print("\nYou carefully study the missing city map.")
            print("You discover a hidden passage marked beneath the city.")

            # Add the missing city map to the inventory
            add_item("Missing City Map")
            story_flags["has_clue"] = True
            story_flags["found_map"] = True

        elif city_choice == "2":
            print("\nYou ask the Map Keeper about the hidden city.")
            print("The Map Keeper reveals that the city disappeared from everyone's memory.")
            story_flags["has_clue"] = True

    elif choice == "3":
        story_flags["visited_clocks"] = True
        print("\n" + story_paths["3"]["name"])
        print(story_paths["3"]["description"])
        print(story_paths["3"]["clue"])

        # Meet the Clockmaker
        print("\n" + clocks_scene["description"])
        print(clocks_scene["character"] + ": " + clocks_scene["dialogue"])

        print("\nWhat would you like to do?")
        for index, clock_choice in enumerate(clocks_scene["choices"]):
            print(str(index + 1) + ". " + clock_choice)

        while True:
            clock_choice = input("Enter 1 or 2: ")

            if clock_choice in ["1", "2"]:
                break
            else:
                print("Invalid choice. Please enter 1 or 2.")

        if clock_choice == "1":
            print("\nYou examine the broken clock carefully.")
            print("You discover that its hands are pointing to 2:17 AM.")

            # Add the broken clock hand to the inventory
            add_item("Broken Clock Hand")
            story_flags["has_clue"] = True
            story_flags["found_clock_hand"] = True

        elif clock_choice == "2":
            print("\nYou ask the Clockmaker to repair the clock.")
            print("The Clockmaker warns you that fixing the clock may change the museum forever.")
            story_flags["has_clue"] = True

    return choice

# Run the story when this file is executed directly
if __name__ == "__main__":
    while True:
        opening_Scene()
