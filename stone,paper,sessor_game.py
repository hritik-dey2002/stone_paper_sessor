import random



Playerscore = 0
Computerscore = 0



while True:
    choices = ["rock","paper","scissors"]

    computer = random.choice(choices)


    player = None



    while player not in choices:
        player = input("rock, paper, or scissors?: ").lower()

    if player == computer:
        print("computer: ",computer)
        print("player: ",player)
        print("Tie!")



    elif player == "rock":
        if computer == "paper":
            Computerscore = Computerscore + 1
            print("player: ", player)
            print("computer: ", computer)
            print("You lose!")
            print("Computer score :",(Computerscore))
            print("Player Score :",(Playerscore))
        if computer == "scissors":
            Playerscore = Playerscore + 1
            print("computer: ", computer)
            print("player: ", player)
            print("You win!")
            print("Computer score :", (Computerscore))
            print("Player Score :", (Playerscore))

    elif player == "scissors":
        if computer == "rock":
            Computerscore = Computerscore + 1
            print("computer: ", computer)
            print("player: ", player)
            print("You lose!")
            print("Computer score :", (Computerscore))
            print("Player Score :", (Playerscore))
        if computer == "paper":
            Playerscore = Playerscore + 1
            print("computer: ", computer)
            print("player: ", player)
            print("You win!")
            print("Computer Score :",(Computerscore))
            print("Player Score :", (Playerscore))

    elif player == "paper":
        if computer == "scissors":
            Computerscore = Computerscore + 1
            print("computer: ", computer)
            print("player: ", player)
            print("You lose!")
            print("Computer Score :", (Computerscore))
            print("Player Score :", (Playerscore))
        if computer == "rock":
            Playerscore = Playerscore + 1
            print("computer: ", computer)
            print("player: ", player)
            print("You win!")
            print("Computer Score :", (Computerscore))
            print("Player Score :", (Playerscore))

    play_again = input("Play again? (yes/no): ").lower()

    if play_again != "yes":
        break

print("Bye!")
