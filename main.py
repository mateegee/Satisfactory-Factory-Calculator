from recipes import recipes, raw_inputs
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
            return recipes[recipe]["alts"]

# Collates all alternate recipes for the inputted base recipe into a list.
def output_alt_recipes(input_recipe):
    output = recipes[input_recipe]["output material"]
    alternates = []
    for recipe in recipes:
        if output == recipes[recipe]["output material"]:
            alternates.append(recipe)
    return alternates

# Collates all alternate recipes for materials of a recipe. Might be irrelevent, may delete.
def material_alt_recipes(input_recipe):
    materials = recipes[input_recipe]["materials"]
    materials_list = []
    for recipe in recipes:
        for material in materials:
            if material == recipes[recipe]["output material"]:
                materials_list.append(recipe)
    return materials_list

def main():
    while True:
        # This block makes the user select the recipe they wish to produce.
        while True: 
            product_recipe = input("What recipe would you like to produce?\n").title()
            if product_recipe not in recipes:
                print("\nRecipe does not exist")
            else:
                break
            
        clear()
        chosen_recipes = []

        # This block makes the user select any alternate recipes they wish to use in their production line.
        while True: 
            alt_recipe = input(f"Which alternate recipes would you like to use? If there are no more recipes, press Enter.\n Current recipes: {chosen_recipes}\n").title()
            clear()
            if alt_recipe == "":
                clear()
                break
            elif alt_recipe not in recipes:
                clear()
                print("Recipe does not exist.")
                continue
            elif recipes[alt_recipe]["is alt"] == False:
                clear()
                print("Recipe is not an alternate recipe.")
            else:
                chosen_recipes.append(alt_recipe)

        raw_materials = {}

        # This block makes the user input raw inputs and their quantities.
        while True:
            print("Choose a raw material input. If there are no more raw inputs, press Enter.\nCurrent inputs:\n")
            for material, quantity in raw_materials.items():
                print(f"{quantity} {material} per minute.")
            raw_input = input("\n").title()
            if raw_input == "":
                clear()
                break
            elif raw_input not in raw_inputs:
                clear()
                print("Raw input does not exist.")
            else:
                clear()
                while True:
                    raw_input_quantity = input(f"How many {raw_input} do you have per minute?\n")
                    try:
                        float(raw_input_quantity)
                    except ValueError:
                        clear()
                        print("Please enter a numerical value.")
                    else:
                        raw_materials[raw_input] = raw_input_quantity
                        clear()
                        break


main()