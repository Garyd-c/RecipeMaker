
def newRecipe():
    # Create a dictionary that holds:
    # Recipe Name
    # Recipe Description
    # Recipe list with ingredients, units, and unit amounts
    # Recipe steps
    # Updata Database with new data

    # Define recipe as dictionary
    new_recipe = {}

    # Add name and description
    new_recipe["name"] = input("What is the name of your recipe? ")
    new_recipe["Description"] = input("Describe your recipe? ")

    # Ingredient list
    new_item1 = []
    new_item2 = []
    new_item3 = []

    while True:
        item = input("What is the ingredient? ")
        if item.lower() == "done":
            new_recipe["ingredients"] = new_item1
            new_recipe["units"] = new_item2
            new_recipe["unit_amount"] = new_item3
            break
        else:
            new_item1.append(item)
        item = input("What unit do you use for measurement (for example: cup, liter, tbsp)? ")
        if item.lower() == "done":
            new_recipe["ingredients"] = new_item1
            new_recipe["units"] = new_item2
            new_recipe["unit_amount"] = new_item3
            break
        else:
            new_item2.append(item)
        item = input(f"How much should be added? ")
        if item.lower() == "done":
            new_recipe["ingredients"] = new_item1
            new_recipe["units"] = new_item2
            new_recipe["unit_amount"] = new_item3
            break
        else:
            new_item3.append(item)
        item = input(f"Do you want to add another ingredient?\nType 'done' to describe the steps: ")
        if item.lower() == "done":
            new_recipe["ingredients"] = new_item1
            new_recipe["units"] = new_item2
            new_recipe["unit_amount"] = new_item3
            break
        else:
            pass


    # Add steps
    step_number = 1
    step = []

    while True:
        item = input(f"What is step #{step_number}? ")
        if item.lower() == "done":
            new_recipe["step"] = step
            break
        else:
            step.append(item)
            step_number += 1
        item = input(f"\nWould you like to continue?\nType 'done' to complete recipe: ")
        if item.lower() == "done":
            new_recipe["step"] = step
            break
        else:
            pass


    # Update records

    # Step 1: Read the list from the text file
    with open("recipe_list.txt", "r") as file:
        content = file.read()
        data_list = eval(content)  # Use with caution

    # Step 2: Append a new item
    data_list.append(new_recipe)

    # Step 3: Write it back to the file
    with open("recipe_list.txt", "w") as file:
        file.write(str(data_list))

