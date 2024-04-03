from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.request import HttpRequest
from rest_framework.decorators import api_view, action
from rest_framework import status

from django.db.models.query import QuerySet

from recipies.api.serializers import (
    RecipeBaseSerializer, 
    RecipeDetailSerializer,
    IngredientSerializer,
    RandomComlexNumber
)
from recipies.models import Recipe


class RecipeListCreateAPIView(ListCreateAPIView):
    queryset = (
        Recipe.objects
        .select_related("category")
        .prefetch_related("liked_by_users")
    )
    serializer_class = RecipeBaseSerializer


class RecipeRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = (
        Recipe.objects
        .select_related("category")
        .prefetch_related("liked_by_users")
    )
    serializer_class = RecipeDetailSerializer


class RecipeViewSet(ModelViewSet):
    queryset = (
        Recipe.objects
        .select_related("category")
        .prefetch_related("liked_by_users")
    )
    serializer_class = RecipeBaseSerializer

    def get_serializer_class(self):
        if self.detail:
            return RecipeDetailSerializer
        return super().get_serializer_class()
    
    @action(methods=["GET"], detail=False, url_path="most-liked")
    def most_liked(self, request: HttpRequest, *args, **kwargs):
        recipe_limit = int(request.query_params.get("limit") or 3)
        recipe_queryset: QuerySet[Recipe] = self.get_queryset().most_liked(recipe_limit)
        recipe_serializer = self.get_serializer(recipe_queryset, many=True)
        return Response(recipe_serializer.data, status=status.HTTP_200_OK)
    
    @action(methods=["GET", "POST"], detail=True)
    def ingredients(self, request: HttpRequest, pk=None, *args, **kwargs):
        recipe: Recipe = self.get_object()
        ingredients = recipe.ingredients or []
        if request.method == "POST":
            ingredient_serializer = IngredientSerializer(data=request.data)
            if ingredient_serializer.is_valid(raise_exception=True):
                ingredients.append(ingredient_serializer.data)
                recipe.ingredients = ingredients
                recipe.save()
        return Response(ingredients)


@api_view(["GET"])
def random_complex_number(request):
    random_number = RandomComlexNumber(instance={"name": "complex"})
    
    return Response(random_number.data)
