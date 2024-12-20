# Generated by Django 4.2.17 on 2024-12-20 05:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('recipebook', '0007_alter_ingredient_measurement_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='amount',
            field=models.FloatField(default=1, verbose_name='amount'),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='measurement',
            field=models.CharField(choices=[('pint', 'Pint(s)'), ('lbs', 'Pound(s)'), ('not_set', 'None'), ('g', 'Gram(s)'), ('tsp', 'Teaspoon(s)'), ('gallon', 'Gallon(s)'), ('mL', 'Milliliter(s)'), ('floz', 'Fluid Ounce(s)'), ('tbsp', 'Tablespoon(s)'), ('cup', 'Cup(s)'), ('quart', 'Quart(s)')], max_length=200, verbose_name='measurement'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='date_added',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='recipe_type',
            field=models.CharField(choices=[('holiday', 'Holiday'), ('dessert', 'Dessert'), ('dinner', 'Dinner'), ('breakfast', 'Breakfast'), ('lunch', 'Lunch'), ('large_group', 'Large Groups/Parties'), ('not_set', 'Not Set')], default='not_set', max_length=20, verbose_name='recipe type'),
        ),
    ]
