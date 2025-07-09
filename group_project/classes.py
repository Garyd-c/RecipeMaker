"""
This file contains all the CRUD classes and functions to work with the database.
"""

"""//////////////////////////////////////////////   VIEW   /////////////////////////////////////////////////////////////"""

recipe_id_name = "test"
recipe_id_number = "1"
recipe_id = "".join(str(recipe_id_name) + str(recipe_id_number).rjust((5 - len(recipe_id_number)),"0"))
print(recipe_id)



"""
class View:
    # View list of recipes
    # View full recipe
    # View Ingredient list

    recipe_number = int()

    def __init__(self, recipe_number):
        self.recipe_number = recipe_number

    def lookUp(self):

        # Open File
        with open("recipe_list.txt", "r") as file:
            content = file.read()
            data_list = eval(content)  # Use with caution

        # Print Lookup list
        for i in data_list:
            print(str(data_list.index(i)) + "  " + i["name"].title())

    def recipeLookUp(self):

        # Open File
        with open("recipe_list.txt", "r") as file:
            content = file.read()
            data_list = eval(content)  # Use with caution

        # recipe is printed out
        print("\n" + data_list[self.recipe_number]["name"].title())
        print(data_list[self.recipe_number]["Description"])
        for item in data_list[self.recipe_number]["ingredients"]:
            print(item)
        try:
            for item in data_list[self.recipe_number]["step"]:
                print(item)
        except:
            pass
        finally:
            print("\n")

    def ingredientLookUp(self):

        # Open File
        with open("recipe_list.txt", "r") as file:
            content = file.read()
            data_list = eval(content)  # Use with caution

        # Ingredient List is printed out
        print("\n" + data_list[self.recipe_number]["name"].title())
        print(data_list[self.recipe_number]["Description"])
        for item in data_list[self.recipe_number]["ingredients"]:
            print(item)


"""#/////////////////////////////////////////////////  UPDATE  ///////////////////////////////////////////////////////////////#
"""

class Update:
    # What recipe would you like to update?
    # What part of the recipe would you like to update?
        # The full recipe
        # Different keys to the recipe
    # full or partial recipe update
    # Does this look correct?

    recipe_number = int()
    recipe_part = int()

    def __init__(self, recipe_number,recipe_part):
        self.recipe_number = recipe_number
        self.recipe_part = recipe_part



    def listPartNumbers(self):
        recipe_parts = ["name", "Description", "ingredients, units, and unit_amount", "steps", "full recipe"]
        for i in recipe_parts:
            print(str(recipe_parts.index(i)) + "  " + str(i))



    def lookCorrect(self,data_list):

        # recipe is printed out
        print("\n" + data_list[self.recipe_number]["name"].title())
        print(data_list[self.recipe_number]["Description"])
        for item in data_list[self.recipe_number]["ingredients"]:
            print(item)
        try:
            for item in data_list[self.recipe_number]["step"]:
                print(item)
        except:
            pass



    def updateFile(self,confirmation,data_list):
        # Update file
        if int(confirmation) == 1:
            with open("recipe_list.txt", "w") as file:
                file.write(str(data_list))
            print("The recipe was updated!")
        else:
            print("Recipe was not updated.")



    def updateRecipe(self):
        # Open File
        with open("recipe_list.txt", "r") as file:
            content = file.read()
            data_list = eval(content)  # Use with caution


        # Recipe Part numbers
        if self.recipe_part == 0:
            print("\nPrevious name: " + data_list[self.recipe_number]["name"].title())
            data_list[self.recipe_number]["name"] = input("\nWhat is the new name of your recipe? ")




        elif self.recipe_part == 1:
            print("\nPrevious Description: " + data_list[self.recipe_number]["Description"].title())
            data_list[self.recipe_number]["Description"] = input("\nWhat is the new Description of your recipe? ")



        elif self.recipe_part == 2:
            # Ingredient list
            new_item1 = []
            new_item2 = []
            new_item3 = []
            data_list[self.recipe_number]["ingredients"] = new_item1
            data_list[self.recipe_number]["units"] = new_item2
            data_list[self.recipe_number]["unit_amount"] = new_item3

            while True:
                item = input("What is the ingredient? ")
                if item.lower() == "q":
                    data_list[self.recipe_number]["ingredients"] = new_item1
                    data_list[self.recipe_number]["units"] = new_item2
                    data_list[self.recipe_number]["unit_amount"] = new_item3
                    break
                else:
                    new_item1.append(item)
                item = input("What unit do you use for measurement (for example: cup, liter, tbsp)? ")
                if item.lower() == "q":
                    data_list[self.recipe_number]["ingredients"] = new_item1
                    data_list[self.recipe_number]["units"] = new_item2
                    data_list[self.recipe_number]["unit_amount"] = new_item3
                    break
                else:
                    new_item2.append(item)
                item = input(f"How much should be added? ")
                if item.lower() == "q":
                    data_list[self.recipe_number]["ingredients"] = new_item1
                    data_list[self.recipe_number]["units"] = new_item2
                    data_list[self.recipe_number]["unit_amount"] = new_item3
                    break
                else:
                    new_item3.append(item)
                item = input(f"Do you want to add another ingredient?\nType 'q' to update the recipe: ")
                if item.lower() == "q":
                    data_list[self.recipe_number]["ingredients"] = new_item1
                    data_list[self.recipe_number]["units"] = new_item2
                    data_list[self.recipe_number]["unit_amount"] = new_item3
                    break
                else:
                    pass



        elif self.recipe_part == 3:
            # Add steps
            step_number = 1
            step = []

            while True:
                item = input(f"What is step #{step_number}? ")
                if item.lower() == "q":
                    data_list[self.recipe_number]["step"] = step
                    break
                else:
                    step.append(item)
                    step_number += 1
                item = input(f"\nWould you like to continue?\nType 'q' to update recipe: ")
                if item.lower() == "q":
                    data_list[self.recipe_number]["step"] = step
                    break
                else:
                    pass



        elif self.recipe_part == 4:

            # Update Name
            data_list[self.recipe_number]["name"] = input("What is the new name of your recipe? ")
            # Update Description
            data_list[self.recipe_number]["Description"] = input("What is the new Description of your recipe? ")

            # Ingredient list
            new_item1 = []
            new_item2 = []
            new_item3 = []
            data_list[self.recipe_number]["ingredients"] = new_item1
            data_list[self.recipe_number]["units"] = new_item2
            data_list[self.recipe_number]["unit_amount"] = new_item3

            while True:
                item = input("What is the ingredient? ")
                if item.lower() == "q":
                    data_list[self.recipe_number]["ingredients"] = new_item1
                    data_list[self.recipe_number]["units"] = new_item2
                    data_list[self.recipe_number]["unit_amount"] = new_item3
                    break
                else:
                    new_item1.append(item)
                item = input("What unit do you use for measurement (for example: cup, liter, tbsp)? ")
                if item.lower() == "q":
                    data_list[self.recipe_number]["ingredients"] = new_item1
                    data_list[self.recipe_number]["units"] = new_item2
                    data_list[self.recipe_number]["unit_amount"] = new_item3
                    break
                else:
                    new_item2.append(item)
                item = input(f"How much should be added? ")
                if item.lower() == "q":
                    data_list[self.recipe_number]["ingredients"] = new_item1
                    data_list[self.recipe_number]["units"] = new_item2
                    data_list[self.recipe_number]["unit_amount"] = new_item3
                    break
                else:
                    new_item3.append(item)
                item = input(f"Do you want to add another ingredient?\nType 'q' to continue to the steps: ")
                if item.lower() == "q":
                    data_list[self.recipe_number]["ingredients"] = new_item1
                    data_list[self.recipe_number]["units"] = new_item2
                    data_list[self.recipe_number]["unit_amount"] = new_item3
                    break
                else:
                    pass

            # Add steps
            step_number = 1
            step = []

            while True:
                item = input(f"What is step #{step_number}? ")
                if item.lower() == "q":
                    data_list[self.recipe_number]["step"] = step
                    break
                else:
                    step.append(item)
                    step_number += 1
                item = input(f"\nWould you like to continue?\nType 'q' to update recipe: ")
                if item.lower() == "q":
                    data_list[self.recipe_number]["step"] = step
                    break
                else:
                    pass

        # View update recipe
        Update(self.recipe_number,0).lookCorrect(data_list)

        # Update recipe
        Update(self.recipe_number, 0).updateFile(
            input("Does this look correct?\nType 1 to confirm and update: "), data_list)




"""#/////////////////////////////////////    DELETE   ////////////////////////////////////////////#
"""


class Delete:
    # What recipe would you like to delete?
    # confirmation

    recipe_number = int()

    def __init__(self, recipe_number):
        self.recipe_number = recipe_number

    def updateFile(self,confirmation,data_list):
        # Update file
        if int(confirmation) == 1:
            with open("recipe_list.txt", "w") as file:
                file.write(str(data_list))
            print("The recipe was removed")
        else:
            print("The recipe was not removed")
        print("")



    def deleteRecipe(self):
        # Open File
        with open("recipe_list.txt", "r") as file:
            content = file.read()
            data_list = eval(content)  # Use with caution

        recipe_to_delete = data_list.pop(self.recipe_number)
        confirmation = input(f"Are you sure you want to delete {recipe_to_delete["name"]}?\n"
                             f"Type 1 to confirm and update: ")

        self.updateFile(int(confirmation),data_list)
"""