from recipies.models import Recipe

def add_ingredient_to_recipe(recipe: Recipe, ingredient: dict[str, str]):
    ingredients = recipe.ingredients or []
    ingredients.append(ingredient)
    recipe.ingredients = ingredients
    recipe.save()