"""
This file has the code for the classes and functions

Contents:

Ingredints Class:
    Create: add_ing()
    Retrieve: fetch_ing()
    Update: update_ing()
    Delete: delete_ing()
    Reset: reset_database_ing()

Steps Class:
    Create: add_steps()
    Retrieve: fetch_steps()
    Update: update_steps()
    Delete: delete_steps()
    Reset: reset_database_steps()

Recipes Class
    Create: add_recipe()
    Retrieve: fetch_recipe()
    Update: update_recipe()
    Delete: delete_recipe()
    Reset: reset_database_recipe()

Upload CSV Class
"""

import db_base as db
import csv


#////////////////////////////////// Ingredients Class //////////////////////////////////#


class IngredientList(db.DBbase):

    def __init__(self):
        super().__init__("recipedb.sqlite")

# Create
    def add_ing(self,recipe_name,ingredient,unit=None,quantity=1):
        if quantity is not None and quantity <= 0:
            raise ValueError("Quantity must be greater than 0.")
        try:
            super().get_cursor.execute("INSERT OR IGNORE INTO Ingredients (recipe_name,ingredient,unit,quantity) values(?,?,?,?);", (recipe_name,ingredient,unit,quantity))
            super().get_connection.commit()
            print(f"Added {ingredient} to {recipe_name} successfully")
        except Exception as e:
            print("An error has occurred.", e)

# Retrieve
    def fetch_ing(self, recipe_name=None, ingredient_id=None):
        try:
            # View an individual ingredient:

            if ingredient_id is not None:
                return super().get_cursor.execute("SELECT * FROM Ingredients WHERE ingredient_id = ?;", (ingredient_id,)).fetchone()
            
            # View a recipe ingredient list:

            elif recipe_name is not None:
                return super().get_cursor.execute("SELECT * FROM Ingredients WHERE recipe_name = ?;", (recipe_name,)).fetchall()
            
            # View the full DB of ingredients

            else:
                return super().get_cursor.execute("SELECT * FROM Ingredients;").fetchall()

        except Exception as e:
            print("An error has occurred.", e)
            return False

# Update
    def update_ing(self, ingredient_id):     

        self._ing_name = ""
        self._ing_unit = ""
        self._ing_quantity = 0

        # Selection Menu

        print("What would you like to update?\n"
              "1: Ingredient Name\n"
              "2: Unit of measurement\n"
              "3: Quantity called for\n")

        option = int(input())

        # Update ingredient name
        if option == 1:
            print("What is the updated ingredient name?")
            self._ing_name = input()

            try:
                super().get_cursor.execute("UPDATE Ingredients SET ingredient = ? WHERE ingredient_id = ?;", (self._ing_name, ingredient_id))
                super().get_connection.commit()
                print(f"Update record to {self._ing_name} success!")

            except Exception as e:
                print("An error has occurred.", e)

        # Update unit of measurement
        elif option == 2:
            print("What is the updated unit of measurement?")
            self._ing_unit = input()

            try:
                super().get_cursor.execute("UPDATE Ingredients SET unit = ? WHERE ingredient_id = ?;", (self._ing_unit, ingredient_id))
                super().get_connection.commit()
                print(f"Update record to {self._ing_unit} success!")

            except Exception as e:
                print("An error has occurred.", e)

        # Update quantity called for
        elif option == 3:
            print("What is the updated quantity?")
            self._ing_quantity = input()

            try:
                super().get_cursor.execute("UPDATE Ingredients SET quantity = ? WHERE ingredient_id = ?;", (self._ing_quantity, ingredient_id))
                super().get_connection.commit()
                print(f"Update record to {self._ing_quantity} success!")

            except Exception as e:
                print("An error has occurred.", e)

        # Handle alternate options
        else:
            print("That is not a valid option. Thank you.")

# Delete
    def delete_ing(self, recipe_name=None, ingredient_id=None):
        try:
            
            # Delete an individual ingredient:

            if ingredient_id is not None:
                super().get_cursor.execute("DELETE FROM Ingredients WHERE ingredient_id = ?;", (ingredient_id,))
                print(f"Deleted ingredient id: {ingredient_id} successfully")

            # Delete a full recipe ingredient list:

            elif recipe_name is not None:
                super().get_cursor.execute("DELETE FROM Ingredients WHERE recipe_name = ?;", (recipe_name,))
                print(f"Deleted {recipe_name} ingredients successfully")
            
            # Save to DB

            super().get_connection.commit()
            return True
        
        except Exception as e:
            print("An error has occurred.", e)
            return False

# Reset

    def reset_database_ing(self):
        try:
            sql = """

                DROP TABLE IF EXISTS Ingredients;

                CREATE TABLE Ingredients (
                    ingredient_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    recipe_name TEXT,
                    ingredient TEXT NOT NULL,
                    unit TEXT,
                    quantity REAL CHECK (quantity > 0),
                    FOREIGN KEY (recipe_name) REFERENCES Recipes(recipe_name)
                );"""
            super().execute_script(sql)
        except Exception as e:
            print("An error occured.", e)
        finally:
            super().close_db()



#///////////////////////////////// Steps Class ///////////////////////////////////////#


class StepsList(db.DBbase):

    def __init__(self):
        super().__init__("recipedb.sqlite")

# Create
    def add_steps(self,recipe_name,step):
        try:
            # Determine the step order for the recipe

            last_step = super().get_cursor.execute("SELECT MAX(step_order) FROM Steps WHERE recipe_name = ?;", (recipe_name,)).fetchone()[0]
            if last_step == None:
                step_order = 1
            else:
                step_order = int(last_step) + 1

            # Add new step

            super().get_cursor.execute("INSERT INTO Steps (recipe_name,step_order,step) values(?,?,?);", (recipe_name,step_order,step))

            # Save to DB

            super().get_connection.commit()
            print(f"Added {step} successfully")
        except Exception as e:
            print("An error has occurred.", e)

# Retrieve
    def fetch_steps(self, recipe_name=None, step_order=None):
        if step_order is not None and step_order <= 0:
            raise ValueError("Step must be a number more than 0.")
        try:
            # View an individual step of a recipe:

            if recipe_name is not None and step_order is not None:
                return super().get_cursor.execute("SELECT * FROM Steps WHERE recipe_name = ? AND step_order = ?;", (recipe_name,step_order)).fetchone()
            
            # View the list of recipe steps:

            elif recipe_name is not None:
                return super().get_cursor.execute("SELECT * FROM Steps WHERE recipe_name = ?;", (recipe_name,)).fetchall()
            
            # View the full DB of steps

            else:
                return super().get_cursor.execute("SELECT * FROM Steps;").fetchall()

        except Exception as e:
            print("An error has occurred.", e)
            return False

# Update
    def update_steps(self, recipe_name, step_order):
        # Get replacement step instruction:

        print(f"What is the new step for {recipe_name} step #{step_order}?")
        self._updated_step = input()

        # Update DB

        try:
            super().get_cursor.execute("UPDATE Steps SET step = ? where recipe_name = ? AND step_order = ?;", (self._updated_step, recipe_name, step_order))
            super().get_connection.commit()
            print(f"Updated step #{step_order} for {recipe_name}!")
        except Exception as e:
            print("An error has occurred.", e)

# Delete
    def delete_steps(self, recipe_name=None, step_order=None):
        try:
            # Delete an individual step of a recipe:

            if recipe_name is not None and step_order is not None:
                super().get_cursor.execute("DELETE FROM Steps WHERE recipe_name = ? AND step_order = ?;", (recipe_name,step_order)).fetchone()
                print(f"Deleted step: {step_order} from {recipe_name} successfully")

            # Delete the list of recipe steps:

            elif recipe_name is not None:
                super().get_cursor.execute("DELETE FROM Steps WHERE recipe_name = ?;", (recipe_name,)).fetchall()
                print(f"Deleted steps for {recipe_name} successfully")

            # View the full DB of steps

            else:
                super().get_cursor.execute("DELETE FROM Steps;").fetchall()
                print(f"Deleted all recipe steps successfully")

            
            # Save to DB

            super().get_connection.commit()
            return True
        
        except Exception as e:
            print("An error has occurred.", e)
            return False

# Reset

    def reset_database_steps(self):
        try:
            sql = """

                DROP TABLE IF EXISTS Steps;

                CREATE TABLE Steps (
                    recipe_name TEXT,
                    step_order INTEGER NOT NULL,
                    step TEXT NOT NULL,
                    PRIMARY KEY (recipe_name, step_order),
                    FOREIGN KEY (recipe_name) REFERENCES Recipes(recipe_name)
                ); """
            super().execute_script(sql)
        except Exception as e:
            print("An error occured.", e)
        finally:
            super().close_db()




#///////////////////////////////// Recipe Class ///////////////////////////////////////#


class RecipeList(db.DBbase):

    def __init__(self):
        super().__init__("recipedb.sqlite")

# Create
    def add_recipe(self,recipe_name,description,category):
        try:
            # Add new recipe

            super().get_cursor.execute("INSERT INTO Recipes (recipe_name,description,category) values(?,?,?);", (recipe_name,description,category))

            # Save to DB

            super().get_connection.commit()

# Mike's code: 
            # Add ingredients for the recipe added

            # Add initial ingredient to the list
            ingredients = []
            print("Enter the first ingredient?")
            new_ing = (input())
            another_ing = "y"
            ingredients.append(new_ing)
            print("Would you like to add another ingredient? y/n ")
            another_ing = input().lower()

            # Add additional ingredients
            while another_ing != "n":
                print("What is the next ingredient?")
                new_ing = (input())
                ingredients.append(new_ing)
                another_ing = input("Would you like to add another ingredient? y/n ").lower()
                #recipe_name,ingredient,unit,quantity

            # Pull classes
            ingredient_list = IngredientList()
            steps_list = StepsList()

            # Go through each ingredient to add units and measurements
            for ingredient in ingredients:
                unit = input("What is the unit of measurement for " + ingredient + "? ")
                quantity = float(input("How many units of {}? ".format(ingredient)))
                ingredient_list.add_ing(recipe_name, ingredient, unit, quantity)

            # Add steps for the recipe and ingredients added

            # Add initial Step
            new_cooking_steps = []
            print("What is the first instruction?")
            new_step = input()
            new_cooking_steps.append(new_step)
            print("Would you like to add another step? y/n")
            another_step = input().lower()

            # Add additional steps
            while another_step != "n":
                print("What is the next step?")
                new_step = (input())
                new_cooking_steps.append(new_step)
                another_step = input("Would you like to add another step? y/n ").lower()

            # Add steps to recipe list.
            for step in new_cooking_steps:
                steps_list.add_steps(recipe_name, step)
# End Mikes code

            print(f"Added {recipe_name} successfully")
        except Exception as e:
            print("An error has occurred.", e)

# Retrieve
    def fetch_recipe(self, recipe_name=None, name_start = None, name_end = None):
        try:        
            # View the list of recipe steps:

            if recipe_name is not None:
                return super().get_cursor.execute("SELECT * FROM Recipes WHERE recipe_name = ?;", (recipe_name,)).fetchall()
            
            # View the full DB of ingredients

            elif name_start is not None:
                return super().get_cursor.execute("SELECT * FROM Recipes WHERE recipe_name >= ? AND recipe_name < ?;", (name_start, name_end)).fetchall()

            else:
                return super().get_cursor.execute("SELECT * FROM Recipes;").fetchall()

        except Exception as e:
            print("An error has occurred.", e)
            return False

# Update
    def update_recipe(self, recipe_name):

        self._new_recipe_name = ""
        self._new_description = ""
        self._new_category = ""

        # Selection Menu

        print("What would you like to update?\n"
              "1: Recipe Name\n"
              "2: Recipe Description\n"
              "3: Recipe Category")

        option = int(input())

        # Update Recipe Name
        if option == 1:
            print("What is the updated recipe name?")
            self._new_recipe_name = input()

            try:
                # Update all tables
                super().get_cursor.execute("UPDATE Recipes SET recipe_name = ? WHERE recipe_name = ?;", (self._new_recipe_name, recipe_name))
                super().get_cursor.execute("UPDATE Ingredients SET recipe_name = ? WHERE recipe_name = ?;", (self._new_recipe_name, recipe_name))
                super().get_cursor.execute("UPDATE Steps SET recipe_name = ? WHERE recipe_name = ?;", (self._new_recipe_name, recipe_name))

                # Save Changes
                super().get_connection.commit()
                print(f"Updated record from {recipe_name} to {self._new_recipe_name}")

            except Exception as e:
                print("An error has occurred.", e)

        # Update Recipe Description
        elif option == 2:
            print("What is the updated description?")
            self._new_description = input()

            try:
                # Update table
                super().get_cursor.execute("UPDATE Recipes SET description = ? WHERE recipe_name = ?;", (self._new_description, recipe_name))

                # Save changes
                super().get_connection.commit()
                print(f"Updated {recipe_name}!")

            except Exception as e:
                print("An error has occurred.", e)

        # Update Recipe Category
        elif option == 3:
            print("What is the updated category?")
            self._new_category = input()

            try:
                super().get_cursor.execute("UPDATE Recipes SET category = ? WHERE recipe_name = ?;", (self._new_category, recipe_name))
                super().get_connection.commit()
                print(f"Updated {recipe_name}!")

            except Exception as e:
                print("An error has occurred.", e)

        # Handle Alternate inputs
        else:
            print("That is not a valid option. Thank you.")


# Delete
    def delete_recipe(self, recipe_name):
        try:
            # Delete a full recipe:

            # 1 Delete Steps table

            steps = StepsList()
            steps.delete_steps(recipe_name,None)

            # 2 Delete Ingredients table

            ing = IngredientList()
            ing.delete_ing(recipe_name,None)

            # 3 Delete Recipe Table

            super().get_cursor.execute("DELETE FROM Recipes WHERE recipe_name = ?;", (recipe_name,))
            print(f"Deleted {recipe_name} successfully")
            
            # Save to DB

            super().get_connection.commit()
            return True
        
        except Exception as e:
            print("An error has occurred.", e)
            return False

# Reset

    def reset_database_recipe(self):
        try:
            sql = """

                DROP TABLE IF EXISTS Steps;
                DROP TABLE IF EXISTS Ingredients;
                DROP TABLE IF EXISTS Recipes;

                CREATE TABLE Recipes (
                    recipe_name TEXT PRIMARY KEY,
                    description TEXT,
                    category TEXT
                );

                CREATE TABLE Ingredients (
                    ingredient_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    recipe_name TEXT,
                    ingredient TEXT NOT NULL,
                    unit TEXT,
                    quantity REAL CHECK (quantity > 0),
                    FOREIGN KEY (recipe_name) REFERENCES Recipes(recipe_name)
                );

                CREATE TABLE Steps (
                    recipe_name TEXT,
                    step_order INTEGER NOT NULL,
                    step TEXT NOT NULL,
                    PRIMARY KEY (recipe_name, step_order),
                    FOREIGN KEY (recipe_name) REFERENCES Recipes(recipe_name)
                ); """
            super().execute_script(sql)
            print("The database has been reset.")
        except Exception as e:
            print("An error occured.", e)
        finally:
            super().close_db()



#//////////////////////// Upload CSV //////////////////////////#


class Recipe:
    def __init__(self, row):
        # Assuming CSV columns: recipe_name, description, category, ingredient, unit, quantity, step_order, step
        self.recipe_name = row[0]
        self.description = row[1]
        self.category = row[2]

class Ingredient:
    def __init__(self, row):
        self.recipe_name = row[0]
        self.ingredient = row[3]
        self.unit = row[4]
        try:
            self.quantity = float(row[5])
        except ValueError:
            self.quantity = None  # or 0 or raise an error

class Step:
    def __init__(self, row):
        self.recipe_name = row[0]
        try:
            self.step_order = int(row[6])
        except ValueError:
            self.step_order = None  # or raise error
        self.step = row[7]
class CsvRecipe(db.DBbase):

    def reset_or_create_db(self):
        """
        Drops the existing Steps, Ingredients, and Recipes tables if they exist,
        then creates fresh tables for storing recipe data, ingredients, and steps.
        This ensures the database schema is up-to-date and clean.
        """
        try:
            sql = """
            DROP TABLE IF EXISTS Steps;
            DROP TABLE IF EXISTS Ingredients;
            DROP TABLE IF EXISTS Recipes;

            CREATE TABLE Recipes (
                recipe_name TEXT PRIMARY KEY,
                description TEXT,
                category TEXT
            );

            CREATE TABLE Ingredients (
                ingredient_id INTEGER PRIMARY KEY AUTOINCREMENT,
                recipe_name TEXT,
                ingredient TEXT NOT NULL,
                unit TEXT,
                quantity REAL CHECK (quantity > 0),
                FOREIGN KEY (recipe_name) REFERENCES Recipes(recipe_name)
            );

            CREATE TABLE Steps (
                recipe_name TEXT,
                step_order INTEGER NOT NULL,
                step TEXT NOT NULL,
                PRIMARY KEY (recipe_name, step_order),
                FOREIGN KEY (recipe_name) REFERENCES Recipes(recipe_name)
            );
            """
            super().execute_script(sql)
            print("Database reset/created successfully.")
        except Exception as e:
            print("Error resetting/creating database:", e)

    def read_recipe_data(self, file_name):
        """
        Reads the CSV file and parses its contents into separate lists of recipe,
        ingredient, and step objects. Uses a set to avoid duplicate recipe entries.
        """
        self.recipe_list = []
        self.ingredient_list = []
        self.step_list = []
        self.seen_recipes = set()  # Tracks recipes already added to avoid duplicates

        try:
            with open(file_name, 'r') as record:
                csv_contents = csv.reader(record)
                next(csv_contents)  # Skip the CSV header row

                for row in csv_contents:
                    # row assumed format: [recipe_name, description, category, ingredient, unit, quantity, step_order, step]

                    # Add a Recipe object only once per unique recipe_name
                    if row[0] not in self.seen_recipes:
                        recipe = Recipe(row)
                        self.recipe_list.append(recipe)
                        self.seen_recipes.add(row[0])

                    # Add Ingredient object for every row (multiple ingredients per recipe possible)
                    ingredient = Ingredient(row)
                    self.ingredient_list.append(ingredient)

                    # Add Step object for every row (multiple steps per recipe possible)
                    step = Step(row)
                    self.step_list.append(step)

                    print(row)  # Optional debug print of the row data

        except Exception as e:
            print("Error reading CSV data:", e)

    def save_to_database(self):
        """
        Saves the parsed recipes, ingredients, and steps into their respective database tables.
        Asks for confirmation before saving.
        Commits each insert operation individually, with error handling.
        """
        print(f"Number of recipes records to save: {len(self.recipe_list)}")
        print(f"Number of ingredients records to save: {len(self.ingredient_list)}")
        print(f"Number of steps records to save: {len(self.step_list)}")

        save = input("Continue? ").lower()

        if save == 'y':
            # Insert Recipes
            for item in self.recipe_list:
                try:
                    super().get_cursor.execute(
                        """INSERT OR IGNORE INTO Recipes (recipe_name, description, category)
                           VALUES (?, ?, ?)""",
                        (item.recipe_name, item.description, item.category)
                    )
                    super().get_connection.commit()
                    print("Saved recipe:", item.recipe_name)
                except Exception as e:
                    print("Error saving recipe:", e)

            # Insert Ingredients
            for item in self.ingredient_list:
                try:
                    super().get_cursor.execute(
                        """INSERT INTO Ingredients (recipe_name, ingredient, unit, quantity)
                           VALUES (?, ?, ?, ?)""",
                        (item.recipe_name, item.ingredient, item.unit, item.quantity)
                    )
                    super().get_connection.commit()
                    print(f"Saved ingredient: {item.ingredient} (Recipe: {item.recipe_name})")
                except Exception as e:
                    print("Error saving ingredient:", e)

            # Insert Steps
            for item in self.step_list:
                try:
                    super().get_cursor.execute(
                        """INSERT INTO Steps (recipe_name, step_order, step)
                           VALUES (?, ?, ?)""",
                        (item.recipe_name, item.step_order, item.step)
                    )
                    super().get_connection.commit()
                    print(f"Saved step {item.step_order} for recipe: {item.recipe_name}")
                except Exception as e:
                    print("Error saving step:", e)

        else:
            print("Save to DB aborted")