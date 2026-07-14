from django.urls import path

from .views import (
    article_list_view,
    category_detail_view,
    category_list_view,
    category_posts_view,
)


urlpatterns = [
    path("categories/", category_list_view, name="category-list"),
    path(
    "category/<int:category_id>/",
    category_posts_view,
    name="category-posts"
),
 
]