# Generated by Django 5.0.1 on 2024-02-05 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0002_alter_recipe_cook_time_alter_recipe_pref_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='cook_time',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='pref_time',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
