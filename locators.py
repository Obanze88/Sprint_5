from selenium.webdriver.common.by import By


class Locators:
    LOGIN_ACCOUNT_BUTTON = (
        By.XPATH,
        ".//button[text()='Войти в аккаунт']"
    )  # Кнопка «Войти в аккаунт»

    PERSONAL_ACCOUNT_LINK = (
        By.XPATH,
        ".//p[text()='Личный Кабинет']"
    )  # Ссылка «Личный Кабинет»

    CONSTRUCTOR_LINK = (
        By.XPATH,
        ".//p[text()='Конструктор']"
    )  # Ссылка «Конструктор»

    LOGO_LINK = (
        By.XPATH,
        ".//a[@href='/']"
    )  # Логотип Stellar Burgers

    REGISTER_LINK = (
        By.XPATH,
        ".//a[@href='/register']"
    )  # Ссылка «Зарегистрироваться»

    LOGIN_LINK = (
        By.XPATH,
        ".//a[@href='/login']"
    )  # Ссылка «Войти»

    FORGOT_PASSWORD_LINK = (
        By.XPATH,
        ".//a[@href='/forgot-password']"
    )  # Ссылка «Восстановить пароль»

    NAME_INPUT = (
        By.XPATH,
        ".//label[text()='Имя']/following-sibling::input"
    )  # Поле «Имя»

    EMAIL_INPUT = (
        By.XPATH,
        ".//label[text()='Email']/following-sibling::input"
    )  # Поле Email

    PASSWORD_INPUT = (
        By.XPATH,
        ".//label[text()='Пароль']/following-sibling::input"
    )  # Поле «Пароль»

    REGISTER_BUTTON = (
        By.XPATH,
        ".//button[text()='Зарегистрироваться']"
    )  # Кнопка «Зарегистрироваться»

    LOGIN_BUTTON = (
        By.XPATH,
        ".//button[text()='Войти']"
    )  # Кнопка «Войти»

    PASSWORD_ERROR = (
        By.XPATH,
        ".//p[text()='Некорректный пароль']"
    )  # Ошибка некорректного пароля

    LOGOUT_BUTTON = (
        By.XPATH,
        ".//button[text()='Выйти' or text()='Выход']"
    )  # Кнопка выхода из аккаунта

    BUNS_TAB = (
        By.XPATH,
        ".//*[text()='Булки']"
    )  # Вкладка «Булки»

    SAUCES_TAB = (
        By.XPATH,
        ".//*[text()='Соусы']"
    )  # Вкладка «Соусы»

    FILLINGS_TAB = (
        By.XPATH,
        ".//*[text()='Начинки']"
    )  # Вкладка «Начинки»