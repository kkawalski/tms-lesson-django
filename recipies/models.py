from django.db import models


class RecipeQuerySet(models.QuerySet):
    def most_liked(self, recipe_limit: int = 3):
        return (self
                .annotate(likes_count=models.Count("liked_by_users"))
                .order_by("-likes_count")
                )[:recipe_limit]


class Recipe(models.Model):
    title = models.CharField(max_length=255)
    instruction = models.TextField(blank=True)
    created = models.DateTimeField(null=True, blank=True)
    ingredients = models.JSONField(null=True, blank=True)
    author = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="recipies",
        null=True,
        blank=True,
    )
    liked_by_users = models.ManyToManyField(
        "users.User",
        through="recipies.FavoriteRecipe",
        related_name="favorite_recipies",
    )
    category = models.ForeignKey(
        "categories.Category",
        on_delete=models.SET_NULL,
        related_name="recipies",
        null=True, blank=True,
    )

    is_active = models.BooleanField(default=True)

    objects = RecipeQuerySet.as_manager()

    def __str__(self) -> str:
        return self.title


class FavoriteRecipe(models.Model):
    recipe = models.ForeignKey(
        "recipies.Recipe",
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )


class RecipeStep(models.Model):
    description = models.TextField()
    recipe = models.ForeignKey(
        "recipies.Recipe",
        on_delete=models.CASCADE,
        related_name="steps",
    )

    class Meta:
        ordering = ("id",)
