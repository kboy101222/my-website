from django.contrib import admin
from django.forms import Textarea
from django.db import models

from .models import Recipe, Ingredient, RecipeStep

class IngredientsInline(admin.TabularInline):
    model = Ingredient
    extra = 2

class RecipeStepsInline(admin.TabularInline):
    model = RecipeStep
    extra = 2
    formfields_overrides = {
        models.CharField: {'widget': Textarea(attrs={'rows':20, 'cols':10})}
    }

class RecipeAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Recipe Info", {"fields": ["recipe_name", "date_added", "recipe_desc", "amt_served", "recipe_img"]}),
    ]
    inlines = [IngredientsInline, RecipeStepsInline] 

# Register your models here.
admin.site.register(Recipe, RecipeAdmin)