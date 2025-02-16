// let recipe;

// async function loadRecipe() {
//     const recipeURL = `/recipes/${recipeName}/assets/data.json`;
//     const response = await fetch(recipeURL);
//     recipe = await response.json();
// }

// // let currentStage = "collection";
// loadRecipe();

const recipeURL = `/recipes/${recipeName}/assets/data.json`;
const recipePlayURL = `/recipes/${recipeName}/play`;

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

function addCard(data, card) {
    card.id = data.cardCounter;
    data.currentCards.push(card);
    data.cardCounter++;
}

function endCard(data, resp) {
    console.log(resp);
    addCard(data, {
        type: 'finish',
        resp: resp
    })
}

function nextStep(data) {
    if (data.currentStep >= data.recipe.steps.length){
        
        fetch(recipePlayURL, {
            method: 'POST',
            body: JSON.stringify({})
          }).then(function(response) {
            response.json().then(function(recv) {
                endCard(data, recv);
            })
          })

        return;
    }
    let step = data.recipe.steps[data.currentStep];

    if (step.timer != null) {
        addCard(data, {
            type: 'timer',
            time: step.timer
        })
    }

    addCard(data, {
        type: 'step',
        text: step.instruction
    })
    data.currentStep++;
}

function nextCard(data) {
    data.currentCards.splice(data.index, 1);
    nextStep(data);
}

function collectableClick(data) {
    data.card.items[data.item] = !data.card.items[data.item];
    if (Object.values(data.card.items).every((a) => a)) {
        data.offscreen = true;
        setTimeout(() => nextCard(data), 300);
    }
}

function stepSubmit(data) {
    data.offscreen = true;
    setTimeout(() => nextCard(data), 300);
}

function formatTime(time) {
    let left = time;

    let mins = String(Math.floor(left/60000));
    left %= 60000;

    let secs = String(Math.floor(left/1000)).padStart(2, "0");

    return `${mins}:${secs}`
}

function initTimer(data) {
    setInterval(function() {
        let delta = Date.now() - data.startTime;
        if (data.running) {
            data.timeLeft = data.lastTime - delta;
        }
    }, 10);
}

function removeCard(data) {
    data.offscreen = true;
    setTimeout(() => data.currentCards.splice(data.index, 1), 300);
}