const openButton = document.getElementsByClassName('recipe');
const closeButton = document.getElementsByClassName('close')[0];
const modal = document.getElementsByClassName('modal')[0];

const modal_name = document.getElementById('modal-name');
const description = document.getElementById('modal-description');
const requirement = document.getElementById('modal-requirement');
const ingredients = document.getElementById('modal-ingredients');
const source = document.getElementById('modal-source');
const image = document.getElementById('modal-image');
const difficulty = document.getElementById('modal-difficulty');
const time = document.getElementById('modal-time');
const xp = document.getElementById('modal-xp');

image.src = "";

for (let i = 0; i < openButton.length; i++) {
	openButton[i].addEventListener('click', function() {
		modal.showModal();
		document.body.style.overflow = 'hidden';
		console.log(i);
		fetch('/recipes/' + openButton[i].dataset.name + "/assets/data.json").then(function(response) {
			response.json().then(function(data){
				modal_name.innerHTML = data.display_name;
				description.innerHTML = data.description;
				if(data.recipe_requirements != ""){
					requirement.innerHTML = "Requirements: " + data.recipe_requirements;
				} else {
					requirement.innerHTML = "";
				}
				let ingredientsList = "<div class='subtitle'> Ingredients: </div><ul>";
				data.ingredients.forEach(function(ingredient) {
					ingredientsList += `<li>${ingredient}</li>`;
				});
				ingredientsList += "</ul>";
				ingredients.innerHTML = ingredientsList;
				console.log(data.recipe_requirements);
				source.innerHTML = data.source;
				image.src = `/recipes/${data.name}/assets/Cover.jpg`;
				difficulty.innerHTML = "Difficulty: " + data.difficulty;
				time.innerHTML = "Average Time to make: " + data.total_time + " minutes";
				xp.innerHTML = "XP: " + data.xp_level;
			});
		});
	});
}

modal.addEventListener('close', function() {
	document.body.style.overflow = 'auto';
	modal_name.innerHTML = "";
	description.innerHTML = "";
	requirement.innerHTML = "";
	ingredients.innerHTML = "";
	source.innerHTML = "";
	image.src = "";
	difficulty.innerHTML = "";
	time.innerHTML = "";
	xp.innerHTML = "";
});

closeButton.addEventListener('click', function() {
	modal.close();
});