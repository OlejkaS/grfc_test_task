# grfc_test_task

Веб-сервис для формирования каталога категорий.

### Стэк

- [Python 3.11.5](https://docs.python.org/release/3.11.5/)
- [Django 5.0.4](https://docs.djangoproject.com/en/5.0/releases/5.0.4/)
- [Django MPTT 0.16.0](https://django-mptt.readthedocs.io/en/latest/)
- [Python dotenv 1.0.1](https://pypi.org/project/python-dotenv/)
- [Psycopg 2.9.9](https://www.psycopg.org/docs/)

## Оформление проекта

В корневой директории находятся файлы схемы базы данных, UML-схемы и SQL-дамп со структурой базы и данными приложения.

## Установка проекта

1. Клонируйте репозиторий:

    ```
    git clone git@github.com:OlejkaS/grfc_test_task.git
    ```
2. Перейдите в папку с проектом:
    ```
    cd grfc_test_task
    ```
2. Создайте файл .env и заполните его своими данными. Перечень данных указан в корневой директории проекта в файле .env.example.

[Инструкция по созданию переменных окружения](./.env.example)

## Запуск приложения через терминал

1. Cоздать и активировать виртуальное окружение:

   ```
   python -m venv venv
   ```
   ```
   source venv/Scripts/activate
   ```

2. Установить зависимости из файла requirements.txt:

   ```
   cd cat_logistics
   ```
   ```
   python -m pip install --upgrade pip
   ```
   ```
   pip install -r requirements.txt
   ```

3. Выполнить миграции:

   ```
   python manage.py migrate
   ```

4. Выполнить миграции:

   ```
   python manage.py runserver
   ```

## Запуск приложения через Docker

Для запуска через Docker в файле .env для поля `DB_HOST` установить значение `db`.

1. После завершения настройки для запуска приложения через Docker достаточно прописать в терминале одну команду:

   ```bash
   docker-compose up -d
   ```

2. Для остановки приложения нужно выполнить команду:

   ```bash
   docker-compose down
   ```

### Автор
- [Олег Силецкий](https://github.com/OlejkaS)
