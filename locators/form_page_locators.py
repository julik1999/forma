from selenium.webdriver.common.by import By


class FormPageLocators:
    USER_NAME = (By.CSS_SELECTOR, '#Имя')
    USER_SURNAME = (By.CSS_SELECTOR, '#Фамилия')
    EMAIL = (By.CSS_SELECTOR, '#Email')
    PHONE = (By.CSS_SELECTOR, '#Телефон')
    SUBMIT = (By.CSS_SELECTOR, '#Отправить')
    RESULT_TABLE = (By.XPATH, 'Форма отправлена')
