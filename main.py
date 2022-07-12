### (
## Importations

# import system from the operatin system
from os import system, name

# import sleep function from time
from time import sleep

def clear(): # clear screen function from geeksforgeeks

    # clear the screen on windows
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")

import random

### )

### (

## Variables
languages = ["english", "spanish"] 
units_list = ( ["1", "one", "uno"], ["2", "two", "dos"], ["3", "three", "tres"] )

# create a list containing all of the available unit-words for get_start_info()
units_text = []
for sublist in units_list:
    for item in sublist:
        units_text.append(item)
        
## Lists for Translation

# Unit 1: People and Adjectives
unit_1_english = ( ["boy"], ["girl"] , ["friend"] , ["happy"] , ["ugly"] , ["pretty"] , ["athletic"] , ["fun"] , ["tall"] , ["blonde"] , ["brunette"] , ["interesting"] , ["angry", "mad"] )
unit_1_spanish = ( ["muchacho"] , ["muchacha"] , ["amigo", "amiga"] , ["feliz"] , ["feo", "fea"] , ["bonito" ,"bonita"] , ["atlético", "atlética", "atletico", "atletica"] , ["divertido", "divertida"] , ["alto" , "alta"] , ["rubio", "rubia"] , ["moreno", "morena"] , ["interesante"] , ["enojado", "enojada"] )

# Unit 2: Calendar and Weather
unit_2_english = ( ["snow"] , ["weather"] , ["rain"] , ["monday"] , ["tuesday"] , ["wednesday"] , ["thursday"] , ["friday"] , ["saturday"] , ["sunday"] , ["january"] , ["february"] , ["march"] , ["april"] , ["may"] , ["june"] , ["july"] , ["august"] , ["september"] , ["october"] , ["november"] , ["december"] , ["summer"] , ["winter"] , ["spring"] , ["autumn", "fall"] , ["birthday"] , ["day"] )
unit_2_spanish = ( ["nieve"] , ["tiempo"] , ["llueve"] , ["lunes"] , ["martes"] , ["miércoles",  "miercoles"] , ["jueves"], ["viernes"], ["sábado", "sabado"] , ["domingo"] , ["enero"] , ["febrero"] , ["marzo"] , ["abril"] , ["mayo"] , ["junio"] , ["julio"] , ["agosto"] , ["septiembre"] , ["octubre"] , ["noviembre"] , ["diciembre"] , ["verano"] , ["invierno"] , ["primavera"] , ["otoño", "otono"] , ["cumpleaños", "cumpleanos"], ["día", "dia"] )

# Unit 3: Home and Travel
unit_3_english = ( ["living room"] , ["kitchen"] , ["bedroom"] , ["garage"] , ["country"] , ["airport"] , ["passport"] , ["bus"] , ["luggage"] , ["backpack"] )
unit_3_spanish = ( ["sala"] , ["cocina"] , ["dormitorio", "recámara", "recamara", "alcoba"] , ["garaje"] , ["campo"] , ["aeropuerto"] , ["pasaporte"] , ["autobús", "autobus"], ["equipaje"] , ["mochila"] )

# Compound lists containing the respective lists for each languages units
english_units = (unit_1_english, unit_2_english, unit_3_english)
spanish_units = (unit_1_spanish, unit_2_spanish, unit_3_spanish)

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
                print("Please choose one of the available units: 1, 2, or 3.")
        
        # packages the variables starting and unit into a list to be passed along
        return_list = [starting, unit]

        # lets user confirm the imput info and re-input if necessary
        can_move_on = confirm_start_info(return_list) # confirm_start_info() returns boolean

        if (can_move_on == True):
            return return_list
        else: 
            print("Please re-type your information!")
            print() # goes back to top of function and user re-does process
            
        
def confirm_start_info(returned_list):

    # unpackage the data from get_start_info()
    starting = returned_list[0] # the language the user wanted to start with
    unit = returned_list[1] # the unit the user wanted to start with

    yeses = ["y", "yes", "si"]
    nos = ["n", "no"]

    while True:
        confirmation_response = input("Are you sure you want to translate Unit: " + unit + " from " + starting.capitalize() + "? ")
        confirmation_response = confirmation_response.lower()
        if (confirmation_response in yeses):
            return True # get_start_info() will return this set of start language and unit
        elif (confirmation_response in nos):
            return False # get_start_info() will re-run asking user to re-input their start language and unit
        else:
            print("Please type either 'Y' or 'N'.")
            continue


def get_play_info(start_info):

    # unpackage data from start_info
    starting_language = start_info[0] 
    starting_unit = start_info[1]

    unit_index = None 

    
    # finds the unit index for the unit the user wants to study
    # to be used to get that unit from spanish/english_units
    counter = 0
    for sublist in units_list:
        counter += 1
        if starting_unit in sublist:
            unit_index = (counter - 1)
            break
    
    # returns the start and end lists used to play the game
    if (starting_language == "spanish"):
        start_list = spanish_units[unit_index]
        end_list = english_units[unit_index]
        return [start_list, end_list]
    elif (starting_language == "english"):
        start_list = english_units[unit_index]
        end_list = spanish_units[unit_index]
        return [start_list, end_list]
    else:
        return ("ERROR: Start and End lists not transmitted properly")
    

def play_game():
    start_info = get_start_info() # start info will equal the return_list containing the starting language and unit
    print(get_play_info(start_info))
    

### )

### (
## Run Program

play_game()

###)