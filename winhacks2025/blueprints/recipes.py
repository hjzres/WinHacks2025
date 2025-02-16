from string import ascii_lowercase, digits

from flask import (
    Blueprint,
    abort,
    jsonify,
    render_template,
    request,
    send_from_directory,
)

from winhacks2025.database import Recipe, User, get_cursor
from winhacks2025.database.cursor import get_db

recipes = Blueprint("recipes", __name__)

allowed_characters = set(ascii_lowercase + digits + "_")


def validate_recipe_name(name: str) -> bool:
    return all(char in allowed_characters for char in name)


@recipes.route("/<string:recipe_name>/play", methods=["GET", "POST"])
def recipe_player(recipe_name: str):
    if request.method == "GET":
        return render_template("recipe_player.html", recipe_name=recipe_name)
    elif request.method == "POST":
        cur = get_cursor()
        rec = Recipe.from_name(cur, recipe_name)
        usr = User.from_id(cur, 1)
        old_xp = usr.xp
        old_level = usr.level
        usr.add_xp(cur, rec.xp_amount)

        get_db().commit()
        return jsonify(
            {
                "old_xp": old_xp,
                "new_xp": usr.xp,
                "old_level": old_level,
                "new_level": usr.level,
            }
        )


@recipes.route("/<string:recipe_name>/assets/<path:file>")
def get_recipe(recipe_name: str, file: str):
    print(recipe_name, file)
    if not validate_recipe_name(recipe_name):
        abort(400)
    return send_from_directory(f"../recipes/{recipe_name}", file)
