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
				requirement.innerHTML = data.recipe_requirements;
				ingredients.innerHTML = data.ingredients;
				source.innerHTML = data.source;
				image.src = `/recipes/${data.name}/assets/Cover.jpg`;
				difficulty.innerHTML = data.difficulty;
				time.innerHTML = data.total_time;
				xp.innerHTML = data.xp_level;
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