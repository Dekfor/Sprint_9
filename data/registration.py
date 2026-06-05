import random, string


def generate_user_data():
    rand = ''.join(random.choices(string.ascii_lowercase + string.digits,k=8))

    return {
        "first_name": "Ivan",
        "last_name": "Ivanov",
        "username": f"user_{rand}",
        "email": f"{rand}@mail.ru",
        "password": "Testpassword123!"
    }
