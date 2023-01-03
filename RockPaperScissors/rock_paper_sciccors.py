import random


def play():
    user = input(
        "What's your choice? 'r' for rock, 'p' for paper, 's' for scissors \n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        print(f"you choose {user}, computer chooses {computer}")
        return 'it\'s a tie!'
    if is_win(user, computer):
        print(f"you choose {user}, computer chooses {computer}")
        return "you won!"

    print(f"you choose {user}, computer chooses {computer}")
    return "You lost!"


def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True


print(play())
