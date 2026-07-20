#!/usr/bin/env python3
# rock_paper_scissors.py

from random import randrange


def get_user_weapon():
    print("\nSELECT YOUR WEAPON (1-3)")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

    user_choice = int(input("Enter your Weapon : "))
    return user_choice


def get_opponent_weapon():
    opponent_choice = randrange(1, 4)
    return opponent_choice


def determine_winner(user_weapon, opponent_weapon):
    weapons = {1: "Rock", 2: "Paper", 3: "Scissors"}

    if user_weapon == opponent_weapon:
        print("It's a tie!.")

    elif user_weapon == 1 and opponent_weapon == 3:
        print("Rock beats Scissors. You win!")
    elif user_weapon == 3 and opponent_weapon == 2:
        print("Scissors beats Paper. You win!")
    elif user_weapon == 2 and opponent_weapon == 1:
        print("Paper beats Rock. You win!")

    elif user_weapon == 1 and opponent_weapon == 2:
        print("Paper beats Rock. You lose!")
    elif user_weapon == 3 and opponent_weapon == 1:
        print("Rock beats Scissors. You lose!")
    elif user_weapon == 2 and opponent_weapon == 3:
        print("Scissors beats Paper. You lose!")


def main():
    play_again = "y"

    while play_again.lower() == "y":
        user_weapon = get_user_weapon()
        opponent_weapon = get_opponent_weapon()

        determine_winner(user_weapon, opponent_weapon)

        play_again = input("\nWould you like to play again? (y/n): ")

    print("\nCompleted by, Peyton Tharp")


if __name__ == "__main__":
    main()
