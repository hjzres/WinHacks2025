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
            "SELECT * FROM 'Users' WHERE Id = ?",
            (user_id,),
        ).fetchone()
        
        if user_query is None:
            return None
        return cls(*user_query)
    


