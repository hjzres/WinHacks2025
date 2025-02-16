from flask import Blueprint, render_template

from winhacks2025.database import Recipe, get_cursor

home = Blueprint("home", __name__)


@home.route("/")
def home_page():
	cur = get_cursor()
	recipes = Recipe.return_all(cur)
	
	print(recipes)
	recipe_length = print(len(recipes))
	
	return render_template("home.html", recipes=recipes, recipe_length=recipe_length)
