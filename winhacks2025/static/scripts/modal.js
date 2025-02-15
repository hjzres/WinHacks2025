const openButton = document.getElementsByClassName('recipe');
const closeButton = document.getElementsByClassName('close')[0];
const modal = document.getElementsByClassName('modal')[0];

console.log(document.getElementsByClassName('close'));

console.log(closeButton);

for (let i = 0; i < openButton.length; i++) {
	openButton[i].addEventListener('click', function() {
		modal.showModal();
		console.log('1');
		document.body.style.overflow = 'hidden';
	});
}

modal.addEventListener('close', function() {
	document.body.style.overflow = 'auto';
});

closeButton.addEventListener('click', function() {
	modal.close();
});