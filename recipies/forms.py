from django import forms

from recipies.models import Recipe
from categories.models import Category


class RecipeUpdateCreateForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter Title"
        })
    )
    instruction = forms.CharField(
        widget=forms.Textarea(attrs={
            "class": "form-control",
            "placeholder": "Type your instruction"
        })
    )
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget=forms.Select(attrs={
            "class": "form-control",
            "placeholder": "Select category"
        }),
        required=False,
    )

    class Meta:
        model = Recipe
        fields = [
            "title",
            "instruction",
            "category",
        ]
