from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=32)
    parent = models.ForeignKey(
        "categories.Category",
        on_delete=models.SET_NULL,
        related_name="children",
        null=True, blank=True
    )
    image = models.ImageField(
        upload_to="category_images",
        null=True, blank=True,
    )

    def __str__(self) -> str:
        return self.name
