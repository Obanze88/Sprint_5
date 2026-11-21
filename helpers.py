from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators import Locators
from data import BASE_URL, generate_email, generate_password


def register_user(driver):
    email = generate_email()
    password = generate_password()
    name = 'Олег'

    driver.get(BASE_URL + 'register')

    driver.find_element(*Locators.NAME_INPUT).send_keys(name)
    driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*Locators.REGISTER_BUTTON).click()

    WebDriverWait(driver, 5).until(
        expected_conditions.url_contains('/login')
    )

    return email, password


def login_user(driver, email, password):
    driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*Locators.LOGIN_BUTTON).click()

    WebDriverWait(driver, 5).until(
        expected_conditions.url_to_be(BASE_URL)
    )