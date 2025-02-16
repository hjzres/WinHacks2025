from dataclasses import dataclass, field


@dataclass
class Recipe:
    id: int
    display_name: str
    name: str
    official: bool
    difficulty: str
    time: int
    xp_amount: int
    recipe: str = field(repr=False)

    @classmethod
    def from_id(cls, cur, recipe_id: int):
        recipe_query = cur.execute(
            "SELECT * FROM Recipes WHERE Id = ?",
            (recipe_id,),
        ).fetchone()

        if recipe_query is None:
            return None
        return cls(*recipe_query)

    def write(self, cur):
        inserted_tuple = (
            self.display_name,
            self.name,
            self.official,
            self.difficulty,
            self.time,
            self.xp_amount,
            self.recipe,
        )

        cur.execute(
            "INSERT INTO Recipes(DisplayName, Name, Offical, Difficulty, Time, XP_Amount, Recipe) "
            "VALUES (?, ?, ?, ?, ?, ?)",
            inserted_tuple,
        )

    @classmethod
    def search(cls, cur, name_snip: str):
        recipe_query = cur.execute(
            "SELECT * FROM Recipes WHERE Name LIKE ?", (name_snip + "%",)
        ).fetchall()
        recipe_list = []
        for i in range(len(recipe_query)):
            recipe_list.append(cls(*recipe_query[i]))
        return recipe_list

    @staticmethod
    def count(cur):
        return cur.execute("SELECT COUNT(*) FROM Recipe").fetchone()[0]

    @classmethod
    def return_all(cls, cur):
        recipe_query = cur.execute("SELECT * FROM Recipes").fetchall()
        recipe_list = []
        for i in range(len(recipe_query)):
            recipe_list.append(cls(*recipe_query[i]))
        return recipe_list
