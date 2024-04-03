from rest_framework import serializers

from recipies.models import Recipe
from categories.models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            "id",
            "name",
        ]


class RecipeBaseSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.IntegerField(write_only=True, required=False)
    likes_count = serializers.SerializerMethodField()

    class Meta:
        model = Recipe
        fields = [
            "id",
            "title",
            "category",
            "category_id",
            "likes_count",
        ]
        
    def get_likes_count(self, obj: Recipe):
        return obj.liked_by_users.count()


class RecipeDetailSerializer(RecipeBaseSerializer):
    liked_by_users = serializers.ListSerializer(
        child=serializers.CharField(source="liked_by_users.username")
    )
    # random_number = serializers.SerializerMethodField()

    class Meta(RecipeBaseSerializer.Meta):
        fields = RecipeBaseSerializer.Meta.fields + [
            "instruction",
            "ingredients",
            "liked_by_users",
            # "random_number",
        ]

    # def get_random_number(self, obj):
    #     import random
    #     return random.randint(1,100)



import random

class RandomComlexNumber(serializers.Serializer):
    name = serializers.CharField()
    i = serializers.SerializerMethodField()
    j = serializers.SerializerMethodField()

    class Meta:
        fields = ["i", "j", "name"]

    def get_i(self, obj):
        return random.randint(1,100)
    
    def get_j(self, obj):
        return random.randint(1,100)


class IngredientSerializer(serializers.Serializer):
    name = serializers.CharField()
    value = serializers.CharField(default="", required=False)
    measure = serializers.CharField(default="", required=False)
