from config import CONN, CURSOR


class Song:
    def __init__(self, name, album):
        self.name = name
        self.album = album
        self.id = None
    
    @classmethod
    def create_table(self):
        sql= """
            CREATE TABLE IF NOT EXISTS songs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                album TEXT
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO songs (name, album)
            VALUES (?, ?)
        """
        CURSOR.execute(sql, (self.name, self.album))
        self.id = CURSOR.execute("SELECT last_insert_rowid() FROM songs").fetchone()[0]
        CONN.commit()
    
    @classmethod
    def create(cls, name, album):
        song = Song(name, album)
        song.save()
        return song



# song = Song.create("Zablon", "Mwema")
# print(song.name)
# print(song.album)
