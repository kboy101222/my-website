# Generated by Django 4.2.17 on 2024-12-20 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipebook', '0005_recipe_recipe_type_alter_ingredient_measurement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='measurement',
            field=models.CharField(choices=[('gallon', 'Gallon(s)'), ('quart', 'Quart(s)'), ('mL', 'Milliliter(s)'), ('cup', 'Cup(s)'), ('tsp', 'Teaspoon(s)'), ('pint', 'Pint(s)'), ('tbsp', 'Tablespoon(s)'), ('lbs', 'Pound(s)'), ('floz', 'Fluid Ounce(s)'), ('g', 'Gram(s)')], max_length=200, verbose_name='measurement'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='recipe_type',
            field=models.CharField(choices=[('breakfast', 'Breakfast'), ('dessert', 'Dessert'), ('dinner', 'Dinner'), ('lunch', 'Lunch'), ('not_set', 'Not Set'), ('large_group', 'Large Groups/Parties')], max_length=20, verbose_name='recipe type'),
        ),
    ]
