# Story scenes for The Museum of Things That Never Happened

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

# Story flags
story_flags = {
    "visited_letters": False,
    "visited_cities": False,
    "visited_clocks": False,
    "has_clue": False
}


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

    elif choice == "2":
        story_flags["visited_cities"] = True
        print("\n" + story_paths["2"]["name"])
        print(story_paths["2"]["description"])
        print(story_paths["2"]["clue"])

    elif choice == "3":
        story_flags["visited_clocks"] = True
        print("\n" + story_paths["3"]["name"])
        print(story_paths["3"]["description"])
        print(story_paths["3"]["clue"])

    story_flags["has_clue"] = True

    return choice
# Run the game
opening_Scene()
