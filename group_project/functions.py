import db_base as db

class Ingredient_list(db.DBbase):

    def __init__(self):
        super().__init__("recipedb.sqlite")

# Create
    # 1. Pull ingredients_id
    def add_ing(self,recipe_name,ingredient,unit,quantity):
        try:

            super().get_cursor.execute("INSERT OR IGNORE INTO Ingredients (recipe_name, ingredient, unit, quantity) values(?,?,?,?);", (recipe_name,ingredient,unit,quantity))
            super().get_connection.commit()
            print(f"Add {ingredient} successfully")
        except Exception as e:
            print("An error has occurred.", e)

# Retrieve
    def fetch_ing(self, id=None, recipe_name=None):
        try:
            if id is not None:
                return super().get_cursor.execute("SELECT * FROM Recipe WHERE id = ?;", (id,)).fetchone()
            elif recipe_name is not None:
                return super().get_cursor.execute("SELECT * FROM Recipe WHERE name = ?;", (recipe_name,)).fetchone()
            else:
                return super().get_cursor.execute("SELECT * FROM recipe;").fetchall()
        except Exception as e:
            print("An error has occurred.", e)
            return False

# Update
    def update_ing(self, recipe_id, name):
        try:
            super().get_cursor.execute("update recipe set name = ? where id = ?;", (name, recipe_id))
            super().get_connection.commit()
            print(f"Update record to  {name} success!")
        except Exception as e:
            print("An error has occurred.", e)

# Delete
    def delete_ing(self, recipe_id):
        try:
            super().get_cursor.execute("DELETE FROM recipe WHERE id = ?;", (recipe_id,))
            super().get_connection.commit()
            print(f"Deleted recipe id {recipe_id} successfully")
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

