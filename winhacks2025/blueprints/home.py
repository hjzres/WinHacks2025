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
	if rank_number == "I":
		rank_colour = "#996600, #CC8800"
	elif rank_number == "II":
		rank_colour = "#C9C0BB, #838996"
	elif rank_number == "III":
		rank_colour = "#FFD500, #B39500"
	elif rank_number == "IV":
		rank_colour = "#FF8080, #FF5533"
	else:
		rank_colour = "#B9F2FF, #0099E6"
	
	recipe_length = print(len(recipes))
	
	return render_template("home.html", recipes=recipes, recipe_length=recipe_length, name=name, level=level, xp_remaining=xp_remaining, rank=rank, rank_colour=rank_colour)
	
def get_rank(level):
	if level < 2:
		return ("I", "Bronze Baker")
	elif level < 4:
		return ("II", "Silver Slicer")
	elif level < 8:
		return ("III", "Golden Griller")
	elif level < 16:
		return ("IV", "Ruby Roaster")
	else:
		return ("V", "Diamond Dicers")