from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators import Locators
from data import BASE_URL, generate_email, generate_password


class TestRegistration:

    def test_successful_registration(self, driver):
        driver.get(BASE_URL + 'register')

        driver.find_element(*Locators.NAME_INPUT).send_keys('Олег')
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(generate_email())
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(generate_password())
        driver.find_element(*Locators.REGISTER_BUTTON).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.url_contains('/login')
        )

        assert '/login' in driver.current_url

    def test_registration_with_incorrect_password(self, driver):
        driver.get(BASE_URL + 'register')

        driver.find_element(*Locators.NAME_INPUT).send_keys('Олег')
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(generate_email())
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys('12345')
        driver.find_element(*Locators.REGISTER_BUTTON).click()

        error = WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                Locators.PASSWORD_ERROR
            )
        )

        assert error.text == 'Некорректный пароль'