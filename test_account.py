import requests
import json
import pytest
from faker import Faker
from client import Client


@pytest.fixture
def client():
    return Client()


@pytest.fixture
def generate_user():
    fake = Faker("ru_RU")
    return {
        "login": fake.user_name(),
        "email": fake.email(),
        "password": fake.password()
    }


data = [
    # короткий логин
    {
        "login": "l",
        "email": "email_12345@mail.ru",
        "password": "12345678"
    },
    # невалидный емейл
    {
        "login": "login_12345678902",
        "email": "e",
        "password": "12345678"
    },
    # Короткий пароль
    {
        "login": "login_12345678902",
        "email": "email_12345@mail.ru",
        "password": "1"
    }
]


@pytest.mark.parametrize('data', data)
def test_post_v1_account(data, client):
    response = client.register_user(data)
    assert response.status_code == 200, "Статус код ответа сервера должен быть 400"
