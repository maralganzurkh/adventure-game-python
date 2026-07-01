# Adventure Game — Python

**Python fundamentals project | SimpliLearn Microsoft AI Engineer Program**

A text-based adventure game built in Python demonstrating core programming concepts including variables, lists, functions, loops, and conditionals.

---

## What This Project Does

- Presents the player with a branching story set in an ancient quest
- Player chooses between two paths — a dark forest or a mysterious cave
- Each path has two further choices leading to a win or lose outcome
- Includes full replay capability without restarting the program

## Concepts Demonstrated

| Concept | Where Used |
|---|---|
| Functions | `start_game()`, `forest_path()`, `cave_path()`, `win_ending()`, `lose_ending()` |
| Conditionals | Path branching based on player choices |
| Loops | `ask_choice()` input validation loop, replay loop |
| Lists | Options passed to `ask_choice()` |
| Type hints | Function signatures use `str`, `list[str]` |

## How to Run

```bash
# 1. Clone the repo
git clone https://github.com/maralganzurkh/adventure-game-python

# 2. No dependencies needed — uses Python standard library only

# 3. Run
python adventure_game.py
```

## Example Gameplay

```
=== Welcome to the Ancient Quest ===
Adventurer, what is your name? > Maral

You arrive at a fork: a DARK FOREST to the left and a MYSTERIOUS CAVE to the right.
1. Forest
2. Cave
> 2

--- The Cave ---
1. Light a torch
2. Proceed in the dark
> 1

You strike a spark and the torch flares to life...
A golden relic sits atop a stone altar — the legendary treasure! ✨

Congratulations, Maral! You have found the treasure!
```
---

*Project completed as part of the Microsoft AI Engineer Program — SimpliLearn (2026)*  
*Author: Maral-Od Ganzurkh | [maralganzurkh.com](https://maralganzurkh.com)*
