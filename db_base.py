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


    def _reset_database(self):
        raise NotImplementedError("Must implement from the derived class")
    

    def close_db(self):
        self._conn.close()

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