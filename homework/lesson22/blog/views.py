from datetime import timedelta

from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from .models import Category, Post

def category_posts_view(request, category_id):
    category = get_object_or_404(Category, id=category_id)

    posts = Post.objects.filter(category=category)

    return render(
        request,
        "blog/category_posts.html",
        {
            "category": category,
            "posts": posts,
        }
    )


def category_list_view(request):
    categories = Category.objects.all()

    return render(
        request,
        "blog/category_list.html",
        {
            "categories": categories
        }
    )


def category_detail_view(request, pk):
    category = get_object_or_404(Category, pk=pk)

    return render(
        request,
        "blog/category_detail.html",
        {
            "category": category
        }
    )


def article_list_view(request):
    posts = Post.objects.all().order_by("-publication_date")

    query = request.GET.get("q")

    if query:
        posts = posts.filter(
            title__icontains=query
        )

    new_post_date = timezone.now() - timedelta(days=3)

    for post in posts:
        post.is_new = post.publication_date >= new_post_date

    return render(
        request,
        "blog/article_list.html",
        {
            "articles": posts,
            "query": query or "",
        }
    )