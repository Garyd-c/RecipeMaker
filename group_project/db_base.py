import sqlite3

"""
FILE DESCRIPTION:
This file connects the inputs from the other files to the sqlite database and allows for CRUD operations to occur.

CONTENTS:
    __init__(self,db_name):
        Collects the database file name.
        Starts the connection to the database.

    connect(self):
        The function to start the connection to the database.
        This connects to the database. Done through the .connect() method.
        This sets things up to write SQL. Done through the .cursor() method.

    execute_script(self, sql_string):
        # For executing multiple SQL statements (DROP, SELECT, CREATE, etc.). Good for batches of code.

    @property
        The @property is a decorator that will make the 'get_cursor' look like an attribute.

    get_cursor(self):
        get_cursor will allow us to write SQL code.
        This can be used for executing a single SQL statement with the .execute().
        For example: DBbase.get_cursor.execute("SELECT ...")

    get_connection(self):
        This will be used to save a SQL statement, or close a database.
        To save this is the path: DBbase.get_connection.commit()

    reset_database(self):
        This function is a placeholder function. Since reseting a database will require a unique code,
        this function is defaulting the job to a subclass.

    close_db(self):
        This funciton will be used to close the database.
"""

class DBbase:

    _conn = None
    _cursor = None


    def __init__(self,db_name):
        self._db_name = db_name
        self.connect()

    
    def connect(self):
        self._conn = sqlite3.connect(self._db_name)
        self._cursor = self._conn.cursor()

    
    def execute_script(self, sql_string):
        self._cursor.executescript(sql_string)
    
    @property
    def get_cursor(self):
        return self._cursor


    @property
    def get_connection(self):
        return self._conn


    def reset_database(self):
        raise NotImplementedError("Must implement from the derived class")
    

    def close_db(self):
        self._conn.close()

"""//////////////////////////////////   CREATE DB   ////////////////////////////////////////////"""

# class CreateDB(DBbase):

#     def reset_database(self):
#         sql = """

#             DROP TABLE IF EXISTS ingredients;
#             DROP TABLE IF EXISTS recipes;
#             DROP TABLE IF EXISTS steps;

#             CREATE TABLE recipes (
#                 id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#                 name    TEXT NOT NULL,
#                 description TEXT
#             );

#             CREATE TABLE ingredients (
#                 id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#                 recipe_id INTEGER,
#                 ingredient  TEXT NOT NULL,
#                 unit    TEXT,
#                 quantity INTEGER,
#                 FOREIGN KEY (recipe_id) REFERENCES recipes(id)
#             );

#             CREATE TABLE steps (
#                 id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#                 recipe_id INTEGER,
#                 step_number INTEGER NOT NULL,
#                 step TEXT,
#                 FOREIGN KEY (recipe_id) REFERENCES recipes(id)
#             ); """

#         self.execute_script(sql)
#         print("Database has been reset.")


# createSql = CreateDB("recipedb.sqlite")
# createSql.reset_database()
# createSql.close_db()
# print("Completed")


# import db_base as db

# class Recipes(db.DBbase):

#     def __init__(self):
#         super().__init__("recipedb.sqlite")

#     def update(self, recipe_id, name):
#         try:
#             super().get_cursor.execute("update recipe set name = ? where id = ?;", (name, recipe_id))
#             super().get_connection.commit()
#             print(f"Update record to  {name} success!")
#         except Exception as e:
#             print("An error has occurred.", e)

#     def add(self, name):
#         try:
#             super().get_cursor.execute("insert or ignore into recipe (name) values(?);", (name,))
#             super().get_connection.commit()
#             print(f"Add {name} successfully")
#         except Exception as e:
#             print("An error has occurred.", e)

#     def delete(self, recipe_id):
#         try:
#             super().get_cursor.execute("DELETE FROM recipe WHERE id = ?;", (recipe_id,))
#             super().get_connection.commit()
#             print(f"Deleted recipe id {recipe_id} successfully")
#             return True
#         except Exception as e:
#             print("An error has occurred.", e)
#             return False

#     def fetch(self, id=None, recipe_name=None):
#         try:
#             if id is not None:
#                 return super().get_cursor.execute("SELECT * FROM recipe WHERE id = ?;", (id,)).fetchone()
#             elif recipe_name is not None:
#                 return super().get_cursor.execute("SELECT * FROM recipe WHERE name = ?;", (recipe_name,)).fetchone()
#             else:
#                 return super().get_cursor.execute("SELECT * FROM recipe;").fetchall()
#         except Exception as e:
#             print("An error has occurred.", e)
#             return False

#     def reset_database(self):
#         try:
#             sql = """

#                 DROP TABLE IF EXISTS ingredients;
#                 DROP TABLE IF EXISTS recipes;
#                 DROP TABLE IF EXISTS steps;

#                 CREATE TABLE recipes (
#                     id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#                     name    TEXT NOT NULL,
#                     description TEXT
#                 );

#                 CREATE TABLE ingredients (
#                     id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#                     recipe_id INTEGER,
#                     ingredient  TEXT NOT NULL,
#                     unit    TEXT,
#                     quantity INTEGER,
#                     FOREIGN KEY (recipe_id) REFERENCES recipes(id)
#                 );

#                 CREATE TABLE steps (
#                     id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#                     recipe_id INTEGER,
#                     step_number INTEGER NOT NULL,
#                     step TEXT,
#                     FOREIGN KEY (recipe_id) REFERENCES recipes(id)
#                 ); """
#             super().execute_script(sql)
#         except Exception as e:
#             print("An error occured.", e)
#         finally:
#             super().close_db()



# class Ingredients(Recipes):

#     def add_inv(self, name, unit, qty):
#         try:
#             super().add(name)
#         except Exception as e:
#             print("An error occurred in the recipe class", e)
#         else:
#             try:
#                 recipe_id = super().fetch(recipe_name=name)[0]
#                 if recipe_id is not None:
#                     super().get_cursor.execute("""INSERT INTO ingredients (recipe_id, unit, quantity)
#                      VALUES (?,?,?);""", (recipe_id, unit, qty))
#                     super().get_connection.commit()
#                     print(f"Ingredient {name} added successfully")
#                 else:
#                     raise Exception("The id of the ingredient name was not found")
#             except Exception as ex:
#                 print("An error occured in the ingredients class.", ex)

#     def update_inv(self,id,qty,price):
#         try:
#             super().get_cursor.execute("""UPDATE ingredients SET unit = ?, quantity = ? WHERE id = ?;""",
#                                        (qty, price, id))
#             super().get_connection.commit()
#             print("Updated ingredients record successfully")
#             return True
#         except Exception as e:
#             print("An error occurred", e)
#             return False

#     def delete_inv(self, recipe_id):
#         try:
#             recipe_id = self.fetch_inv(recipe_id)[1]
#             if recipe_id is not None :
#                 rsts = super().delete(recipe_id)
#                 super().get_connection.commit()

#                 if rsts == False:
#                     raise Exception("Delete method in recipe failed. Delete aborted.")

#         except Exception as e:
#             print("An error occurred", e)
#             return False
#         else:
#             try:
#                 super().get_cursor.execute("DELETE FROM ingredients WHERE id = ?;", (recipe_id,))
#                 super().get_connection.commit()
#                 return True
#             except Exception as e:
#                 print("An error occurred in ingredients delete", e)
#                 return False

#     def fetch_inv(self, id=None):
#         try:
#             if id is not None:
#                 retval = super().get_cursor.execute("""SELECT ingredients.id, r.name, recipe_id, ingredient, unit, quantity
#                 FROM ingredients JOIN recipe p on ingredients.recipe_id = p.id
#                 WHERE ingredients.id = ?;""", (id,)).fetchone()
#                 return retval
#             else:
#                 return super().get_cursor.execute("""SELECT ingredients.id, part_id, p.name, quantity, price
#                 FROM ingredients JOIN parts p on ingredients.part_id = p.id;""").fetchall()

#         except Exception as e:
#             print("An error occurred", e)
#             return False

#     def reset_database(self):
#         try:
#             sql = """
#                 DROP TABLE IF EXISTS ingredients;
                
#                 CREATE TABLE ingredients (
#                     id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#                     recipe_id INTEGER,
#                     ingredient  TEXT NOT NULL,
#                     unit    TEXT,
#                     quantity INTEGER,
#                     FOREIGN KEY (recipe_id) REFERENCES recipes(id)
#                 );
#             """
#             super().execute_script(sql)
#             print("Ingredient table successfully created")
#         except Exception as e:
#             print("An error occurred", e)
#         finally:
#             super().close_db()


# class Project:

#     def run(self):

#         inv_options = { "get": "Get all recipes",
#                         "getby": "Get recipes by Id",
#                         "update": "Update recipe",
#                         "add": "Add recipe",
#                         "delete": "Delete recipe",
#                         "reset": "Reset database",
#                         "exit": "Exit the program"
#                         }

#         print("Welcome to my inventory program, please choose a selection")
#         user_selection = str()
#         while user_selection != "exit":
#             print("*** Option List ***")
#             for option in inv_options.items():
#                 print(option)

#             user_selection = input("Select an option: ").lower()
#             ingredients = Ingredients()

#             if user_selection == "get":
#                 results = ingredients.fetch_inv()
#                 for item in results:
#                     print(item)
#                 input("Press return to continue")

#             elif user_selection == "getby":
#                 inv_id = input("Enter Ingredient Id: ")
#                 results = ingredients.fetch_inv(inv_id)
#                 print(results)
#                 input("Press return to continue")

#             elif user_selection == "update":
#                 results = ingredients.fetch_inv()
#                 for item in results:
#                     print(item)

#                 recipe_id = input("Enter Recipe Id: ")
#                 unit = input("Enter unit measurment: ")
#                 qty = input("Enter unit amount: ")
#                 ingredients.update_inv(recipe_id, unit, qty)
#                 print(ingredients.fetch_inv(inv_id))
#                 input("Press return to continue")


#             elif user_selection == "add":
#                 name = input("Enter ingredient name: ")
#                 unit = input("Enter unit measurment: ")
#                 qty = input("Enter unit amount: ")
#                 ingredients.add_inv(name, unit, qty)
#                 print("Done\n")
#                 input("Press return to continue")


#             elif user_selection == "delete":
#                 inv_id = input("Enter Ingredient Id: ")
#                 ingredients.delete_inv(inv_id)
#                 print("Done\n")
#                 input("Press return to continue")


#             elif user_selection == "reset":
#                 confirm = input("This will delete all records in recipes and ingredients, continue? (y/n) ").lower()
#                 if (confirm == "y"):
#                     ingredients.reset_database()
#                     recipes = Recipes()
#                     recipes.reset_database()
#                     print("Reset complete")
#                     input("Press return to continue")

#                 else:
#                     print("Reset aborted")
#                     input("Press return to continue")


#             else:
#                 if user_selection != "exit":
#                     print("Invalid selection, please try again\n")


# project = Project()
# project.run()