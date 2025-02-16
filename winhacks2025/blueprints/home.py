from flask import Blueprint, render_template

from winhacks2025.database import Recipe, User, get_cursor

home = Blueprint("home", __name__)


@home.route("/")
def home_page():
    cur = get_cursor()
    recipes = Recipe.return_all(cur)
    user = User.from_id(cur, 1)
    name = user.name
    level = user.level
    xp_remaining = user.xp - level * 250
    rank_number, rank_name = get_rank(level)
    rank = f"{rank_number} - {rank_name}"

    recipe_length = print(len(recipes))

    return render_template(
        "home.html",
        recipes=recipes,
        recipe_length=recipe_length,
        name=name,
        level=level,
        xp_remaining=xp_remaining,
        rank=rank,
    )


def get_rank(level):
    if level < 2:
        return ("I", "Bronze Bakers")
    elif level < 4:
        return ("II", "Silver Slicers")
    elif level < 8:
        return ("III", "Golden Grillers")
    elif level < 16:
        return ("IV", "Ruby Roasters")
    else:
        return ("V", "Diamond Dicers")
