'''
Project Name: Rock paper scissor
Author: Sushant
'''
import random

def comp_turn():

    comp_move = random.randint(1,3)

    if comp_move == 1:
        return "Rock!"

    elif comp_move == 2:
        return "Paper!"

    else:
        return "Scissors!"

def main():

    num_games = int(input("Enter how many games you would like to play: "))

    print("You are going to play " + str(num_games) + " games! Here we go!")

    num_wins = 0

    for i in range(num_games):

        user_move = input("Choose either Rock, Paper or Scissors and enter it: ")

        cpu_turn = comp_turn()

        print("The computer went with: " + cpu_turn)

        if user_move == 'Rock' and cpu_turn == 'Scissors':
            print("You won! Nice job!")
            num_wins +=1

        elif user_move == 'Paper' and cpu_turn == 'Rock':
            print ("You won! Nice job!")
            num_wins +=1

        elif user_move == 'Scissors' and cpu_turn == 'Paper':
            print("You won! Nice job!")
            num_wins +=1

        elif user_move == cpu_turn:
            print ("Oh! You tied")

        else:
            print("Whoops! You lost!")
            return num_wins

print(main())
