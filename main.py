### (
## Importations

# import system from the operatin system
from os import system, name

# import sleep function from time
from time import sleep

def clear():

    # clear the screen on windows
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")



### )

### (
## Lists for Translation

# Variables
languages = ["english", "spanish"]
units_num = [1]
units_text = ["1", "one"]

# Unit 1
unit_1_english = []
unit_1_spanish = []

### )

### (
## Functions





def get_start_info():

    can_move_on = False

    # empty variables
    starting = ""
    unit = "" 
    
    print("The available languages are: English, Spanish.") 
    print()

    while (can_move_on == False):

        # grabbing the language the user wants to start with
        while True:
            choice = input("What language would you like to translate from? ")
            if choice.lower() in languages:
                starting = choice.lower()
                if starting == "spanish":
                    ending = "english"
                else:
                    ending = "spanish"
                print("You are translating from " + starting.capitalize() + " to " + ending.capitalize() + ".")
                break
            else:
                print("Please chosoe either English or Spanish!")
                continue
        
        # grabbing the unit the user wants to study
        while True:
            choice = input("What unit would you like to study? ")
            if (choice.lower() in units_text):
                unit = choice.lower()
                break
            else:
                print("Please choose one of the available units: 1.")
        
        # packages the variables starting and unit into a list to be passed along
        return_list = [starting, unit]
        can_move_on = confirm_start_info(return_list)

        if (can_move_on == True):
            #print("INFORMATION PASSED ON!!!")
            return "INFORMATION PASSED ON!!"
        else: # (can_move_on == False)
            print("Please re-type your information!")
            print() # goes back to top of function and user re-does process
            
        


def confirm_start_info(ret):
    starting = ret[0]
    unit = ret[1]

    yeses = ["y", "yes"]
    nos = ["n", "no"]

    while True:
        confirmation_response = input("Are you sure you want to translate Unit: " + unit + " from " + starting.capitalize() + "? ")
        confirmation_response = confirmation_response.lower()
        if (confirmation_response in yeses):
            return True
        elif (confirmation_response in nos):
            return False
        else:
            print("Please type either 'Y' or 'N'.")
            continue
        




def play_game():
    start_info = get_start_info()
    
    

### )

### (
## Run Program

play_game()

###)