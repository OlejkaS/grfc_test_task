# grfc_test_task

Веб-сервис для формирования каталога категорий.

### Стэк

- [Python 3.11.5](https://docs.python.org/release/3.11.5/)
- [Django 5.0.4](https://docs.djangoproject.com/en/5.0/releases/5.0.4/)
- [Django MPTT 0.16.0](https://django-mptt.readthedocs.io/en/latest/)
- [Python dotenv 1.0.1](https://pypi.org/project/python-dotenv/)
- [Psycopg 2.9.9](https://www.psycopg.org/docs/)

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

## Запуск приложения через Docker

1. После завершения настройки для запуска приложения через Docker достаточно прописать в терминале одну команду:

   ```bash
   docker-compose up -d
   ```

2. Для остановки приложения нужно выполнить команду:

   ```bash
   docker-compose down
   ```

---

[Инструкция по созданию переменных окружения](./.env.example)

### Автор
- [Олег Силецкий](https://github.com/OlejkaS)
