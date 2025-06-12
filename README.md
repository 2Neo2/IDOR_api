# Онлайн магазин с защитой от IDOR (Django REST Framework)

## Установка и запуск проекта

### 1. Миграции базы данных

Создание миграций и применение их к базе данных:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 2. Загрузка данных

```bash
python manage.py installation
```

### 3. Создание суперпользователя

Для доступа к Django админ панели создайте суперпользователя:

```bash
python manage.py createsuperuser
```

### 4. Запуск тестов

Для запуска тестов используйте команду:

```bash
python manage.py test
```

### 5. Запуск сервера

Для запуска локального сервера используйте:

```bash
python manage.py runserver
```
