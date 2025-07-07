import db_base as db

class Recipes(db.DBbase):

    def __init__(self):
        super().__init__("recipedb.sqlite")

    def update(self, recipe_id, name):
        try:
            super().get_cursor.execute("update recipe set name = ? where id = ?;", (name, recipe_id))
            super().get_connection.commit()
            print(f"Update record to  {name} success!")
        except Exception as e:
            print("An error has occurred.", e)

    def add(self, name):
        try:
            super().get_cursor.execute("insert or ignore into recipe (name) values(?);", (name,))
            super().get_connection.commit()
            print(f"Add {name} successfully")
        except Exception as e:
            print("An error has occurred.", e)

    def delete(self, recipe_id):
        try:
            super().get_cursor.execute("DELETE FROM recipe WHERE id = ?;", (recipe_id,))
            super().get_connection.commit()
            print(f"Deleted recipe id {recipe_id} successfully")
            return True
        except Exception as e:
            print("An error has occurred.", e)
            return False

    def fetch(self, id=None, recipe_name=None):
        try:
            if id is not None:
                return super().get_cursor.execute("SELECT * FROM recipe WHERE id = ?;", (id,)).fetchone()
            elif recipe_name is not None:
                return super().get_cursor.execute("SELECT * FROM recipe WHERE name = ?;", (recipe_name,)).fetchone()
            else:
                return super().get_cursor.execute("SELECT * FROM recipe;").fetchall()
        except Exception as e:
            print("An error has occurred.", e)
            return False

    def reset_database(self):
        try:
            sql = """

                DROP TABLE IF EXISTS ingredients;
                DROP TABLE IF EXISTS recipes;
                DROP TABLE IF EXISTS steps;

                CREATE TABLE recipes (
                    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                    name    TEXT NOT NULL,
                    description TEXT
                );

                CREATE TABLE ingredients (
                    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                    recipe_id INTEGER,
                    ingredient  TEXT NOT NULL,
                    unit    TEXT,
                    quantity INTEGER,
                    FOREIGN KEY (recipe_id) REFERENCES recipes(id)
                );

                CREATE TABLE steps (
                    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                    recipe_id INTEGER,
                    step_number INTEGER NOT NULL,
                    step TEXT,
                    FOREIGN KEY (recipe_id) REFERENCES recipes(id)
                ); """
            super().execute_script(sql)
        except Exception as e:
            print("An error occured.", e)
        finally:
            super().close_db()



class Ingredients(Recipes):

    def add_inv(self, name, unit, qty):
        try:
            super().add(name)
        except Exception as e:
            print("An error occurred in the recipe class", e)
        else:
            try:
                recipe_id = super().fetch(recipe_name=name)[0]
                if recipe_id is not None:
                    super().get_cursor.execute("""INSERT INTO ingredients (recipe_id, unit, quantity)
                     VALUES (?,?,?);""", (recipe_id, unit, qty))
                    super().get_connection.commit()
                    print(f"Ingredient {name} added successfully")
                else:
                    raise Exception("The id of the ingredient name was not found")
            except Exception as ex:
                print("An error occured in the ingredients class.", ex)

    def update_inv(self,id,qty,price):
        try:
            super().get_cursor.execute("""UPDATE ingredients SET unit = ?, quantity = ? WHERE id = ?;""",
                                       (qty, price, id))
            super().get_connection.commit()
            print("Updated ingredients record successfully")
            return True
        except Exception as e:
            print("An error occurred", e)
            return False

    def delete_inv(self, recipe_id):
        try:
            recipe_id = self.fetch_inv(recipe_id)[1]
            if recipe_id is not None :
                rsts = super().delete(recipe_id)
                super().get_connection.commit()

                if rsts == False:
                    raise Exception("Delete method in recipe failed. Delete aborted.")

        except Exception as e:
            print("An error occurred", e)
            return False
        else:
            try:
                super().get_cursor.execute("DELETE FROM ingredients WHERE id = ?;", (recipe_id,))
                super().get_connection.commit()
                return True
            except Exception as e:
                print("An error occurred in ingredients delete", e)
                return False

    def fetch_inv(self, id=None):
        try:
            if id is not None:
                retval = super().get_cursor.execute("""SELECT ingredients.id, r.name, recipe_id, ingredient, unit, quantity
                FROM ingredients JOIN recipe p on ingredients.recipe_id = p.id
                WHERE ingredients.id = ?;""", (id,)).fetchone()
                return retval
            else:
                return super().get_cursor.execute("""SELECT ingredients.id, part_id, p.name, quantity, price
                FROM ingredients JOIN parts p on ingredients.part_id = p.id;""").fetchall()

        except Exception as e:
            print("An error occurred", e)
            return False

    def reset_database(self):
        try:
            sql = """
                DROP TABLE IF EXISTS ingredients;
                
                CREATE TABLE ingredients (
                    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                    recipe_id INTEGER,
                    ingredient  TEXT NOT NULL,
                    unit    TEXT,
                    quantity INTEGER,
                    FOREIGN KEY (recipe_id) REFERENCES recipes(id)
                );
            """
            super().execute_script(sql)
            print("Ingredient table successfully created")
        except Exception as e:
            print("An error occurred", e)
        finally:
            super().close_db()


class Project:

    def run(self):

        inv_options = { "get": "Get all recipes",
                        "getby": "Get recipes by Id",
                        "update": "Update recipe",
                        "add": "Add recipe",
                        "delete": "Delete recipe",
                        "reset": "Reset database",
                        "exit": "Exit the program"
                        }

        print("Welcome to my inventory program, please choose a selection")
        user_selection = str()
        while user_selection != "exit":
            print("*** Option List ***")
            for option in inv_options.items():
                print(option)

            user_selection = input("Select an option: ").lower()
            ingredients = Ingredients()

            if user_selection == "get":
                results = ingredients.fetch_inv()
                for item in results:
                    print(item)
                input("Press return to continue")

            elif user_selection == "getby":
                inv_id = input("Enter Ingredient Id: ")
                results = ingredients.fetch_inv(inv_id)
                print(results)
                input("Press return to continue")

            elif user_selection == "update":
                results = ingredients.fetch_inv()
                for item in results:
                    print(item)

                recipe_id = input("Enter Recipe Id: ")
                unit = input("Enter unit measurment: ")
                qty = input("Enter unit amount: ")
                ingredients.update_inv(recipe_id, unit, qty)
                print(ingredients.fetch_inv(inv_id))
                input("Press return to continue")


            elif user_selection == "add":
                name = input("Enter ingredient name: ")
                unit = input("Enter unit measurment: ")
                qty = input("Enter unit amount: ")
                ingredients.add_inv(name, unit, qty)
                print("Done\n")
                input("Press return to continue")


            elif user_selection == "delete":
                inv_id = input("Enter Ingredient Id: ")
                ingredients.delete_inv(inv_id)
                print("Done\n")
                input("Press return to continue")


            elif user_selection == "reset":
                confirm = input("This will delete all records in recipes and ingredients, continue? (y/n) ").lower()
                if (confirm == "y"):
                    ingredients.reset_database()
                    recipes = Recipes()
                    recipes.reset_database()
                    print("Reset complete")
                    input("Press return to continue")

                else:
                    print("Reset aborted")
                    input("Press return to continue")


            else:
                if user_selection != "exit":
                    print("Invalid selection, please try again\n")


project = Project()
project.run()