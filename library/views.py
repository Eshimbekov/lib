from django.db.models import Q
from django.shortcuts import render

from .models import Book


CATEGORY_META = {
    "Все": "Полный каталог",
    "Математика": "Алгебра и геометрия",
    "Русский язык": "Грамотность и речь",
    "Русская литература": "Классика и современность",
    "Программирование": "Web, Python, JS",
    "Дизайн": "Графика и интерфейсы",
}


def get_book_ending(count):
    last_digit = count % 10
    last_two_digits = count % 100

    if 11 <= last_two_digits <= 14:
        return "книг"
    if last_digit == 1:
        return "книга"
    if 2 <= last_digit <= 4:
        return "книги"
    return "книг"


def get_categories():
    categories = [{"name": "Все", "meta": CATEGORY_META["Все"]}]

    for value, label in Book.Category.choices:
        categories.append(
            {
                "name": value,
                "title": label,
                "meta": CATEGORY_META.get(value, "Учебные материалы"),
            }
        )

    return categories


def book_list(request):
    search_query = request.GET.get("q", "").strip()
    active_category = request.GET.get("category", "Все").strip() or "Все"
    books = Book.objects.all()

    if active_category != "Все":
        books = books.filter(category=active_category)

    if search_query:
        books = books.filter(Q(title__icontains=search_query))

    books = list(books)
    popular_books = list(Book.objects.filter(is_popular=True)[:4])

    if not popular_books:
        popular_books = list(Book.objects.all()[:4])

    context = {
        "books": books,
        "popular_books": popular_books,
        "categories": get_categories(),
        "active_category": active_category,
        "search_query": search_query,
        "book_count_label": f"{len(books)} {get_book_ending(len(books))}",
    }

    return render(request, "library/index.html", context)
