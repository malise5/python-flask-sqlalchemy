from ast import Pass
import sqlite3


CONN = sqlite3.connect('resources.db')
CURSOR = CONN.cursor()

class Owner:
    Pass