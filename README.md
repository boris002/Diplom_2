# Diplom_2
## Описание
Этот проект содержит автоматизированные тесты для API сервиса Stellar Burgers.  
Тестируются ключевые эндпоинты: создание пользователя, вход в систему и создание заказов.
## Структура тестов

### test_user_creation
- `test_create_unique_user_success` — создание уникального пользователя.
- `test_create_existing_user_failure` — попытка создать пользователя с уже существующей почтой.
- `test_create_user_missing_field_failure` — создание пользователя без обязательного поля.

### test_user_login
- `test_login_valid_user_success` — успешный вход под существующим пользователем.
- `test_login_invalid_credentials_failure` — вход с неверным логином или паролем.

### test_order_creation
- `test_create_order_with_auth_and_ingredients_success` — создание заказа с авторизацией и ингредиентами.
- `test_create_order_with_auth_without_ingredients_failure` — создание заказа с авторизацией, но без ингредиентов.
- `test_create_order_without_auth_with_ingredients_success` — создание заказа без авторизации, но с ингредиентами.
- `test_create_order_without_auth_and_ingredients_failure` — создание заказа без авторизации и без ингредиентов.
- `test_create_order_invalid_hash_failure` — создание заказа с неверным хешем ингредиентов.
## Запуск тестов
pytest --alluredir=allure-results

## Фикстуры
- `client` — экземпляр API-клиента.
- `new_user` — генерация нового уникального пользователя с email, паролем и токеном авторизации.