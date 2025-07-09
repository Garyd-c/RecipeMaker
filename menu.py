import functions as func

while True:
    try:    
        selection = int(input("View your recipes here!\n"
                            "Enter a number from the list below:\n\n"
                            "1  View recipe List\n"
                            "2  View a full recipe\n"
                            "3  View the ingredient list for a recipe\n"
                            "4  Create new recipe\n"
                            "5  Update a recipe\n"
                            "6  Delete a recipe\n"
                            "7  Reset Database\n"
                            "8  Close program\n\n"
                            "What would you like to do? "))


        if selection == 1:
            print("\nRecipe List"
                "\n--------------")
            rl = func.RecipeList()
            for recipe in rl.fetch_recipe(None):
                print(recipe[0])

        elif selection == 2:
            # View a full recipe
            pass

        elif selection == 3:
            # View the ingredient list for a recipe
            pass

        elif selection == 4:
            # Create new recipe
            pass

        elif selection == 5:
            # Update a recipe
            pass

        elif selection == 6:
            # Delete a recipe
            pass

        elif selection == 6:
            # Reset Database
            pass

        elif selection == 8:
            print("Program Closed. Have a great day!")
            break

        else:
            print("The number you entered is not in the list.")

    except Exception as e:
            print("An error has occurred.", e)


    input("\nPress 'Enter' to return to menu")
    
