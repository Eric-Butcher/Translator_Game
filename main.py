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
                print()
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
            
        
def confirm_start_info(returned_list): # helper function of get_start_info()

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
    

def run_game(returned_list):
    start_list = returned_list[0]
    end_list = returned_list[1]

    num_translated = 0
    num_translated_correctly = 0

    # creates a list of the index values for the unit being translated
    available_indexes_list = []
    counter = 0
    for spot in start_list:
        available_indexes_list.append(counter)
        counter += 1
    
    still_going = True
    while still_going:

        length_available_indexes_list = len(available_indexes_list)
        if (length_available_indexes_list <= 0):
            still_going = False
            return [num_translated, num_translated_correctly]
    
        # get one of the available values from available_indexes_list to be used as an index to call to start/end_list
        # remove that value from available_indexes_list so that the same term is not presented more than once
        random_index = random.randint(0, (length_available_indexes_list - 1) ) # gets the random index in available_indexes_list
        prompt_index = available_indexes_list.pop(random_index) # returns the value at that random index, and removes it from the list

        presented_choices = start_list[prompt_index] # the list of available words the user may translate from
        translated_choices = end_list[prompt_index] # the available translations for that word

        was_correct = translate_prompt( [presented_choices, translated_choices] )
        
        num_translated += 1
        if (was_correct == True):
            num_translated_correctly += 1
        
        pause(1)




def translate_prompt(choices_lists):

    clear()
    

    presented_choices = choices_lists[0]
    translated_choices = choices_lists[1]

    word_to_present = random.choice(presented_choices)
    print("Term: " + word_to_present)
    user_translation = input("Translation: " )
    if user_translation in translated_choices:
        print("Correct!")
        return True
    else:
        print("Incorrect!")
        return False


def show_results(results):
    num_translated = results[0]
    num_translated_correctly = results[1]

    clear()

    print("You translated " + str(num_translated_correctly) + " correctly out of " + str(num_translated) + ".")
    accuracy = round(((num_translated / num_translated_correctly) * 100.0))
    print("Your accuracy was: " + str(accuracy) + "%")


def pause(s):
    sleep(s)
    

def play_game():
    clear()
    start_info = get_start_info() # start info will equal the return_list containing the starting language and unit
    play_info = get_play_info(start_info)
    results = run_game(play_info)
    show_results(results)

    

### )

### (
## Run Program

play_game()

###)