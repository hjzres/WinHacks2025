const recipe = await (
    await fetch(`/recipes/${recipeName}.json`)
).json();

console.log(recipe);