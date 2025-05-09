import sqlite3

CONN = sqlite3.connect('resources.db')
CURSOR = CONN.cursor()

class Pet:
    def __init__(self, name, species,breed, temperament, id=None):
        self.id = id
        self.name = name
        self.species = species
        self.breed = breed
        self.temperament = temperament

    
    @classmethod
    def create_table(cls):
        CURSOR.execute('''
            CREATE TABLE IF NOT EXISTS pets (
                id INTEGER PRIMARY KEY,
                name TEXT,
                species TEXT,
                breed TEXT,
                temperament TEXT
            )
        ''')
        CONN.commit()
    
    @classmethod
    def drop_table(cls):
        CURSOR.execute('DROP TABLE IF EXISTS pets')
        CONN.commit()


    def save(self):
        if self.id is None:
            CURSOR.execute('''
                INSERT INTO pets (name, species, breed, temperament)
                VALUES (?, ?, ?, ?)
            ''', (self.name, self.species, self.breed, self.temperament))
            self.id = CURSOR.lastrowid
        else:
            CURSOR.execute('''
                UPDATE pets
                SET name = ?, species = ?, breed = ?, temperament = ?
                WHERE id = ?
            ''', (self.name, self.species, self.breed, self.temperament, self.id))
        CONN.commit()
    
    @classmethod
    def create(cls, name, species, breed, temperament):
        pet = cls(name, species, breed, temperament)
        pet.save()
        return pet
    
    @classmethod
    def new_from_db(cls, row):
        pet = cls(
            id=row[0],
            name=row[1],
            species=row[2],
            breed=row[3],
            temperament=row[4]
        )
        return pet
    
    @classmethod
    def get_all(cls):
        CURSOR.execute('SELECT * FROM pets')
        rows = CURSOR.fetchall()
        return [cls.new_from_db(row) for row in rows]
    
    