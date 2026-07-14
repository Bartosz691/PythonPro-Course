from django.urls import path

from .views import (
    article_list_view,
    category_detail_view,
    category_list_view,
    category_posts_view,
    home_view,
)


urlpatterns = [
    path("", home_view, name="home"),
    path(
        "category/<int:category_id>/",
        category_posts_view,
        name="category-posts"
    ),
    path("categories/", category_list_view, name="category-list"),
    path(
        "categories/<int:pk>/",
        category_detail_view,
        name="category-detail"
    ),
    path("articles/", article_list_view, name="article-list"),
]