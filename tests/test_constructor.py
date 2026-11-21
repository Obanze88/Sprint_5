from selenium.webdriver.support.wait import WebDriverWait

from locators import Locators
from data import BASE_URL


class TestConstructor:

    def test_go_to_sauces(self, driver):
        driver.get(BASE_URL)

        driver.find_element(*Locators.SAUCES_TAB).click()

        assert WebDriverWait(driver, 5).until(
            lambda driver:
            'tab_tab_type_current' in
            driver.find_element(*Locators.SAUCES_TAB)
            .find_element('xpath', '..')
            .get_attribute('class')
        )

    def test_go_to_fillings(self, driver):
        driver.get(BASE_URL)

        driver.find_element(*Locators.FILLINGS_TAB).click()

        assert WebDriverWait(driver, 5).until(
            lambda driver:
            'tab_tab_type_current' in
            driver.find_element(*Locators.FILLINGS_TAB)
            .find_element('xpath', '..')
            .get_attribute('class')
        )

    def test_go_to_buns(self, driver):
        driver.get(BASE_URL)

        driver.find_element(*Locators.SAUCES_TAB).click()
        driver.find_element(*Locators.BUNS_TAB).click()

        assert WebDriverWait(driver, 5).until(
            lambda driver:
            'tab_tab_type_current' in
            driver.find_element(*Locators.BUNS_TAB)
            .find_element('xpath', '..')
            .get_attribute('class')
        )