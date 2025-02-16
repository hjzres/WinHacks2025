from dataclasses import dataclass


@dataclass
class User:
    id: int
    name: str
    xp: int
    level: int

    @classmethod
    def from_id(cls, cur, user_id: int):
        user_query = cur.execute(
            "SELECT * FROM Users WHERE Id = ?",
            (user_id,),
        ).fetchone()

        if user_query is None:
            return None
        return cls(*user_query)

    def write(self, cur):
        inserted_tuple = (
            self.name,
            self.xp,
        )

        cur.execute(
            "INSERT INTO Users(Name, XP) VALUES (?, ?)",
            inserted_tuple,
        )

    def add_xp(self, cur, val: int):
        cur.execute("UPDATE Users SET XP = XP + ? WHERE Id = ?", (val, self.id))

        new_xp, new_level = cur.execute(
            "SELECT XP, Level FROM Users WHERE Id = ?",
            (self.id,),
        ).fetchone()

        self.xp = new_xp
        self.level = new_level

    @classmethod
    def search(cls, cur, name_snip: str):
        user_query = cur.execute(
            "SELECT * FROM Users WHERE Name LIKE ?", (name_snip + "%",)
        ).fetchall()
        user_list = []
        for i in range(len(user_query)):
            user_list.append(cls(*user_query[i]))
        return user_list

    @staticmethod
    def count(cur):
        return cur.execute("SELECT COUNT(*) FROM Users").fetchone()[0]
