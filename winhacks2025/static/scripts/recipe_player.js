// let recipe;

// async function loadRecipe() {
//     const recipeURL = `/recipes/${recipeName}/assets/data.json`;
//     const response = await fetch(recipeURL);
//     recipe = await response.json();
// }

// // let currentStage = "collection";
// loadRecipe();

const recipeURL = `/recipes/${recipeName}/assets/data.json`;

// fetch(recipeURL).then(function (response) {
//     response.json().then(function (data) {
//         recipe = data;
//         console.log(recipe);
//     })
// })

function initialize(data) {
    fetch(recipeURL).then(function (response) {
        response.json().then(function (recv) {
            data.recipe = recv;
            console.log(recv);

            let items = {}
            data.recipe.ingredients.forEach(element => {
                items[element] = false;
            });

            data.currentCards.push(
                {
                    id: data.cardCounter,
                    type: "collect",
                    items: items
                }
            )
            data.cardCounter++;
        })
    })


}

function addCard(data) {
    let step = data.recipe.steps[data.currentStep];
    data.currentCards.push(
        {
            id: data.cardCounter,
            type: 'step',
            text: step.instruction
        }
    );
    data.currentStep++;
    data.cardCounter++;
}

function collectableClick(data) {
    data.card.items[data.item] = !data.card.items[data.item];
    if (Object.values(data.card.items).every((a) => a)) {
        data.offscreen = true;
        setTimeout(() => nextCard(data), 300);
    }
}

function nextCard(data) {
    data.currentCards.splice(data.index, 1);
    addCard(data);
}

function stepSubmit(data) {
    data.offscreen = true;
    setTimeout(() => nextCard(data), 300);
}