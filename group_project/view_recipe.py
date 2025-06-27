class View:
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