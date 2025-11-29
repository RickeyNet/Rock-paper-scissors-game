import random


rock = '''
    _______
---'   ____)
    (_____)
    (_____)
    (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)__
        ______)
        _______)
        _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)__
        ______)
    __________)
    (____)
---.__(___)
'''
game_over = False
while not game_over:
    players_choice = int(input("Lets play rock, paper, scissors! type 0 for rock, 1 for paper, and 2 for scissors: \n"))
    print("Your choice is: ")
    if players_choice == 0:
        print(rock)
    elif players_choice == 1:
        print(paper)
    elif players_choice == 2:
        print(scissors)
    else:
        print("You did not choose one of the three options. Try again.")


    print("Robots choice is:")
    robots_choice = random.randint(0, 2)
    if robots_choice == 0:
        print(rock)
    elif robots_choice == 1:
        print(paper)
    elif robots_choice == 2:
        print(scissors)
    else:
        print("Robot has gone haywire.")

    if robots_choice == 0 and players_choice == 1:
        print("You beat me this time! Let's go again.")
    elif robots_choice == 0 and players_choice == 2:
        print("I won! Better luck next time. Let's go again.")
    elif robots_choice == players_choice:
        print("Nobody won this round. Let's go again.")
    elif robots_choice == 1 and players_choice == 2:
        print("You beat me this time. Let's go again.")
    elif robots_choice == 1 and players_choice == 0:
        print("I won! Better luck next time. Let's go again.")
    elif robots_choice == 2 and players_choice == 0:
        print("You beat me this time! Let's go again.")
    elif robots_choice == 2 and players_choice == 1:
        print("I won! Better luck next time. Let's go again.")
    else:
        print("Try again")

