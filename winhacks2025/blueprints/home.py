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
	if level < 2:
		rank = "I"
	elif level < 4:
		rank = "II"
	elif level < 8:
		rank = "III"
	elif level < 16:
		rank = "IV"
	else:
		rank = "VI"
	
	print(recipes)
	recipe_length = print(len(recipes))
	
	return render_template("home.html", recipes=recipes, recipe_length=recipe_length, name=name, level=level, xp_remaining=xp_remaining, rank=rank)
