import requests
import re

def Initial(): 
    print("Hallo, I am gonna help you find your drink today :) ") 
    print("If at any point during our conversation, you want to stop, just write 'stop', and i will see you the next time.")
    print("\nDo you want a list of all drinks?")
    
    initial_input = input()
    initial_input_lowerCase = initial_input.lower()
    
    if initial_input_lowerCase == "yes":
        print("\nAlright.")
        list_of_drinks()
    
    elif initial_input_lowerCase == "no":
        print("\nVery well.")
        search_by_ingredient()
    
    elif initial_input_lowerCase == "stop":
        stop_conversation()         
    
    else:
        print("please answer yes or no!")
        Initial()

def list_of_drinks():
    all_drinks = (requests.get("https://www.thecocktaildb.com/api/json/v1/1/filter.php?c=Cocktail")).json()
    list_drinks = all_drinks["drinks"]
    
    for drink in list_drinks:
        print("\n")
        print(drink["strDrink"])
        print(drink["strDrinkThumb"])
        
    specific_drink()

def search_by_ingredient():
    print("\nDo you want to search by ingredient?")
    
    ingredient_input = input()
    ingredient_input_lowerCase = ingredient_input.lower()
    
    if ingredient_input_lowerCase in '':
        ingredient_input_no_space = re.sub('','%',ingredient_input_lowerCase)          
    
    if ingredient_input_lowerCase == "yes":
        print("\nAlright, write an ingredient")
        
        ingredient_input_lowerCase = input()
        
        search_ingredient = (requests.get("https://www.thecocktaildb.com/api/json/v1/1/filter.php?i=" + ingredient_input_lowerCase)).json()
        searched_ingredient = search_ingredient["drinks"]
        
        for ingredient in searched_ingredient:
            print("\n")
            print(ingredient["strDrink"])
            print(ingredient["strDrinkThumb"])
            
        specific_drink()

    elif ingredient_input_lowerCase == "no":
        search_by_name()

    elif ingredient_input_lowerCase == "stop":
        stop_conversation()

    else:
        print("please answer yes or no!")
        search_by_ingredient() 

def search_by_name():
    print("\nDo you want to search by name?")
    
    name_input = input()
    name_input_lowerCase = name_input.lower()
    
    if name_input_lowerCase == "yes":
        print("\nAlright.")
        specific_drink()
    
    elif name_input_lowerCase == "no":
        print("\nThen we can't help you...")
        stop_conversation()
    
    elif name_input_lowerCase == "stop":
        stop_conversation()    
    
    else:
        print("please answer yes or no!")
        search_by_name()

def specific_drink():
    print("\nWhich drink do you want?")
  
    choose_specific_drink = input()
    choose_specific_drink_lowerCase = choose_specific_drink.lower() 
    
    if choose_specific_drink_lowerCase in '':
        choose_specific_drink_no_space = re.sub('','%',choose_specific_drink_lowerCase)

    if choose_specific_drink_lowerCase == "stop":
        stop_conversation()

    search_drink = (requests.get("https://www.thecocktaildb.com/api/json/v1/1/search.php?s=" + choose_specific_drink_lowerCase)).json()
    searched_drink = search_drink["drinks"]
    
    for drink in searched_drink:
        print("\n")
        print(drink["idDrink"])
        print(drink["strDrink"])
        print(drink["strInstructions"])
        print(drink["strAlcoholic"])
        print(drink["strGlass"])
        print(drink["strDrinkThumb"])
    
    stop_conversation()

def stop_conversation():
    print("\nDo you want to go back to the beginning?")
    
    stop_input = input()
    stop_input_lowerCase = stop_input.lower()
    
    if stop_input_lowerCase == "yes":
        Initial()
    
    elif stop_input_lowerCase == "no":
        print("\nAlright. See you later :) ")
    
    else:
        print("Please make a valid choice.")
        stop_conversation()

Initial()