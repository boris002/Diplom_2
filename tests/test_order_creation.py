import allure
from data.urls import OrdersEndpoints

INGREDIENTS = ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa70"]

@allure.epic("Заказы")
class TestOrders:

    @allure.title("Создание заказа с авторизацией и с ингредиентами")
    @allure.description("Авторизованный пользователь создаёт заказ с ингредиентами. Ожидается статус 200 и success=True.")
    def test_create_order_with_auth_and_ingredients_success(self, client, new_user):
        headers = new_user["headers"]
        response = client.post(OrdersEndpoints.CREATE_ORDER, {"ingredients": INGREDIENTS}, headers=headers)
        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title("Создание заказа с авторизацией, но без ингредиентов")
    @allure.description("Авторизованный пользователь создаёт заказ без ингредиентов. Ожидается статус 400 и сообщение об ошибке.")
    def test_create_order_with_auth_without_ingredients_failure(self, client, new_user):
        headers = new_user["headers"]
        response = client.post(OrdersEndpoints.CREATE_ORDER, {"ingredients": []}, headers=headers)
        assert response.status_code == 400
        assert response.json()["message"] == "Ingredient ids must be provided"

    @allure.title("Создание заказа без авторизации, но с ингредиентами")
    @allure.description("Неавторизованный пользователь создаёт заказ с ингредиентами. Ожидается статус 200 и success=True.")
    def test_create_order_without_auth_with_ingredients_success(self, client):
        response = client.post(OrdersEndpoints.CREATE_ORDER, {"ingredients": INGREDIENTS})
        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title("Создание заказа без авторизации и без ингредиентов")
    @allure.description("Неавторизованный пользователь создаёт заказ без ингредиентов. Ожидается статус 400 и сообщение об ошибке.")
    def test_create_order_without_auth_and_ingredients_failure(self, client):
        response = client.post(OrdersEndpoints.CREATE_ORDER, {"ingredients": []})
        assert response.status_code == 400
        assert response.json()["message"] == "Ingredient ids must be provided"

    @allure.title("Создание заказа с неверным хешем ингредиентов")
    @allure.description("Передача некорректного ID ингредиента. Ожидается статус 400 или 500.")
    def test_create_order_invalid_hash_failure(self, client):
        response = client.post(OrdersEndpoints.CREATE_ORDER, {"ingredients": ["invalid_hash"]})
        assert response.status_code in [400, 500]
