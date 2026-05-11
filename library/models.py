from django.db import models


class Book(models.Model):
    class Category(models.TextChoices):
        MATHEMATICS = "Математика", "Математика"
        RUSSIAN_LANGUAGE = "Русский язык", "Русский язык"
        RUSSIAN_LITERATURE = "Русская литература", "Русская литература"
        PROGRAMMING = "Программирование", "Программирование"
        DESIGN = "Дизайн", "Дизайн"

    title = models.CharField("Название книги", max_length=255)
    category = models.CharField(
        "Категория",
        max_length=80,
        choices=Category.choices,
        db_index=True,
    )
    pdf_file = models.FileField("PDF файл", upload_to="books/pdfs/")
    cover = models.ImageField(
        "Обложка",
        upload_to="books/covers/",
        blank=True,
        null=True,
    )
    description = models.TextField("Короткое описание", blank=True)
    is_popular = models.BooleanField("Популярная книга", default=False)
    created_at = models.DateTimeField("Дата добавления", auto_now_add=True)
    updated_at = models.DateTimeField("Дата обновления", auto_now=True)

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
        ordering = ("title",)

    def __str__(self):
        return self.title

    @property
    def first_letter(self):
        return self.title.strip()[:1].upper() or "К"
