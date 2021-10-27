import requests
import json
import re

def Initial(): 
    print("Do you want a list of all drinks?")
    initial_input = input()
    initial_input_lowerCase = initial_input.lower()
    
    if initial_input_lowerCase == "yes":
        print("Alright")
        yes_list_of_drinks()
    elif initial_input_lowerCase == "no":
        print("Very well")
        no_search_by_ingredient()
    elif initial_input_lowerCase == "stop":
        stop_conversation()
    else:
        print("please answer yes or no!")
        initial_input_lowerCase = input()

def yes_list_of_drinks():
    all_drinks = (requests.get("https://www.thecocktaildb.com/api/json/v1/1/filter.php?c=Cocktail")).json()
    list_drinks = all_drinks["drinks"]
    for drink in list_drinks:
        print(drink["strDrink"])
        print(drink["strDrinkThumb"])
    specific_drink()

def specific_drink():
    print("Which drink do you want?")
    choose_specific_drink = input()
    choose_specific_drink_lowerCase = choose_specific_drink.lower()

    if choose_specific_drink_lowerCase in '':
        last_input_no_space = re.sub('','%',choose_specific_drink_lowerCase)

    search_drink = (requests.get("https://www.thecocktaildb.com/api/json/v1/1/search.php?s=" + choose_specific_drink_lowerCase)).json()
    
    searched_drink = search_drink["drinks"]
    for drink in searched_drink:
        print(drink["idDrink"])
        print(drink["strDrink"])
        print(drink["strInstructions"])
        print(drink["strAlcoholic"])
        print(drink["strGlass"])
        print(drink["strDrinkThumb"])
    
    stop_conversation()

def no_search_by_ingredient():
    print("Do you want to search by ingredients?")
    ingredient_input = input()
    ingredient_input_lowerCase = ingredient_input.lower()

    if ingredient_input_lowerCase == "yes":
        print("Alright, write ingredient")
        ingredient_input_lowerCase = input()
        search_ingredient = (requests.get("https://www.thecocktaildb.com/api/json/v1/1/filter.php?i=" + ingredient_input_lowerCase)).json()

        searched_ingredient = search_ingredient["drinks"]
        for ingredient in searched_ingredient:
            print(ingredient["strDrink"])
            print(ingredient["strDrinkThumb"])
        specific_drink()

    elif ingredient_input_lowerCase == "no":
        no_search_by_name()

    else:
        print("please answer yes or no!")
        ingredient_input_lowerCase = input()

def no_search_by_name():
    print("Do you want to search by name?")
    name_input = input()
    name_input_lowerCase = name_input.lower()

    if name_input_lowerCase == "yes":
        print("alright")
        specific_drink()
    elif name_input_lowerCase == "no":
        print("Then we can't help you")

    else:
        print("please answer yes or no!")
        name_input_lowerCase = input() 

def stop_conversation():
    print("do you want to go back to the beginning?")
    stop_input = input()
    stop_input_lowerCase = stop_input.lower()
    if stop_input_lowerCase == "yes":
        Initial()
    elif stop_input_lowerCase == "no":
        print("alright. See you later")
    else:
        print("please make a valid choice")


Initial()
#specific_drink()
#stop_conversation()

#Invalid input - drinks findes ikke
#if stop then stop conversation
#Stavemåder - capslock - stort eller småt 