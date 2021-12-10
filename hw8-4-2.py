# author CJP 12/9/21
from random import randint


def rock_paper_scissors(wins=0,losses=0,ties=0,games=0):
        """Play rock paper scissors"""
        player = int(input("Enter 0 for rock, 1 for paper, and 2 for scissors: "))
        computer = randint(0, 2)
        looped = False

        # Check if the user or the computer won.
        if not looped:
            if player == computer:
                print("It's a tie!")
                ties += 1
            elif player == 0:
                if computer == 1:
                    print("You lose, paper covers rock.\n")
                    losses += 1
                else:
                    print("You win, rock crushes scissors!\n")
                    wins += 1
            elif player == 1:
                if computer == 2:
                    print("You lose, scissors cuts paper.\n")
                    losses += 1
                else:
                    print("You win, paper covers rock!\n")
                    wins += 1
            elif player == 2:
                if computer == 0:
                    print("You lose, rock crushes scissors.\n")
                    losses += 1
                else:
                    print("You win, scissors cuts paper!\n")
                    wins += 1
            elif player >= 3:
                print("number not valid, new round starting\n")
                rock_paper_scissors()
        
        games += 1
        loss = True

        while loss:
            play_again = input("Do you want to play again?(Y/N): ")
            if play_again.lower() == "y":
                rock_paper_scissors(wins,losses,ties,games)
                loss = False
            elif play_again.lower() == "n":
                 print(" Number of wins:",wins,"\n Losses:",losses,"\n Ties:",ties,"\n Games Played:",games)
                 loss = False


rock_paper_scissors()