#Game: Build a Kitty Cat Simulator

#Import all the modules 
import time
import random
import gametwo

#store the users name
user_name = input("Please enter your name: ")

#call game
gametwo.display_rules()

def welcome():
    print('Welcome to the build your cat simulator ' + user_name + '!')
    print('Keep in mind you only have $100 to customize your cat!')
    print('So use them wisely!! :3 ')
    print('----------------------------')
    print(' ')

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
        money -= 30  

def question_two():
    global money
    for i in range(1):  
        while True:
            try:
                # Ask user for their preference
                ans = input(f'Q2: Do you prefer brown eyes for $20 (1) or green eyes for $40 (2)? (1/2): ')
                print(' ')
                if ans.lower() not in ('1', '2'):
                    raise ValueError("Please enter '1' or '2' please. ")
                
                # Confirm user's choice
                confirm = input('Would you like to change your mind? (yes/no): ')
                print(' ')
                if confirm.lower() == 'no':
                    print("Okay, now moving on to the next question.")
                    break  # Exit the while loop to move to the next iteration
                elif confirm.lower() != 'yes':
                    raise ValueError("Please enter 'yes' or 'no'.")
                    
            except ValueError as e:
                print(e)
            print(' ')
#scoring the user response

        if ans.lower() == '1':
            print("You have spent $20!")
            print(' ')
            money -= 20 
        elif ans.lower() == '2':
            print("Yo uhave spent $40!")
            print(' ')
            money -= 40

def question_three():
    global money
    while True:
        try:
            ans = input(' Q3: Would you rather female ($10) or male ($10)? (f/m)?: ')
            if ans.lower() not in ('f', 'm'):
                raise ValueError(f"Please enter 'f' or 'm'. ")
            break
        except ValueError as e:
            print(e)

#Deduction the money from the initial $100 based on the user response
    if ans.lower() == 'f':
        print(f"Now you have a beautiful female cat!")
        print(' ')
        money -= 10  # decreases fund by 10
    elif ans.lower() == 'm':
        print(f"You now have a handsome male cat!")
        print(' ')
        money -= 10  

#Question 4 about a second cat 

def question_four_randomizer():
    global my_cat
    global money

    # List of cat options
    cat_options = [
        ("a playful Siamese", "very vocal and enjoys climbing"),
        ("a Maine Coon", "friendly and great with families"),
        ("a Russian Blue", "shy but very affectionate once familiar")
    ]

    # Randomly selects one cat option
    breed, personality = random.choice(cat_options)

    while True:
        try:
            ans = input(f'Would you like to adopt {breed} that is {personality}? (y/n):')
            print(' ')
            if ans.lower() not in ('y', 'n'):
                raise ValueError("Please enter 'y' or 'n'. ")
            if ans.lower() == 'y':
                my_cat = {'breed': breed, 'personality': personality}
                print("Congratulations on your new cats!")
            else:
                print("Well thats too bad! We will in a differnt home for him!")
            break
        except ValueError as e:
            print(e)
        print(' ')

def finalscreen():
    print('Hello, user :) This concludes the game. Thank you for playing!')
    time.sleep(2)
   
    print('Please, allow for a brief rolling of the credits!')
    time.sleep(2)
   
    print('Credits:')
    print(' ')
    print('Creative Director & Developer: Inaya Siddiqi')


welcome()
time.sleep(2)
question_one()
time.sleep(2)
print(' ')
print('You have', money,'dollars left in the bank')
print(' ')
time.sleep(3)
question_two()
time.sleep(2)
print(' ')
print('You have', money,'dollars left in the bank')
time.sleep(2)
question_three()
time.sleep(2)
print(' ')
print('You have', money,'dollars left in the bank')
time.sleep(2)
print('__________________________________________ ')
print('Its your lucky day we are having a buy one get one free sale, in addtion to your new cat, you also get ANOTHER randomized second cat!!!')
question_four_randomizer()
time.sleep(2)
finalscreen()

