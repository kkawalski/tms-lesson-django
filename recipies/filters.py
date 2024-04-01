from django import forms
import django_filters

from categories.models import Category
from recipies.models import Recipe
from users.models import User

class RecipeFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(
        lookup_expr='icontains', 
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Title",
        })
    )
    # instruction = django_filters.CharFilter(
    #     lookup_expr='icontains', 
    #     widget=forms.TextInput(attrs={
    #         "class": "form-control",
    #         "placeholder": "Instruction",
    #     })
    # )
    author__username = django_filters.CharFilter(
        lookup_expr='icontains', 
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Author",
        })
    )
    category = django_filters.ModelChoiceFilter(
        queryset=Category.objects.all(),
        widget=forms.Select(attrs={
            "class": "form-control",
            "placeholder": "Category",
        })
    )

    class Meta:
        model = Recipe
        fields = [
            'title', 
            # 'instruction', 
            'category',
        ]