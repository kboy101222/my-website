from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, template_name="recipebook/index.html")

def recipe_list(request):
    return render(request, template_name="recipebook/recipe_list.html")

def recipe(request):
    return render(request, template_name="recipebook/recipe.html")