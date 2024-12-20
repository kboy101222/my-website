from django.shortcuts import render, get_object_or_404

from .models import Recipe, Ingredient, RecipeStep

# Create your views here.
def index(request):
    return render(request, template_name="recipebook/index.html")

def recipe_list(request):
    recipes = Recipe.objects.order_by("recipe_name")
    icons_list = {
    "breakfast": "brightness-alt-high-fill",
    "lunch"    : "brightness-high-fill",
    "dinner"   : "moon-stars-fill",
    }
    return render(request, template_name="recipebook/recipe_list.html", context={"recipe_list": recipes, "icons_list":icons_list})

def recipe(request, recipe_id):
    recipe_info = get_object_or_404(Recipe, pk=recipe_id)
    ingredients = Ingredient.objects.filter(recipe__exact=recipe_id)
    return render(request, template_name="recipebook/recipe.html", context={"recipe_info": recipe_info, "ingredients":ingredients,})