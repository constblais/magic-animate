"""Simple terminal guessing game.

Run with:
    python demo/number_guess_game.py
"""

from __future__ import annotations

import random


def play_game(max_number: int = 100, max_attempts: int = 7) -> None:
    """Run an interactive number guessing game in the terminal."""
    secret = random.randint(1, max_number)
    print("🎮 Welcome to Number Hunter!")
    print(f"I'm thinking of a number between 1 and {max_number}.")
    print(f"You have {max_attempts} attempts to guess it.\n")

    for attempt in range(1, max_attempts + 1):
        raw = input(f"Attempt {attempt}/{max_attempts}. Your guess: ").strip()

        if not raw.isdigit():
            print("Please enter a valid positive number.\n")
            continue

        guess = int(raw)

        if guess < secret:
            print("Too low!\n")
        elif guess > secret:
            print("Too high!\n")
        else:
            print(f"✅ You got it! The number was {secret}.")
            return

    print(f"❌ Out of attempts! The number was {secret}.")


if __name__ == "__main__":
    play_game()
