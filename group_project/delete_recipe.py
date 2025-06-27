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

