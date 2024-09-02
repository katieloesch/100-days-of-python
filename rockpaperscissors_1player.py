from random import randint

print("Rock...")
print("Paper...")
print("Scissors...")


random_int = randint(0, 2)

if random_int == 0:
    computer = "rock"
elif random_int == 1:
    computer = "paper"
else:
    computer = "scissors"

player = input("Player make your move: ").lower()

print(f"> Player chose {player}")
print(f"> Computer chose {computer}")


def msg_player_wins():
    print("\n*** Player wins! ***")


def msg_computer_wins():
    print("\n*** Computer wins! ***")


def msg_tie():
    print("\n*** It's a tie! ***")


if player == computer:
    msg_tie()
elif player == "rock":
    if computer == "scissors":
        msg_player_wins()
    else:
        msg_computer_wins()
elif player == "paper":
    if computer == "rock":
        msg_player_wins()
    else:
        msg_computer_wins()
elif player == "scissors":
    if computer == "paper":
        msg_player_wins()
    else:
        msg_computer_wins()
else:
    print("something went wrong")
