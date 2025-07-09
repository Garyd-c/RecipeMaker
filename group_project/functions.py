import db_base as db



#////////////////////////////////// Ingredients Class //////////////////////////////////#


class IngredientList(db.DBbase):

    def __init__(self):
        super().__init__("recipedb.sqlite")

# Create
    def add_ing(self,recipe_name,ingredient,unit=None,quantity=1):
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0.")
        try:
            super().get_cursor.execute("INSERT OR IGNORE INTO Ingredients (recipe_name,ingredient,unit,quantity) values(?,?,?,?);", (recipe_name,ingredient,unit,quantity))
            super().get_connection.commit()
            print(f"Add {ingredient} successfully")
        except Exception as e:
            print("An error has occurred.", e)

# Retrieve
    def fetch_ing(self, ingredient_id=None, recipe_name=None):
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

# # Update
#     def update_ing(self, ingredient_id, recipe_name):
#         try:
#             super().get_cursor.execute("UPDATE Ingredients SET recipe_name = ? where id = ?;", (ingredient_id, recipe_name))
#             super().get_connection.commit()
#             print(f"Update record to  {recipe_name} success!")
#         except Exception as e:
#             print("An error has occurred.", e)

# Delete
    def delete_ing(self, ingredient_id=None, recipe_name=None):
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



# ing_list = IngredientList()
# ing_list.add_ing("Hot Sauce","Water","Cup",2)
# ing_list.add_ing("Hot Sauce","Peppers",None,2)
# ing_list.add_ing("gravy","burnaise","packets",1)

# print(ing_list.fetch_ing(None,None))

# ing_list.delete_ing(None,"Hot Sauce")

# print(ing_list.fetch_ing(None,None))


#///////////////////////////////// Steps Class ///////////////////////////////////////#


class StepsList(db.DBbase):

    def __init__(self):
        super().__init__("recipedb.sqlite")

# Create
    def add_ing(self,recipe_name,step):
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
    def fetch_ing(self, ingredient_id=None, recipe_name=None):
        try:
            # View an individual step:

            if ingredient_id is not None:
                return super().get_cursor.execute("SELECT * FROM Ingredients WHERE ingredient_id = ?;", (ingredient_id,)).fetchone()
            
            # View the list of recipe steps:

            elif recipe_name is not None:
                return super().get_cursor.execute("SELECT * FROM Ingredients WHERE recipe_name = ?;", (recipe_name,)).fetchall()
            
            # View the full DB of ingredients

            else:
                return super().get_cursor.execute("SELECT * FROM Ingredients;").fetchall()

        except Exception as e:
            print("An error has occurred.", e)
            return False

# Update
    def update_ing(self, ingredient_id, recipe_name):
        try:
            super().get_cursor.execute("UPDATE Ingredients SET recipe_name = ? where id = ?;", (ingredient_id, recipe_name))
            super().get_connection.commit()
            print(f"Update record to  {recipe_name} success!")
        except Exception as e:
            print("An error has occurred.", e)

# Delete
    def delete_ing(self, ingredient_id=None, recipe_name=None):
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
    def add_ing(self,recipe_name,step):
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
    def fetch_ing(self, ingredient_id=None, recipe_name=None):
        try:
            # View an individual step:

            if ingredient_id is not None:
                return super().get_cursor.execute("SELECT * FROM Ingredients WHERE ingredient_id = ?;", (ingredient_id,)).fetchone()
            
            # View the list of recipe steps:

            elif recipe_name is not None:
                return super().get_cursor.execute("SELECT * FROM Ingredients WHERE recipe_name = ?;", (recipe_name,)).fetchall()
            
            # View the full DB of ingredients

            else:
                return super().get_cursor.execute("SELECT * FROM Ingredients;").fetchall()

        except Exception as e:
            print("An error has occurred.", e)
            return False

# Update
    def update_ing(self, ingredient_id, recipe_name):
        try:
            super().get_cursor.execute("UPDATE Ingredients SET recipe_name = ? where id = ?;", (ingredient_id, recipe_name))
            super().get_connection.commit()
            print(f"Update record to  {recipe_name} success!")
        except Exception as e:
            print("An error has occurred.", e)

# Delete
    def delete_ing(self, ingredient_id=None, recipe_name=None):
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
        except Exception as e:
            print("An error occured.", e)
        finally:
            super().close_db()
