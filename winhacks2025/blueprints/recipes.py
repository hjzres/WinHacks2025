from flask import Blueprint, render_template, send_from_directory

recipes = Blueprint("recipes", __name__)


@recipes.route("/<string:recipe_name>/play")
def recipe_player(recipe_name: str):
    return render_template("recipe_player.html", recipe_name=recipe_name)


@recipes.route("/<string:recipe_name>.json")
def get_recipe(recipe_name: str):
    print(recipe_name)
    return send_from_directory("../recipes/", f"{recipe_name}.json")
