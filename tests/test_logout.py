from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators import Locators
from data import BASE_URL
from helpers import register_user, login_user


class TestLogout:

    def test_logout(self, driver):
        email, password = register_user(driver)

        login_user(driver, email, password)

        driver.find_element(*Locators.PERSONAL_ACCOUNT_LINK).click()

        logout_button = WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable(
                Locators.LOGOUT_BUTTON
            )
        )

        logout_button.click()

        WebDriverWait(driver, 5).until(
            expected_conditions.url_contains('/login')
        )

        assert '/login' in driver.current_url