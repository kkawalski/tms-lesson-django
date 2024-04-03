# Generated by Django 5.0.3 on 2024-04-01 16:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipies', '0007_recipe_ingredients'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecipeStep',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='steps', to='recipies.recipe')),
            ],
            options={
                'ordering': ('id',),
            },
        ),
    ]