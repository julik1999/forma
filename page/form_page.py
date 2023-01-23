from locators.form_page_locators import FormPageLocators as Locators
from page.base_page import BasePage


class FormPage(BasePage):

    def fill_fields_and_submit(self):
        userName = 'Yulia'
        userSurname = 'Churzina'
        email = 'julchurzina@mail.ru'
        phone = '89056748321'
        self.element_is_visible(Locators.USER_NAME).send_keys(userName)
        self.element_is_visible(Locators.USER_SURNAME).send_keys(userSurname)
        self.element_is_visible(Locators.EMAIL).send_keys(email)
        self.element_is_visible(Locators.PHONE).send_keys('89056748321')
        self.element_is_visible(Locators.SUBMIT).click()
        return userName, userSurname, email, phone

    def form_result(self):
        return
