import requests
import json
import re

#url with all drinks
all_info = (requests.get("https://www.thecocktaildb.com/api/json/v1/1/filter.php?c=Cocktail")).json()

#prints text from all_info
def jprint(obj):
    # create a formatted string of the Python JSON object
    textDrinks = json.dumps(obj, sort_keys=True, indent=4)
    print(textDrinks)
jprint(all_info)

print("input name of drink")

#input and search for drink
x=input()

if x in '':
    x_no_space = re.sub('','%',x)

searchDrink = (requests.get("https://www.thecocktaildb.com/api/json/v1/1/search.php?s=" + x)).json()

#info about drink
searchedDrink = searchDrink["drinks"]
for drink in searchedDrink:
    print(drink["idDrink"])
    print(drink["strDrink"])
    print(drink["strInstructions"])
    print(drink["strAlcoholic"])
    print(drink["strGlass"])
    print(drink["strDrinkThumb"])

#Do you want a list of all drinks ->yes:list no: do you want to search by ingredient ->no: do you want to search by name? -> yes: input name no: Then we can't help 
                                                                                    # yes: input ingredient -> list: input drink you want -> list 