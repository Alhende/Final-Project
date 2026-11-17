# Story scenes for The Museum of Things That Never Happened


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
    "has_clue": False
}


# Opening scene function
def opening_Scene():

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

    # Display the available story paths
    print("\nWhere would you like to go?")
    for index, choice in enumerate(opening_scene["choices"]):
        print(str(index + 1) + ". " + choice)

    # Validate the player's choice
    while True:
        choice = input("Enter 1, 2, or 3: ")

        if choice in ["1", "2", "3"]:
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

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
            print("The letter reveals that the Curator is hiding a secret.")

        elif letter_choice == "2":
            print("\nYou give the letter to the Ghost Writer.")
            print("The Ghost Writer thanks you and reveals a hidden clue.")

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

        elif city_choice == "2":
            print("\nYou ask the Map Keeper about the hidden city.")
            print("The Map Keeper reveals that the city disappeared from everyone's memory.")

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

        elif clock_choice == "2":
            print("\nYou ask the Clockmaker to repair the clock.")
            print("The Clockmaker warns you that fixing the clock may change the museum forever.")

    story_flags["has_clue"] = True

    return choice


# Run the game
opening_Scene()



