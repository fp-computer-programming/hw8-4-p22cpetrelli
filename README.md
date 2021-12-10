<h1 align="center">
    Fairfield College Preparatory School<br>
    Computer Programming - Mr. Mesquita<br>
    HW 8-4
</h1>

<h2 align="center">Due before 8:30 AM on 12/10 (10 pts.)</h2>

### Break and Continue
---
Answer each of the following questions in a separate Python file named `hw8-4-#.py` where `#` is the number of the question. In your heading, put your name and the date you began working on the file.

1. Write a program that plays a guessing game with the user. The computer should generate a random number from 0 - 50 inclusive. The user should be prompted to guess the number, and the computer should tell the user if they need to go higher, or lower, and when they guess the number, the program should end. The user should also be able to enter the string "stop" to quit the program without winning, and the computer should tell them what its number was. (5 pts.)

2. Modify the following program that plays rock, paper, scissors so that the user can choose to play another round after a round ends. This program should prompt the user to enter `Y` to play another round and `N` to stop playing after displaying if the user won or lost. When the user chooses to not play another round, the program should display how many times the user won, lost, or tied and how many games have been played. The program should start another round if the user inputs a value other than `0`, `1`, or `2` when playing a game and handle if the user inputs either a capital or lowercase `Y` or `N` when choosing whether to play another round. (5 pts.)

    ```python
    from random import randint


    def rock_paper_scissors():
        """Play rock paper scissors"""
        player = int(input("Enter 0 for rock, 1 for paper, and 2 for scissors: "))
        computer = randint(0, 2)

        # Check if the user or the computer won.
        if player == computer:
            print("It's a tie!")
            return "tie"
        elif player == 0:
            if computer == 1:
                print("You lose, paper covers rock.\n")
                return "loss"
            else:
                print("You win, rock crushes scissors!\n")
                return "win"
        elif player == 1:
            if computer == 2:
                print("You lose, scissors cuts paper.\n")
                return "loss"
            else:
                print("You win, paper covers rock!\n")
                return "win"
        elif player == 2:
            if computer == 0:
                print("You lose, rock crushes scissors.\n")
                return "loss"
            else:
                print("You win, scissors cuts paper!\n")
                return "win"
    ```

<p align="center">Be sure to commit your code before the deadline. Only the latest commit will be graded.</p>
