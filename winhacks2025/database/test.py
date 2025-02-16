import sqlite3

from Recipe import Recipe
from User import User

con = sqlite3.connect("./recipes.db")
cur = con.cursor()


user1 = User.from_id(cur, 1)
print(user1.id, user1.name, user1.xp, user1.level)

fafoof = Recipe.return_all(cur)