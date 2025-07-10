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

        rl = func.RecipeList()
        il = func.IngredientList()
        sl = func.StepsList()

        if selection == 1:
# View recipe List

            print("\nRecipe List"
                "\n--------------")

            for recipe in rl.fetch_recipe(None):
                print(recipe[0])


        elif selection == 2:
# View a full recipe
            rname = input("Which recipe would you like to see? ")
            print("")
            print(rl.fetch_recipe(rname)[0][0].center(30," "))
            print("".center(30,"-"))
            print(rl.fetch_recipe(rname)[0][1])
            print("Category: " + rl.fetch_recipe(rname)[0][2])
            print("\n"+"Ingredients".center(30," "))
            print("".center(30,"-"))
            for ingredient in il.fetch_ing(rname,None):
                print(str(ingredient[4])+" "+ingredient[3]+": "+ingredient[2])
            print("\n" + "Steps".center(30," "))
            print("".center(30,"-"))
            for step in sl.fetch_steps(rname,None):
                print(str(step[1])+": "+step[2])


        elif selection == 3:
# View the ingredient list for a recipe
            rname = input("Which recipe would you like to see? ")
            print("\n"+"Ingredients".rjust(len("Ingredients")+2," "))
            print("".center(len("Ingredients")+4,"-"))
            for ingredient in il.fetch_ing(rname,None):
                print(ingredient[2])

        elif selection == 4:
# Create new recipe

            # Add recipe to the recipes table

            rname = input("What is the name of the recipe? ")
            rdescription = input("Describe your recipe: ")
            rcategory = input("What category does the recipe belong to? ")
            rl.add_recipe(rname,rdescription,rcategory)

            # Add recipe ingredients for the ingredients table

            while True:
                ringredient = input("Ingredient name: ")
                runit = input("Unit of measurement (cup/tbsp/grams/etc): ")
                rquantity = int(input("Unit amount: "))
                il.add_ing(rname,ringredient,runit,rquantity)
                if input("Add another ingredient? (y/n): ").lower() == "n":
                    break
                
            # Gather steps
            count = 1
            while True:
                rstep = input(f"What is step {str(count)}? ")
                count += 1
                sl.add_steps(rname,rstep)
                if input("Add another step? (y/n): ").lower() == "n":
                    break


        elif selection == 5:
# Update a recipe
            print("Not configured yet")
            pass

        elif selection == 6:
# Delete a recipe
            rname = input("What is the name of the recipe you would like to delete? ")
            confirmation = input(f"Are you sure you would like to delete {rname}?\nType 'y' for yes 'n' for no, then press enter (y/n): ").lower()
            if confirmation == "y":
                rl.delete_recipe(rname)
            else:
                print("Delete request aborted.")

        elif selection == 7:
# Reset Database
            while True:
                confirmation1 = input(f"Reseting the database will delete all recipes.\nType 'y' to continue or 'n' to abort, then press enter (y/n): ").lower()
                if confirmation1 == "y":
                    while True:
                        confirmation2 = input(f"Reset Database?\nType 'y' to confirm 'n' to abort, then press enter (y/n): ").lower()
                        if confirmation2 == "y":
                            rl.reset_database_recipe()
                            break
                        elif confirmation2 == "n":
                            print("Reset request aborted.")
                            break
                        else:
                            print("Please type 'y' or 'n'")
                    break        
                elif confirmation1 == "n":
                    print("Reset request aborted.")
                    break
                else:
                    print("Please type 'y' or 'n'")


        elif selection == 8:
# Close Program
            print("Program Closed. Have a great day!\n")
            break

        else:
            print("The number you entered is not in the list.")

    except Exception as e:
            print("An error has occurred.", e)


    input("\nPress 'Enter' to return to menu")
    
