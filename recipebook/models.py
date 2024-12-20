from django.db import models

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
}

# Create your models here.
class Recipe(models.Model):
    recipe_name = models.CharField(max_length=200)
    date_added = models.DateField("date published")
    recipe_desc = models.CharField("recipe description", max_length=400)
    amt_served = models.IntegerField("amount served", default=1)
    recipe_img = models.ImageField("recipe image", upload_to="recipe_images", null=True, blank=True)

    def __str__(self):
        return self.recipe_name
    

class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient_name = models.CharField("name", max_length=200)
    amount = models.IntegerField("amount", default=1)
    measurement = models.CharField("measurement", max_length=200, choices=MEASUREMENTS)

class RecipeStep(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    description = models.CharField("step", max_length=1000)