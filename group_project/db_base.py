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

class RecipeCreate(DBbase):

    def __init__(self):
        super().__init__("recipedb.sqlite")

    def reset_database(self):
        sql = """
            DROP TABLE IF EXISTS Recipe;
            DROP TABLE IF EXISTS Ingredients;
            DROP TABLE IF EXISTS Steps;

            CREATE TABLE Recipe (
                id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                name    TEXT,
                description TEXT
            );

            CREATE TABLE Ingredients (
                id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                ingredient  TEXT,
                unit    TEXT,
                unit_amount INTEGER
            );

            CREATE TABLE Steps (
                id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                step_number INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                step TEXT
            ); """

        super().execute_script(sql)




    def load_database(self,fname):
        stuff = ET.parse(fname)
        all_item = stuff.findall("dict/dict/dict")
        print("Dict count:", len(all_item))

        for entry in all_item:
            if func.lookup(entry,"Name") is None: continue

            name = func.lookup(entry,"Name")
            artist = func.lookup(entry,"Artist")
            album = func.lookup(entry,"Album")
            count = func.lookup(entry,"Play Count")
            rating = func.lookup(entry,"Rating")
            length = func.lookup(entry,"Total Time")

            if name is None or artist is None or album is None:
                continue

            print(name, artist, album, count, rating, length)

            cur = super().get_cursor

            cur.execute('''INSERT OR IGNORE INTO Artist (name)
                VALUES ( ? )''', (artist,))

            cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist,))
            artist_id = cur.fetchone()[0]

            cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id)
                VALUES ( ?, ? )''', (album, artist_id))

            cur.execute('SELECT id FROM Album WHERE title = ? ', (album,))
            album_id = cur.fetchone()[0]

            cur.execute('''INSERT OR REPLACE INTO Track
                (title, album_id, len, rating, count)
                VALUES ( ?, ?, ?, ?, ? )''',
                        (name, album_id, length, rating, count))

            super().get_connection.commit()



createSql = RecipeCreate()
createSql.reset_database("recipedb.sqlite")
createSql.close_db()
print("Completed")