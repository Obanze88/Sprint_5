from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators import Locators
from data import BASE_URL
from helpers import register_user, login_user


class TestPersonalAccount:

    def test_open_personal_account(self, driver):
        email, password = register_user(driver)

        login_user(driver, email, password)

        driver.find_element(*Locators.PERSONAL_ACCOUNT_LINK).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.url_contains('/account')
        )

        assert '/account' in driver.current_url

    def test_go_to_constructor_from_account(self, driver):
        email, password = register_user(driver)

        login_user(driver, email, password)

        driver.find_element(*Locators.PERSONAL_ACCOUNT_LINK).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.url_contains('/account')
        )

        driver.find_element(*Locators.CONSTRUCTOR_LINK).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.url_to_be(BASE_URL)
        )

        assert driver.current_url == BASE_URL

    def test_go_to_constructor_by_logo(self, driver):
        email, password = register_user(driver)

        login_user(driver, email, password)

        driver.find_element(*Locators.PERSONAL_ACCOUNT_LINK).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.url_contains('/account')
        )

        driver.find_element(*Locators.LOGO_LINK).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.url_to_be(BASE_URL)
        )

        assert driver.current_url == BASE_URL