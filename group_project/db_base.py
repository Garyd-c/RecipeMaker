import sqlite3

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

class RecipeDB(DBbase):

    def reset_database(self):
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

        self.execute_script(sql)
        print("Database has been reset.")


createSql = RecipeDB("recipedb.sqlite")
createSql.reset_database()
createSql.close_db()
print("Completed")