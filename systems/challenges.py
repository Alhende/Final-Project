from security.security import audit_log
# Challenge 1: Missing Cities Puzzle
def missing_cities_puzzle():
    print("\nMISSING CITIES PUZZLE")
    print("Map Keeper: Solve this riddle to receive the map.")
    print("What has cities, roads, and rivers, but no people?")

    answer = input("Enter your answer: ").strip().lower()

    if answer == "map" or answer == "a map":
        print("Correct! You unlocked the Missing City Map.")
        audit_log("Missing Cities Puzzle", "Success")
        return True
    else:
        print("Incorrect. Return later to try again.")
        audit_log("Missing Cities Puzzle", "Failure")
        return False


# Challenge 2: Broken Clocks Puzzle
def broken_clocks_puzzle():
    print("\nBROKEN CLOCKS PUZZLE")
    print("Clockmaker: Solve this puzzle to receive the clock hand.")
    print("The museum is frozen at 2:17 AM.")
    print("What time will it be one minute later?")

    answer = input("Enter your answer: ").strip().lower()

    if answer == "2:18" or answer == "2:18 am":
        print("Correct! You unlocked the Broken Clock Hand.")
        audit_log("Broken Clocks Puzzle", "Success")
        return True
    else:
        print("Incorrect. Return later to try again.")
        audit_log("Broken Clocks Puzzle", "Failure")
        return False