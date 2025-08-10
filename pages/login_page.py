import allure
from pages.base_page import BasePageMethods
from locators.login_page_locators import LoginPageLocators


class LoginPageMethods(BasePageMethods):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = LoginPageLocators

    @allure.step("Ждем загрузки страницы Входа")
    def wait_for_load_login_page(self):
        return self.is_element_clickable(self.locators.SUBMIT_BUTTON)

    @allure.step("Заполняем поле Email")
    def set_email(self, email):
        self.send_keys(self.locators.EMAIL_INPUT, email)

    @allure.step("Заполняем поле пароль")
    def set_password(self, password):
        self.send_keys(self.locators.PASSWORD_INPUT, password)

    @allure.step("Нажимаем кнопку Войти")
    def click_submit_button(self):
        self.click(self.locators.SUBMIT_BUTTON)

    @allure.step("Заполняем данные для входа и ждем кнопку Войти")
    def set_login_data_and_submit(self, email, password):
        self.wait_for_load_login_page()
        self.set_email(email)
        self.set_password(password)
        self.click_submit_button()
