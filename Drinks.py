import requests
import json
import re

def Initial(): 
    print("Do you want a list of all drinks?")
    initial_input = input()
    if initial_input == "yes" or initial_input == "Yes":
        print("Alright")
        yes_list_of_drinks()
    elif initial_input == "no":
        print("Very well")
        no_search_by_ingredient()
    else:
        print("please answer yes or no!")
        initial_input = input()

def yes_list_of_drinks():
    all_drinks = (requests.get("https://www.thecocktaildb.com/api/json/v1/1/filter.php?c=Cocktail")).json()
    list_drinks = all_drinks["drinks"]
    for drink in list_drinks:
        print(drink["strDrink"])
        print(drink["strDrinkThumb"])

def specific_drink():
    print("Which drink do you want?")
    last_input = input()

    if last_input in '':
        last_input_no_space = re.sub('','%',last_input)

    search_drink = (requests.get("https://www.thecocktaildb.com/api/json/v1/1/search.php?s=" + last_input)).json()

    searched_drink = search_drink["drinks"]
    for drink in searched_drink:
        print(drink["idDrink"])
        print(drink["strDrink"])
        print(drink["strInstructions"])
        print(drink["strAlcoholic"])
        print(drink["strGlass"])
        print(drink["strDrinkThumb"])

def no_search_by_ingredient():
    print("Do you want to search by ingredients?")
    ingredient_input = input()
    if ingredient_input == "yes" or ingredient_input == "Yes":
        print("Alright, write ingredient")
        ingredient_input = input()
        search_ingredient = (requests.get("https://www.thecocktaildb.com/api/json/v1/1/filter.php?i=" + ingredient_input)).json()

        searched_ingredient = search_ingredient["drinks"]
        for ingredient in searched_ingredient:
            print(ingredient["strDrink"])
            print(ingredient["strDrinkThumb"])

    elif ingredient_input == "no":
        no_search_by_name()

    else:
        print("please answer yes or no!")
        ingredient_input = input()

def no_search_by_name():
    print("Do you want to search by name?")
    name_input = input()
    if name_input == "yes":
        print("alright")
    elif name_input == "no":
        print("Then we can't help you")

    else:
        print("please answer yes or no!")
        name_input = input() 

def stop_conversation():
    print("do you want to go back to the beginning?")
    stop_input = input()
    if stop_input == "yes":
        Initial()
    elif stop_input == "no":
        print("alright. See you later")
    else:
        print("please make a valid choice")


Initial()
specific_drink()
stop_conversation()

#Invalid input - drinks findes ikke
#if stop then stop conversation
#Stavemåder - capslock - stort eller småt