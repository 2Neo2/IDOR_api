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

### 6. IDOR уязвимости

1) `GET /api/clients/<id>` — позволяет авторизованному пользователю получить, изменить или удалить данные другого клиента, просто подставив чужой `id` в URL.

2) `GET /api/orders` и `GET /api/orders/<id>` — позволяют получить список всех заказов в системе, а также доступ к конкретному заказу по ID, независимо от того, кому он принадлежит.

3) `GET /api/reviews` и `GET /api/reviews/<id>` — любой авторизованный пользователь может просматривать, изменять или удалять отзывы, оставленные другими клиентами.

### 7. Устранение уязвимостей

Добавить файл `permissions.py`, который проверяет доступ к запрашиваемой пользователем информации:

```python
from rest_framework import permissions

class IsPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if hasattr(obj, 'user'):
            return obj.user == request.user
        return obj == request.user
```

Помимо этого необходимо чтобы пользователь не мог создавать объекты от имени других пользователей

```python
def perform_create(self, serializer):
    serializer.save(user=self.request.user)
```

