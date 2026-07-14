import random

from django.core.management.base import BaseCommand
from faker import Faker

from blog.models import Category, Post


class Command(BaseCommand):
    help = "Usuwa stare dane i tworzy kategorie oraz 100 losowych postów"

    def handle(self, *args, **options):
        fake = Faker("pl_PL")

        self.stdout.write("Usuwanie istniejących postów i kategorii...")

        Post.objects.all().delete()
        Category.objects.all().delete()

        category_names = [
            "Technologia",
            "Podróże",
            "Kulinaria",
            "Sport",
            "Kultura",
            "Nauka",
            "Zdrowie",
        ]

        categories = []

        for name in category_names:
            category = Category.objects.create(name=name)
            categories.append(category)

        self.stdout.write(
            self.style.SUCCESS(
                f"Utworzono {len(categories)} kategorii."
            )
        )

        posts = []

        for _ in range(100):
            post = Post(
                title=fake.sentence(nb_words=6),
                content=fake.paragraph(nb_sentences=8),
                publication_date=fake.date_time_this_year(
                    tzinfo=None
                ),
                category=random.choice(categories),
            )

            posts.append(post)

        Post.objects.bulk_create(posts)

        self.stdout.write(
            self.style.SUCCESS(
                f"Utworzono {len(posts)} postów."
            )
        )

        self.stdout.write(
            self.style.SUCCESS(
                "Generowanie danych zakończone."
            )
        )