class BaseURL:
    BASE = "https://stellarburgers.education-services.ru/api"


class AuthEndpoints:
    REGISTER = "/auth/register"
    LOGIN = "/auth/login"
    LOGOUT = "/auth/logout"
    DELETE_USER = "/auth/user"


class OrdersEndpoints:
    CREATE_ORDER = "/orders"
    GET_ORDERS = "/orders"