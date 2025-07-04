import sqlite3

class DBbase:

    _conn = None
    _cursor = None

    # Collects the database file name.
    # Starts the connection to the database.
    def __init__(self,db_name):
        self._db_name = db_name
        self.connect()

    # The function to start the connection to the database.
    def connect(self):
        # This connects to the database. Done through the .connect() method.
        self._conn = sqlite3.connect(self._db_name)
        # This sets things up to write SQL. Done through the .cursor() method.
        self._cursor = self._conn.cursor()

    # For executing multiple SQL statements (DROP, SELECT, CREATE, etc.). Good for batches of code.
    def execute_script(self, sql_string):
        self._cursor.executescript(sql_string)
    
    # get_cursor will allow us to write SQL code.
    # This can be used for executing a single SQL statement with the .execute().
    # For example: DBbase.get_cursor.execute("SELECT ...")
    # The @property is a decorator that will make the 'get_cursor' look like an attribute.
    @property
    def get_cursor(self):
        return self._cursor

    # This will be used to save a SQL statement, or close a database.
    # To save this is the path: DBbase.get_connection.commit()
    @property
    def get_connection(self):
        return self._conn

    # This function is a placeholder function. Since reseting a database will require a unique code,
    # this function is defaulting the job to a subclass.
    def reset_database(self):
        raise NotImplementedError("Must implement from the derived class")
    
    # This funciton will be used to close the database.
    def close_db(self):
        self._conn.close()

"""//////////////////////////////////   CREATE DB   ////////////////////////////////////////////"""

class CreateDB(DBbase):

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


# createSql = CreateDB("recipedb.sqlite")
# createSql.reset_database()
# createSql.close_db()
# print("Completed")