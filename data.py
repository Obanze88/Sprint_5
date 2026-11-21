import random


BASE_URL = 'https://stellarburgers.education-services.ru/'


def generate_email():
    number = random.randint(100, 999)
    return f'kirill_golovin_55{number}@yandex.ru'


def generate_password():
    number = random.randint(100, 999)
    return f'password{number}'