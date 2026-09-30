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
# - User provides alternate recipes
# - User provides raw inputs
# - Program determines all recipes used in the process
# - Program swaps any base recipes for alternate recipes chosen

# Clears the terminal.
def clear():
    os = platform.system()
    if os == "Linux":
        subprocess.run("clear")
    elif os == "Windows":
        subprocess.run("cls")

# Identifies all recipes required for the product recipe, including dependancies.
def replace_alts(product_recipe, chosen_alt_recipes):
    recipes_required = []
    recipes_required.append(product_recipe)
    for recipe in recipes_required:
        recipe_materials = recipes[recipe]["materials"]
        for material in recipe_materials:
            for alt_recipe in chosen_alt_recipes:
                if material in recipes_required or material in raw_inputs:
                    continue
                elif recipes[material]["output material"] == recipes[alt_recipe]["output material"]:
                    recipes_required.append(alt_recipe)
                    continue
                else:
                    recipes_required.append(material)
    return recipes_required

# Adds final data numbers, after calculations, to a dictionary, which is used for the final report.
def recipe_report(recipe, machine, multiplier, inputs, outputs, power):
    GREEN = "\033[92m"
    RED = "\033[91m"
    RESET = "\033[0m"

    print(f"{GREEN}={RESET}" * 60)
    print(f"{GREEN}{recipe:^60}{RESET}")
    print(f"{GREEN}{'=' * 60}{RESET}")
    print("\n")

    print("MACHINES REQUIRED")
    print(f" {machine:<26}{multiplier:>10}")
    print("INPUTS REQUIRED")
    for item, quantity in inputs:
        print(f"{GREEN} {item:<25}{quantity:>10}{RESET}")
    print("OUTPUT QUANTITY")
    print(f"{RED} {outputs:<25}{recipes[recipe]['output material']:>10}{RESET}")
    print(f"{'POWER USAGE':<26}{power:>10}")
    

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

         # This block asks the user for the required number of items per minute.
        while True:
            items_per_minute = input("How many items per minute would you like to produce?\n")
            try:
                float(items_per_minute)
            except ValueError:
                clear()
                print("Please enter a numerical value.")
            else:
                items_per_minute = float(items_per_minute)
                clear()
                break
        
        chosen_alt_recipes = []

        # This block makes the user select any alternate recipes they wish to use in their production line.
        while True: 
            alt_recipe = input(f"Which alternate recipes would you like to use? If there are no more recipes, press Enter.\nCurrent recipes: {chosen_alt_recipes}\n").title()
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
                chosen_alt_recipes.append(alt_recipe)
        
        recipes_required = replace_alts(product_recipe, chosen_alt_recipes)

        # ===================================== Recipe Calculations ============================================== #
        recipes_manufactured = []
        recipes_manufactured.append(product_recipe)
        print(recipes_required)

        while len(recipes_manufactured) > 0:
            item = recipes_manufactured[0]
            for recipe in recipes_required:
                if item in recipes_required or item in raw_inputs:
                    continue
                elif recipes[item]["output material"] == recipes[recipe]["output material"]:
                    recipes_manufactured.append(recipe)
                    recipes_manufactured.pop(0)

            if item in raw_inputs:
                recipes_manufactured.pop(0)
                continue
            else:
                machine, multiplier = machine_count(item, items_per_minute)
                power = power_usage(item, multiplier)
                input_quantity = inputs_required(item, multiplier)
                output = output_quantity(item, multiplier)
                recipes_manufactured.extend(recipes[item]["materials"])
                recipe_report(item, machine, multiplier, input_quantity, output, power)
                recipes_manufactured.pop(0)
        

# ============================================================================================================= #
# Calculation Methods
# ============================================================================================================= #

# Calculates how many machines are required for a recipe, using user's inputted number of required items per minute.
def machine_count(recipe, item_quantity): 
    machine = recipes[recipe]["machine"]  
    output = recipes[recipe]["output"]
    multiplier = (item_quantity / output)
    return machine, multiplier

# Calculates power usage, using the multiplier from "machine_count()"
def power_usage(recipe, multiplier):
    power = (recipes[recipe]["power"] * multiplier)
    return power

# Calculates total input quantity required, using the multiplier from "machine_count()"
def inputs_required(recipe, multiplier):
    input_list = []
    x = 0
    for material in recipes[recipe]["materials"]:
        quantity = (recipes[recipe]["input"][x] * multiplier)
        input_list.append((material, quantity))
        x += 1
    return input_list

# Calculates total output quantity, using the multiplier from "machine_count()"
def output_quantity(recipe, multiplier):
    quantity = (recipes[recipe]["output"] * multiplier)
    return quantity
    

main()