'''
Project Name: Treasure Island
Author: Sushant
'''
print("Welcome to Treasure Island !!!")
print("Your mission is to find treasure.\n")
choice1 = input("You are at crossroad, where do you want to go? Type'left' or 'right'.\t").lower()

if choice1 == 'left':
    choice2 =input("You've come to a lake. There is an island in the middle of lake. Type 'wait' to wait for the boat or type 'swim' to swim across. \t").lower()
    if choice2 == 'wait':
        choice3 = input("You arrive safe at the island. There is a house with 3 doors, red, blue and green. Which color do you choose? \t").lower()
        if choice3 == "red":
            print("Room full of fire. Game Over")
        elif choice3 == "blue":
            print("You fell into tank full of sharks. Game Over")
        else:
            print("\nCongrats!!! YOU WIN!!!\n")
    else:
        print("You got attacked by shark. Game Over")
else:
    print("You fell into a hole.Game Over.")