# Generated by Django 5.0.1 on 2024-02-12 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0002_tag_category_post_commend_recipe_delete_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='text',
            field=models.TextField(null=True),
        ),
    ]
