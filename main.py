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

        # This block makes the user input raw inputs and their quantities. Currently not used, may be deleted.
        # while True:
        #     print("Choose a raw material input. If there are no more raw inputs, press Enter.\nCurrent inputs:\n")
        #     for material, quantity in raw_materials.items():
        #         print(f"{quantity} {material} per minute.")
        #     raw_input = input("\n").title()
        #     if raw_input == "":
        #         clear()
        #         break
        #     elif raw_input not in raw_inputs:
        #         clear()
        #         print("Raw input does not exist.")
        #     else:
        #         clear()
        #         while True: # Start of input quanitity user input.
        #             raw_input_quantity = input(f"How many {raw_input} do you have per minute?\n")
        #             try:
        #                 float(raw_input_quantity)
        #             except ValueError:
        #                 clear()
        #                 print("Please enter a numerical value.")
        #             else:
        #                 raw_materials[raw_input] = raw_input_quantity
        #                 clear()
        #                 break
        
        # This block identifies all recipes required for the product recipe, including dependancies.
        recipes_required = []
        recipes_required.append(product_recipe)
        print(type(items_per_minute))
        for recipe in recipes_required:
            print(recipes_required) #NOTE - debugging
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

        machine, multiplier = machine_count(product_recipe, items_per_minute)
        power = power_usage(product_recipe, multiplier)
        inputs = inputs_required(product_recipe, multiplier)

        print(f"Machine Count = {machine, multiplier}")
        print(f"Power Usage = {power}")
        print(f"Inputs Required = {inputs}")



# ============================================================================================================= #
# Calculation Methods
# ============================================================================================================= #

def machine_count(recipe, item_quantity):
    machine = recipes[recipe]["machine"]
    output = recipes[recipe]["output"]
    multiplier = (item_quantity / output)
    return machine, multiplier

def power_usage(recipe, number_of_machines):
    power = (recipes[recipe]["power"] * number_of_machines)
    return power

def inputs_required(recipe, number_of_machines):
    input_list = []
    x = 0
    for material in recipes[recipe]["materials"]:
        quantity = (recipes[recipe]["input"][x] * number_of_machines)
        input_list.append((material, quantity))
        x += 1
    return input_list
    

main()