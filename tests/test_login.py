from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators import Locators
from data import BASE_URL
from helpers import register_user, login_user


class TestLogin:

    def test_login_from_main_page(self, driver):
        email, password = register_user(driver)

        driver.get(BASE_URL)
        driver.find_element(*Locators.LOGIN_ACCOUNT_BUTTON).click()

        login_user(driver, email, password)

        assert driver.current_url == BASE_URL

    def test_login_from_personal_account(self, driver):
        email, password = register_user(driver)

        driver.get(BASE_URL)
        driver.find_element(*Locators.PERSONAL_ACCOUNT_LINK).click()

        login_user(driver, email, password)

        assert driver.current_url == BASE_URL

    def test_login_from_registration_page(self, driver):
        email, password = register_user(driver)

        driver.get(BASE_URL + 'register')
        driver.find_element(*Locators.LOGIN_LINK).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.url_contains('/login')
        )

        login_user(driver, email, password)

        assert driver.current_url == BASE_URL

    def test_login_from_forgot_password_page(self, driver):
        email, password = register_user(driver)

        driver.get(BASE_URL + 'forgot-password')
        driver.find_element(*Locators.LOGIN_LINK).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.url_contains('/login')
        )

        login_user(driver, email, password)

        assert driver.current_url == BASE_URL