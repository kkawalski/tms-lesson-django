from django.urls import path
from rest_framework import routers

from recipies.api.views import RecipeListCreateAPIView, RecipeRetrieveUpdateDestroyAPIView, RecipeViewSet, random_complex_number


recipe_router = routers.SimpleRouter()
recipe_router.register("", RecipeViewSet)


# urlpatterns = [
#     # path("", RecipeListCreateAPIView.as_view()),
#     # path("<int:pk>", RecipeRetrieveUpdateDestroyAPIView.as_view()),
#     # # path("/create", RecipeCreateAPIView.as_view()),
#     # path("random", random_complex_number),
# ]

urlpatterns = recipe_router.urls
