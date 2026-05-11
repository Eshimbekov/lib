from django.contrib import admin

from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "is_popular", "has_pdf", "has_cover")
    list_filter = ("category", "is_popular")
    search_fields = ("title", "description")
    readonly_fields = ("created_at", "updated_at")
    fieldsets = (
        (
            "Основная информация",
            {
                "fields": (
                    "title",
                    "category",
                    "description",
                    "is_popular",
                )
            },
        ),
        (
            "Файлы",
            {
                "fields": (
                    "pdf_file",
                    "cover",
                )
            },
        ),
        (
            "Служебная информация",
            {
                "classes": ("collapse",),
                "fields": (
                    "created_at",
                    "updated_at",
                ),
            },
        ),
    )

    @admin.display(description="PDF")
    def has_pdf(self, obj):
        return bool(obj.pdf_file)

    @admin.display(description="Обложка")
    def has_cover(self, obj):
        return bool(obj.cover)
