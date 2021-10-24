import requests
import json
import re

def no_search_by_ingredient():
    print("Do you want to search by ingredients?")
    x = input()

    if x in '':
        x_no_space = re.sub('','%',x)

    searchDrink = (requests.get("https://www.thecocktaildb.com/api/json/v1/1/filter.php?i=" + x)).json()

    searchedDrink = searchDrink["drinks"]
    for drink in searchedDrink:
        
        print(drink["strDrink"])
        

no_search_by_ingredient()