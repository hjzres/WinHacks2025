from flask import Blueprint, render_template

from winhacks2025.database import Recipe

home = Blueprint("home", __name__)


@home.route("/")
def home_page():
	r = Recipe.return_all()
	print(r)
	return render_template("home.html")
