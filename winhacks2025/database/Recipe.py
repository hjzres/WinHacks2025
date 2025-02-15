from dataclasses import dataclass

@dataclass
class Recipe:
    id: int
    name: str
    official: bool
    difficulty: str
    time: int
    xp_amount:int
    recipe: str

    @classmethod
    def from_id(cls, cur, recipe_id: int):
        
        recipe_query = cur.execute(
            "SELECT * FROM Recipes WHERE Id = ?",
            (recipe_id,),
        ).fetchone()
        
        if recipe_query is None:
            return None
        return cls(*recipe_query)