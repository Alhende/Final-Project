# NPC interactions for The Museum of Things That Never Happened

def forgotten_visitor_interaction():
    print("\nYou meet the Forgotten Visitor.")
    print("Forgotten Visitor: I remember you. You have been here before.")

    print("\nWhat would you like to ask?")
    print("1. How do you know me?")
    print("2. What is the Final Exhibition?")

    while True:
        choice = input("Enter 1 or 2: ")

        if choice == "1":
            print("\nYou: How do you know me?")
            print("\nForgotten Visitor: Your memories are hidden inside this museum.")
            print("You must find them before the Curator does.")
            return "memory_clue"

        elif choice == "2":
            print("\nForgotten Visitor: The Final Exhibition contains the truth about you.")
            print("You must collect the three missing pieces first.")
            return "final_exhibition_clue"

        else:
            print("Invalid choice. Please enter 1 or 2.")

def ghost_writer_interaction():
    print("\nYou meet the Ghost Writer.")
    print("Ghost Writer: Some letters contain secrets that were never meant to be discovered.")
    print("1. Ask about the sealed letter")
    print("2. Ask about the Curator")
    while True:
        choice = input("Enter 1 or 2: ")

        if choice == "1":
            print("Ghost Writer: The letter contains a memory the Curator wants to hide.")
            return "letter_clue"
        elif choice == "2":
            print("Ghost Writer: The Curator was once a visitor, just like you.")
            return "curator_clue"
        else:
            print("Invalid choice.")


def map_keeper_interaction():
    print("\nYou meet the Map Keeper.")
    print("Map Keeper: Every missing city has a secret.")
    print("1. Ask about the hidden city")
    print("2. Ask why the cities disappeared")
    while True:
        choice = input("Enter 1 or 2: ")

        if choice == "1":
            print("Map Keeper: Look beneath the oldest map to find the hidden entrance.")
            return "hidden_city_clue"
        elif choice == "2":
            print("Map Keeper: The Curator erased the cities to hide their memories.")
            return "missing_cities_clue"
        else:
            print("Invalid choice.")



def clockmaker_interaction():
    print("\nYou meet the Clockmaker.")
    print("Clockmaker: This museum is trapped at 2:17 AM.")
    print("1. Ask about the broken clock")
    print("2. Ask how to stop the clock")
    while True:
        choice = input("Enter 1 or 2: ")
        if choice == "1":
            print("Clockmaker: The clock stopped when the museum's first memory disappeared.")
            return "clock_clue"
        elif choice == "2":
            print("Clockmaker: You need to recover the missing memories to change time.")
            return "time_clue"
        else:
            print("Invalid choice.")



def curator_interaction():
    print("\nYou meet the Curator.")
    print("Curator: Welcome back. This museum has been waiting for you.")
    print("1. Ask why you are here")
    print("2. Ask about the museum")
    while True:
        choice = input("Enter 1 or 2: ")

        if choice == "1":
            print("Curator: You left something important behind.")
            return "player_memory_clue"
        elif choice == "2":
            print("Curator: Every exhibit holds a memory that someone wanted to forget.")
            return "museum_clue"
        else:
            print("Invalid choice.")
