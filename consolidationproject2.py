#Game: Build a Kitty Cat Simulator

#Import all the modules 
import time
import random
import gametwo

#store the users name
user_name = input("Please enter your name: ")

#this will generate a random number that shall b used later after some questions
random_number = random.randint(10, 100)

#call game
gametwo.display_rules()

def welcome():
    print('Welcome to the build your cat simulator ' + user_name + '!')
    print('----------------------------')
    print('Keep in mind you only have $50 to cusomize your cat!')
    print(' ')
    print('So use them wisely!! :3 ')

# Global money variable
money = 0
