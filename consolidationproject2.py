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
    print('Keep in mind you only have $100 to customize your cat!')
    print(' ')
    print('So use them wisely!! :3 ')

# Global money variable
money = 100

#first question!
def question_one():
    global money
    while True:
        try:
            ans = input(' Q1: Would you rather pay $50 for a long hair cat (1) or $30 for a short haired (2) ? Type 1 or 2 to pick: ')
            if ans.lower() not in ('1', '2'):
                raise ValueError(f"Please enter '1' or '2'. ")
            break
        except ValueError as e:
            print(e)

#Deduction the money from the initial $100 based on the user response
    if ans.lower() == '1':
        print(f"Now you have a beautiful fluffy cat!")
        print(' ')
        money -= 50  # decreases fund by 50
    elif ans.lower() == '2':
        print(f"You now have a beautiful short haired cat!")
        print(' ')
        money -= 30  # increases the score for making an ethical choice


welcome()
question_one()
print(' ')
print('You have', money,'dollars left in the bank')
