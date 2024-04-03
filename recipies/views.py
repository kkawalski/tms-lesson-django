from typing import Any
import itertools

from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DetailView,
    DeleteView,
)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django_filters.views import FilterView
from django.db.models import Q

from core.mixins import OwnOrRedirectMixin
from recipies.models import Recipe
from recipies.forms import RecipeUpdateCreateForm
from recipies.filters import RecipeFilter


class RecipeListView(FilterView):
    template_name = "recipe_list.html"
    model = Recipe
    queryset = (
        Recipe.objects
        .select_related("author")
        .prefetch_related("liked_by_users")
    )
    filterset_class = RecipeFilter

    def get_queryset(self) -> QuerySet[Recipe]:
        queryset = super().get_queryset()
        queryset = queryset.filter(is_active=True)
        return queryset


class RecipeCreateView(LoginRequiredMixin, CreateView):
    template_name = "recipe_create.html"
    model = Recipe
    form_class = RecipeUpdateCreateForm
    success_url = reverse_lazy("recipe-list")

    def form_valid(self, form: RecipeUpdateCreateForm) -> HttpResponse:
        self.object: Recipe = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
    
    def get_form_kwargs(self) -> dict[str, Any]:
        kwargs =  super().get_form_kwargs()
        if self.request.method in ("POST", "PUT"):
            ingr_data = {
                key: value for key, value in self.request.POST.items()
                if key.startswith("name") or key.startswith("value") or key.startswith("measure")
            }
            ingr_data_with_idx = map(lambda item: tuple(item[0].rsplit("_", 1)[::-1] + [item[1]]), ingr_data.items())
            ingr_groups = itertools.groupby(ingr_data_with_idx, key=lambda item: item[0])
            ingrs = [None] * (len(ingr_data) // 3)
            for idx, (_, i_data) in enumerate(ingr_groups):
                ing = {k: v for _, k, v in i_data}
                ingrs[idx] = ing
            kwargs["data"] = {
                "instruction": kwargs["data"]["instruction"][0],
                "title": kwargs["data"]["title"][0],
                "category": kwargs["data"]["category"][0],
            }
            kwargs["data"]["ingredients"] = ingrs
        return kwargs


class MyRecipiesListView(LoginRequiredMixin, ListView):
    template_name = "recipe_mine.html"
    model = Recipe
    filterset_class = RecipeFilter
    queryset = Recipe.objects.prefetch_related("liked_by_users")

    def get_queryset(self) -> QuerySet[Recipe]:
        queryset = super().get_queryset()
        queryset = queryset.filter(author=self.request.user)
        return queryset


class RecipeDetailView(DetailView):
    template_name = "recipe_detail.html"
    model = Recipe
    queryset = Recipe.objects.select_related("author")


class RecipeUpdateView(LoginRequiredMixin, OwnOrRedirectMixin, UpdateView):
    template_name = "recipe_create.html"
    model = Recipe
    queryset = Recipe.objects.select_related("author")
    form_class = RecipeUpdateCreateForm
    success_url = reverse_lazy("recipe-list")
    user_foreign_key = "author"


class RecipeDeleteView(LoginRequiredMixin, OwnOrRedirectMixin, DeleteView):
    model = Recipe
    success_url = reverse_lazy("recipe-mine")
    user_foreign_key = "author"

    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.is_active = not self.object.is_active
        self.object.save()
        return HttpResponseRedirect(success_url)


class MyFavoriteRecipies(LoginRequiredMixin, ListView):
    template_name = "recipe_favorites.html"
    model = Recipe
    queryset = (
        Recipe.objects
        .select_related("author")
        .prefetch_related("liked_by_users")
    )

    def get_queryset(self) -> QuerySet[Recipe]:
        queryset = super().get_queryset()
        queryset = queryset.filter(liked_by_users=self.request.user)
        return queryset


@csrf_exempt
@login_required
def recipe_like(request: HttpRequest, pk):
    user = request.user
    recipe = get_object_or_404(Recipe, pk=pk)
    dislike = user in recipe.liked_by_users.all()
    if dislike:
        recipe.liked_by_users.remove(user)
    else:
        recipe.liked_by_users.add(user)
    recipe.save()
    return JsonResponse({"status": not dislike})


def recipe_list_api(request: HttpRequest):
    recipe_list = [
        {
            "title": recipe.title,
            "instruction": recipe.instruction,
            "ingredients": recipe.ingredients,
        } for recipe in Recipe.objects.all()
    ]
    return JsonResponse({"recipe_list": recipe_list})
