from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Book",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255, verbose_name="Название книги")),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("Математика", "Математика"),
                            ("Русский язык", "Русский язык"),
                            ("Русская литература", "Русская литература"),
                            ("Программирование", "Программирование"),
                            ("Дизайн", "Дизайн"),
                        ],
                        db_index=True,
                        max_length=80,
                        verbose_name="Категория",
                    ),
                ),
                (
                    "pdf_file",
                    models.FileField(upload_to="books/pdfs/", verbose_name="PDF файл"),
                ),
                (
                    "cover",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="books/covers/",
                        verbose_name="Обложка",
                    ),
                ),
                ("description", models.TextField(blank=True, verbose_name="Короткое описание")),
                (
                    "is_popular",
                    models.BooleanField(default=False, verbose_name="Популярная книга"),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Дата обновления"),
                ),
            ],
            options={
                "verbose_name": "Книга",
                "verbose_name_plural": "Книги",
                "ordering": ("title",),
            },
        ),
    ]
