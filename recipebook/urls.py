from django.urls import include, path

from . import views

app_name="recipebook"
urlpatterns = [
    # index
    path("", views.index, name="index"),
    # recipe list
    path("recipe_list/", views.recipe_list, name="recipe_list"),
    # specific recipe
    path("recipe_list/<int:recipe_id>", views.recipe, name="recipe")
]
