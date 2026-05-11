# Электронная библиотека колледжа

Статический frontend сохранен и подключен к Django backend. Книги теперь добавляются через Django Admin, PDF-файлы хранятся в `media/`.

## Запуск

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata sample_books
python manage.py createsuperuser
python manage.py runserver
```

После запуска:

- сайт: http://127.0.0.1:8000/
- админка: http://127.0.0.1:8000/admin/

## Как добавить книгу

1. Перейдите в админку.
2. Откройте раздел `Книги`.
3. Нажмите `Добавить книгу`.
4. Заполните название, категорию, описание и загрузите PDF.
5. Сохраните запись.

PDF откроется на сайте по ссылке `Открыть PDF`.
