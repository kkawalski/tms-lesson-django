from typing import Any
from django.db.models.query import QuerySet
from django.db.models import Count, Q
from django.views.generic import ListView, DetailView

from categories.models import Category


class CategoryListView(ListView):
    template_name = "category_list.html"
    model = Category

    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset()
        queryset = queryset.filter(parent__isnull=True)
        return queryset


class CategoryDetailView(DetailView):
    template_name = "category_detail.html"
    model = Category
    queryset = Category.objects

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        category: Category = self.get_object()
        parents = []
        parent_id = category.parent_id
        if parent_id is not None:
            categories = (
                Category.objects
                .exclude(
                    Q(parent=category) | 
                    Q(id=category.id)
                )
                .values_list("id", "parent_id", "name")
            )

            parent_id_dict = {}
            parent_title_dict = {}
            for cat_id, cat_parent_id, cat_title in categories:
                parent_id_dict[cat_id] = cat_parent_id
                parent_title_dict[cat_id] = cat_title

            while parent_id is not None:
                parents.append({
                    "id": parent_id,
                    "name": parent_title_dict[parent_id],
                })
                parent_id = parent_id_dict.get(parent_id)

        context['parents'] = parents[::-1]

        most_likes_recipies: QuerySet = category.recipies.most_liked()
        context["recipe_list"] = most_likes_recipies
        return context
