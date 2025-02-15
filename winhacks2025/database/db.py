from dataclasses import dataclass
import sqlite3;

# CHANGE THIS AFTER TO THE FLASK CONNECTION
con = sqlite3.connect("../../recipes.db")
cur = con.cursor()

