import allure
from data.user_data import generate_user

@allure.epic("Создание пользователя")
class TestUsers:

    @allure.title("Создание уникального пользователя — успешно")
    @allure.description("Тест проверяет успешное создание нового пользователя с валидными данными. Ожидается статус 200 и success=True.")
    def test_create_unique_user_success(self, client):
        user = generate_user()
        response = client.post("/auth/register", user)
        assert response.status_code == 200
        assert response.json()["success"] is True

        # Очистка (удаляем пользователя после теста, если создан)
        login_res = client.post("/auth/login", {"email": user["email"], "password": user["password"]})
        token = login_res.json().get("accessToken")
        if token:
            headers = {"Authorization": token}
            client.delete("/auth/user", headers=headers)

    @allure.title("Создание пользователя, который уже зарегистрирован")
    @allure.description("Тест проверяет, что нельзя создать пользователя с уже существующей почтой. Ожидается статус 403 и сообщение 'User already exists'.")
    def test_create_existing_user_failure(self, client, new_user):
        user_data = new_user["user"]
        # первый раз создаём пользователя (через фикстуру)
        client.post("/auth/register", user_data)
        # пытаемся создать повторно
        response = client.post("/auth/register", user_data)
        assert response.status_code == 403
        assert response.json()["message"] == "User already exists"

    @allure.title("Создание пользователя без обязательного поля")
    @allure.description("Тест проверяет, что нельзя создать пользователя без обязательного поля. Ожидается статус 403 и сообщение об ошибке.")
    def test_create_user_missing_field_failure(self, client):
        user_data = {
            "name": "Test User",
            "email": "testuser@example.com"
            # пароль отсутствует
        }
        response = client.post("/auth/register", user_data)
        assert response.status_code == 403
        assert response.json()["message"] == "Email, password and name are required fields"
