from django.db import models
from django.utils import timezone

MEASUREMENTS = {
    ("tsp"   , "Teaspoon(s)"),
    ("tbsp"  , "Tablespoon(s)"),
    ("floz"  , "Fluid Ounce(s)"),
    ("cup"   , "Cup(s)"),
    ("pint"  , "Pint(s)"),
    ("quart" , "Quart(s)"),
    ("gallon", "Gallon(s)"),
    ("lbs"   , "Pound(s)"),
    ("g"     , "Gram(s)"),
    ("mL"    , "Milliliter(s)"),
    ("amt"   , "Amount"),
    ("stick" , "Stick"),
    ("not_set", "None")
}

RECIPE_TYPES = {
    ("breakfast", "Breakfast"), # "brightness-alt-high-fill"
    ("lunch", "Lunch"), # "brightness-high-fill"
    ("dinner", "Dinner"), # "moon-stars-fill"
    ("dessert", "Dessert"), # "box2-heart-fill"
    ("large_group", "Large Groups/Parties"), # "people-fill"
    ("holiday", "Holiday"), # "snow"
    ("snack", "Snack"), # "person-arms-up"
    ("not_set", "Not Set"),
}

# Create your models here.
class Recipe(models.Model):
    recipe_name = models.CharField(max_length=200)
    date_added = models.DateField("date published", default=timezone.now)
    recipe_desc = models.CharField("recipe description", max_length=400)
    amt_served = models.IntegerField("amount served", default=1)
    recipe_img = models.ImageField("recipe image", upload_to="recipe_images", null=True, blank=True)
    recipe_type = models.CharField("recipe type", max_length=20, choices=RECIPE_TYPES, default="not_set")

    def __str__(self):
        return self.recipe_name
    

class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient_name = models.CharField("name", max_length=200)
    amount = models.FloatField("amount", default=1)
    measurement = models.CharField("measurement", max_length=200, choices=MEASUREMENTS)

    # def __str__(self):
    #     recipe_fraction = self.amount.as_integer_ratio()
    #     if recipe_fraction[1] == 1:
    #         return str(recipe_fraction[0]) + " " + self.measurement + " of " + self.ingredient_name
    #     else:
    #         return str(recipe_fraction[0]) + "/" + str(recipe_fraction[1]) + " " + self.measurement + " of " + self.ingredient_name

class RecipeStep(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    description = models.CharField("step", max_length=1000)