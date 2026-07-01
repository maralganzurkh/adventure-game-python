#!/usr/bin/env python3
"""
adventure_game.py
A simple text-based adventure game demonstrating variables, lists, loops,
conditionals, and functions. The player chooses paths in a forest or cave to
find a legendary treasure. Includes replay capability.
"""

import sys
from typing import Callable


def ask_choice(prompt: str, options: list[str]) -> str:
    """
    Ask the player to choose one of the given options (case-insensitive).
    Returns the normalized (lowercase) selection.
    """
    normalized = [o.lower() for o in options]
    while True:
        print(prompt)
        for idx, o in enumerate(options, start=1):
            print(f"  {idx}. {o}")
        choice = input("> ").strip().lower()
        # allow number or text
        if choice.isdigit():
            i = int(choice) - 1
            if 0 <= i < len(options):
                return normalized[i]
        if choice in normalized:
            return choice
        print("Please choose a valid option.\n")


def start_game() -> None:
    """
    Display intro, ask for the player's name, and route to the first decision.
    Returns when the player reaches an ending (win/lose).
    """
    print("\n=== Welcome to the Ancient Quest ===")
    print("You are an explorer in search of a legendary treasure hidden in an ancient land.\n")

    name = input("Adventurer, what is your name? > ").strip() or "Explorer"
    print(f"\nGreetings, {name}! Your journey begins now...\n")

    path = ask_choice(
        "You arrive at a fork: a DARK FOREST to the left and a MYSTERIOUS CAVE to the right. Where do you go?",
        ["Forest", "Cave"]
    )

    if path == "forest":
        forest_path(name)
    else:
        cave_path(name)


def forest_path(name: str) -> None:
    """
    The forest scenario: player can follow a river or climb a tree.
    Outcomes differ based on the player's decision.
    """
    print("\n--- The Forest ---")
    print("Tall trees block much of the sunlight. You hear water trickling in the distance.\n")

    choice = ask_choice(
        "What will you do?",
        ["Follow the river", "Climb a tree"]
    )

    if choice == "follow the river":
        print("\nYou follow the river downstream, pushing aside ferns and low branches.")
        print("The river opens into a clearing where you spot an ancient stone pedestal.")
        print("On it lies a small chest engraved with your initials.\n")
        print("You open the chest and discover the legendary treasure! ✨")
        win_ending(name)
    else:
        print("\nYou climb a towering tree to get a better view.")
        print("Halfway up, the bark crumbles under your grip and you slip!")
        print("You catch yourself, but drop your map into the underbrush...")
        print("Without the map, you wander in circles until nightfall.\n")
        lose_ending(name, reason="You became lost in the forest.")


def cave_path(name: str) -> None:
    """
    The cave scenario: player can light a torch or proceed in the dark.
    Outcomes differ based on the player's decision.
    """
    print("\n--- The Cave ---")
    print("The cave mouth exhales a cold draft. Your footsteps echo into the darkness.\n")

    choice = ask_choice(
        "How will you proceed?",
        ["Light a torch", "Proceed in the dark"]
    )

    if choice == "light a torch":
        print("\nYou strike a spark and the torch flares to life.")
        print("Shadows dance on the walls, revealing ancient carvings that form a map.")
        print("You follow the markings through narrow tunnels to a hidden chamber...")
        print("A golden relic sits atop a stone altar—the legendary treasure! ✨\n")
        win_ending(name)
    else:
        print("\nYou step forward into the pitch black...")
        print("A sudden drop! You fall into a shallow pit and twist your ankle.")
        print("The echoes of your call fade, and you cannot climb out.\n")
        lose_ending(name, reason="You fell into a pit in the dark.")


def win_ending(name: str) -> None:
    """Display the win message and offer a replay."""
    print(f"Congratulations, {name}! You have found the treasure and completed your quest!\n")
    replay_loop()


def lose_ending(name: str, reason: str = "Your quest failed.") -> None:
    """Display the loss message with a reason and offer a replay."""
    print(f"Alas, {name}, your quest ends here. {reason}")
    print("Better luck next time!\n")
    replay_loop()


def replay_loop() -> None:
    """Ask the player if they want to replay the game. Loop until a valid answer is given."""
    again = ask_choice("Would you like to play again?", ["Yes", "No"])
    if again == "yes":
        start_game()
    else:
        print("\nThank you for playing. Farewell, adventurer!\n")
        sys.exit(0)


def main() -> None:
    """Main entry point: run the game loop starting at start_game()."""
    start_game()


if __name__ == "__main__":
    main()
