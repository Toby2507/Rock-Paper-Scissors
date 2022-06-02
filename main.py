import random as rd


def winner(c, u):
    selections = c, u
    match selections:
        case ("R", "P") | ("P", "R"):
            return "P"
        case ("S", "P") | ("P", "S"):
            return "S"
        case ("R", "S") | ("S", "R"):
            return "R"


options = ["R", "P", "S"]
options_name = {"R": "Rock", "P": "Paper", "S": "Scissors"}
while True:
    while True:
        print("R for Rock\n"
              "P for Paper\n"
              "S for Scissors")
        user_input = input("R, P, S: ").upper()
        if user_input not in options:
            print("Invalid selection, please make another selection\n")
        else:
            break
    computer_input = rd.choice(options)
    print(f"Player ({options_name[user_input]}) : Computer ({options_name[computer_input]})")
    if user_input == computer_input:
        print("It's a Tie, please pick again\n")
    else:
        killed = winner(computer_input, user_input)
        if killed == computer_input:
            print("Computer won :)")
        else:
            print("You won :(")
        break
