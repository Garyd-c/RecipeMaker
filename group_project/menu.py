import functions as func

while True:
    selection = int(input("View your recipes here!\n"
                          "Enter a number from the list below:\n\n"
                          "1  View recipe List\n"
                          "2  View a full recipe\n"
                          "3  View the ingredient list for a recipe\n"
                          "4  Create new recipe\n"
                          "5  Update a recipe\n"
                          "6  Delete a recipe\n"
                          "7  Close program\n\n"
                          "What would you like to do? "))


    if selection == 1:
        # User view a list of the recipes
        func.RecipeList.fetch_recipe(None)

    elif selection == 2:
        # User selects recipe
        recipe_number = int(input("Enter the number of a recipe: "))

        # Recipe List is printed out
        func.RecipeList.fetch_recipe(None)

    elif selection == 3:
        # User selects recipe
        recipe_number = int(input("Enter the number of a recipe you would like to view: "))

        # Ingredient list for recipe is printed out
        cl.View(recipe_number).ingredientLookUp()

    elif selection == 4:
        # start function
        cr.newRecipe()

    elif selection == 5:
        # User selects recipe
        recipe_number = int(input("Enter the number of a recipe you would like to update: "))

        # Display options and user selects the part of the recipe to update
        cl.Update(0,0).listPartNumbers()
        recipe_part = int(input("Enter the number of the part of recipe you would like to update: "))

        # Initiate update recipe function
        cl.Update(recipe_number,recipe_part).updateRecipe()
        pass

    elif selection == 6:
        # User selects recipe
        recipe_number = int(input("Enter the number of a recipe you would like to delete"))
        cl.Delete(recipe_number).deleteRecipe()

    elif selection == 7:
        print("Program Closed. Have a great day!")
        break

    if input("\nWould you like to return to the menu?\nType 'no' to close the program: ").lower() == "no":
        break
