import random
import string

def random_email():
    return "user_" + "".join(random.choices(string.ascii_lowercase, k=6)) + "@test.com"

def random_password():
    return "".join(random.choices(string.ascii_letters + string.digits, k=8))

def generate_user():
    return {
        "email": random_email(),
        "password": random_password(),
        "name": "TestUser"
    }
