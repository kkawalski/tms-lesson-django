from typing import Any
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
            "ingredients",
        ]

    def clean_ingredients(self):
        return self.cleaned_data["ingredients"]

    # def clean(self) -> dict[str, Any]:
    #     import pdb
    #     pdb.set_trace()
    #     return super().clean()
