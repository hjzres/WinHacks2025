from string import ascii_lowercase, digits

from flask import Blueprint, abort, render_template, send_from_directory

recipes = Blueprint("recipes", __name__)

allowed_characters = set(ascii_lowercase + digits + "_")


def validate_recipe_name(name: str) -> bool:
    return all(char in allowed_characters for char in name)


@recipes.route("/<string:recipe_name>/play")
def recipe_player(recipe_name: str):
    return render_template("recipe_player.html", recipe_name=recipe_name)


@recipes.route("/<string:recipe_name>/assets/<path:file>")
def get_recipe(recipe_name: str, file: str):
    print(recipe_name, file)
    if not validate_recipe_name(recipe_name):
        abort(400)
    return send_from_directory(f"../recipes/{recipe_name}", file)
