import allure

@allure.epic("Логин")
class TestLogin:

    @allure.title("Успешный вход под существующим пользователем")
    @allure.description("Тест проверяет успешный вход под существующим пользователем. Ожидается статус 200 и success=True.")
    def test_login_valid_user_success(self, client, new_user):
        user_data = new_user["user"]
        headers = new_user["headers"]
        response = client.post("/auth/login", {"email": user_data["email"], "password": user_data["password"]})
        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title("Вход с неверным логином или паролем")
    @allure.description("Тест проверяет, что вход с неверным логином или паролем невозможен. Ожидается статус 401 и сообщение об ошибке.")
    def test_login_invalid_credentials_failure(self, client):
        response = client.post("/auth/login", {"email": "badbad@test.ru", "password": "123456"})
        assert response.status_code == 401
        assert response.json()["message"] == "email or password are incorrect"
