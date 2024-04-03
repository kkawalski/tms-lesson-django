from django.urls import path

from recipies.views import (
    MyFavoriteRecipies,
    RecipeListView, 
    RecipeDetailView,
    RecipeCreateView,
    RecipeUpdateView,
    RecipeDeleteView,
    MyRecipiesListView,
    recipe_like,
    recipe_list_api,
)


urlpatterns = [
    path("", RecipeListView.as_view(), name="recipe-list"),
    path("create", RecipeCreateView.as_view(), name="recipe-create"),
    path("<int:pk>/update", RecipeUpdateView.as_view(), name="recipe-update"),
    path("<int:pk>", RecipeDetailView.as_view(), name="recipe-detail"),
    path("mine", MyRecipiesListView.as_view(), name="recipe-mine"),
    path("favorite", MyFavoriteRecipies.as_view(), name="recipe-favorite"),
    path("<int:pk>/delete", RecipeDeleteView.as_view(), name="recipe-delete"),
    path("<int:pk>/like", recipe_like, name="recipe-like"),
]
