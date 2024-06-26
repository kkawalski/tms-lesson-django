from django.urls import path

from categories.views import CategoryListView, CategoryDetailView


urlpatterns = [
    path("", CategoryListView.as_view(), name="category-list"),
    path("<int:pk>", CategoryDetailView.as_view(), name="category-detail"),
]
