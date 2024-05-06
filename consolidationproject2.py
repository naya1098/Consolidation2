#Game: Build a Kitty Cat Simulator

#Import all the modules 
import time
import random
import gametwo #Module I wrote

#store the users name
user_name = input("Please enter your name: ")

#call gametwo
gametwo.display_rules()

#welcome the user and lay out some more rules
def welcome():
    """
    This function displays the welcome message to the user and introduces the game and the $100 budget constraint.
    """
    print('Welcome to the build your cat simulator ' + user_name + '!')
    print('Keep in mind you only have $100 to customize your cat!')
    print('So use them wisely!! :3 ')
    print('----------------------------')
    print(' ')

# Global money variable
money = 100

#first question that requires user input
#asks user their preference on cat hair length
def question_one():
    """
    This makes the user to choose between a long-haired cat for $50 or a short-haired cat for $30.
    Then deducts the chosen amount from the global 'money' variable.
    """
    global money
    while True:
        try:
            ans = input(' Q1: Would you rather pay $50 for a long hair cat (1) or $30 for a short haired (2) ? Type 1 or 2 to pick: ')
            if ans.lower() not in ('1', '2'):
                raise ValueError(f"Please enter '1' or '2'. ") #redirect user to input either 1 or 2
            break
        except ValueError as e:
            print(e)

#Deducts money from the initial $100 based on the user response
    if ans.lower() == '1':
        print(f"Now you have a beautiful fluffy cat!")
        print(' ')
        money -= 50  # decreases fund by 50
    elif ans.lower() == '2':
        print(f"You now have a beautiful short haired cat!")
        print(' ')
        money -= 30   # decreases fund by 30

def question_two():
    """
    This function asks the user to choose between brown eyes for $20 or green eyes for $40 for their cat.
    This one then asks the user to confirm their choice before deducting the amount from the global 'money' variable.
    If the user keeps answering "yes" when they want to chnage their mind the question will keep looping until user inputs "no".
    """
    global money
    for i in range(1):  
        while True:
            try:
                # Ask user for their preference
                ans = input(f'Q2: Do you prefer brown eyes for $20 (1) or green eyes for $40 (2)? (1/2): ')
                print(' ')
                if ans.lower() not in ('1', '2'):
                    raise ValueError("Please enter '1' or '2' please. ") #redirect user to input either 1 or 2
                
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
#calculating the user response

        if ans.lower() == '1':
            print("You have spent $20!") 
            print(' ')
            money -= 20 # decreases fund by 20
        elif ans.lower() == '2':
            print("Yo uhave spent $40!")
            print(' ')
            money -= 40 # decreases fund by 10

def question_three():
    """
    Question 3 makes the user to choose the sex of the cat for a fixed price of $10.
    Either way it deducts $10 from the global 'money' variable based on the user's choice.
    """
    global money
    while True:
        try:
            ans = input(' Q3: Would you rather female ($10) or male ($10)? (f/m)?: ')
            if ans.lower() not in ('f', 'm'):
                raise ValueError(f"Please enter 'f' or 'm'. ") #redirect user to input either f or m
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
        money -= 10  # decreases fund by 10

#Question 4 about a randomized second cat 
def question_four_randomizer():
    """
    The last question in the game offers the user a chance to adopt a second cat from a randomized selection.
    The 'my_cat' global variable updates if the user decides to adopt.
    """
    global my_cat
    global money

    # List of cat options
    cat_options = [
        ("a playful Siamese", "very vocal and enjoys climbing"),
        ("a Maine Coon", "friendly and great with families"),
        ("a Russian Blue", "shy but very affectionate once familiar")
    ]

    # Randomly selects one cat option for the user to then choose or not choose
    breed, personality = random.choice(cat_options)

    while True:
        try:
            ans = input(f'Would you like to adopt {breed} that is {personality}? (y/n):')
            print(' ')
            if ans.lower() not in ('y', 'n'):
                raise ValueError("Please enter 'y' or 'n'. ") #redirect user to input either y or n
            if ans.lower() == 'y':
                my_cat = {'breed': breed, 'personality': personality}
                print("Congratulations on your new cats!")
            else:
                print("Well thats too bad! We will in a differnt home for him!")
            break
        except ValueError as e:
            print(e)
        print(' ')


#Displays credits and thank you message
def finalscreen():
    """
    Finally, this function displays the final screen with a thank you message and rolls the credits after a brief pause.
    """
    print('Hello, user :) This concludes the game. Thank you for playing!')
    time.sleep(2)
   
    print('Please, allow for a brief rolling of the credits!')
    time.sleep(2)
   
    print('Credits:')
    print(' ')
    print('Creative Director & Developer: Inaya Siddiqi')


welcome() #welcome + rules
time.sleep(2) # Waits for 2 seconds before moving to the 1st question
question_one() #asks user 1st question, gets answer and subtracts the money they owe from their choice from the base $100
time.sleep(2) # Waits for 2 seconds
print(' ')
print('You have', money,'dollars left in the bank') # Displays the new amt of $ left after users choice
print(' ')
time.sleep(3)# Waits for 3 seconds
question_two()#asks user 2nd question, gets answer and subtracts the money they owe from their choice from the base $100 - first choice
time.sleep(2) # Waits for 2 seconds
print(' ')
print('You have', money,'dollars left in the bank') # Displays the new amt of $ left after users choice
time.sleep(2)# Waits for 2 seconds
question_three() #asks user 1st question, gets answer and subtracts the money they owe from their choice from the base $100 -first choicce - secondd choice
time.sleep(2)# Waits for 2 seconds
print(' ')
print('You have', money,'dollars left in the bank') # Displays the new amt of $ left after users choice
time.sleep(2) # Waits for 3 seconds before moving on to the randomizer portion
print('__________________________________________ ')
print('Its your lucky day we are having a buy one get one free sale, in addtion to your new cat, you also get ANOTHER randomized second cat!!!')
question_four_randomizer()
time.sleep(2) # Waits for 2 seconds 
finalscreen() #Displays credits and thank you message

