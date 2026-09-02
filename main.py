from recipes import recipes
import subprocess
import platform

# Output Expectations #

# Final Product - Show number of buildings required, Power Required [Excluding Raw Material Extractors],
# Output of product
 
# Starting Process - Want it to ask "What recipe?", "What raw material inputs?" [Potentially give a list of
# raw materials required for that recipe, pick one, give a number.] Check for alternate recipes, ask if any 
# are wanted. NOTE: will need to ask for alt recipes before input numbers.

# Chronological Process:
# - User provides recipe
# - Grabs recipe
# - Checks for alternate recipes
# - [If true] Asks user which recipe
# - Checks materials for recipes
# - [If true] Checks for alternate recipes
# - [If true] Asks user which recipe
# - Mathematics for working out raw materials -> inputs
# - Prints out results NOTE: Need to figure out layout format for results.
# - Collate buildings, final product[s] and power into a total sum.

# Clears the terminal.
def clear():
    os = platform.system()
    if os == "Linux":
        subprocess.run("clear")
    elif os == "Windows":
        subprocess.run("cls")

# Checks if the base recipe has any alternate recipes.
def alt_check(input_recipe):
    for recipe in recipes:
        if recipe == input_recipe:
            return recipes[recipe]["alt"]

# Collates all alternate recipes for the inputted base recipe into a list.
def alt_recipes(input_recipe):
    output = recipes[input_recipe]["output material"]
    alternates = []
    for recipe in recipes:
        if output == recipes[recipe]["output material"]:
            alternates.append(recipe)
    return alternates

def main():
    while True:
        while True:
            recipe = input("What recipe would you like to produce?\n")
            if recipe not in recipes:
                print("Recipe does not exist")
            else:
                break
            
        clear()

        alt = alt_check(recipe)
        if alt == True:
            alternates = alt_recipes(recipe)
        while True:
            print("Which recipe would you like to use?")
            for item in alternates:
                print(f">> {item}")
            recipe_choice = input()
            if recipe_choice not in alternates:
                print("Recipe choice is invalid. Please choose from the list.")
            else:
                break

main()