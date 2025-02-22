import allure

from locators.locators_main_page import LocatorMainPage
from locators.locators_recover_password_page import LocatorsRecoverPasswordPage
from pages.base_page import BasePage
from conftest import driver

class RecoverPasswordPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step("Клик по кнопке Войти в аккаунт на главном экране")
    def click_button_log_on_main_page(self):
        self.click_on_element(LocatorMainPage.BUTTON_LOG_IN_ACCOUNT)

    @allure.step("Дождать загрузки страницы регистрации")
    def wait_for_button_input(self):
        self.wait_for_element(LocatorsRecoverPasswordPage.BUTTON_INPUT)

    @allure.step("Клик по Восстановить пароль внизу страницы")
    def click_recover_password(self):
        self.click_on_element(LocatorsRecoverPasswordPage.BUTTON_RECOVER_PASSWORD)

    @allure.step("Дождаться появления заголовка Восстановление пароля")
    def wait_for_title_recover_password(self):
        self.wait_for_element(LocatorsRecoverPasswordPage.TITLE_RECOVER_PASSWORD)

    @allure.step("Проверить, что заголовок есть на странице")
    def check_title_recover_password(self):
        return self.check_element_is_displayed(LocatorsRecoverPasswordPage.TITLE_RECOVER_PASSWORD)

    @allure.step("Заполнить пое Email")
    def fill_field_email(self, email):
        self.send_keys_to_input(LocatorsRecoverPasswordPage.FIELD_EMAIL, email)

    @allure.step("Клик по кнопке Восстановить")
    def click_button_recover(self):
        self.click_on_element(LocatorsRecoverPasswordPage.BUTTON_RECOVER)

    @allure.step("Дождаться появления поля Пароль")
    def wait_for_field_password(self):
        self.wait_for_element(LocatorsRecoverPasswordPage.FIELD_PASSWORD)

    @allure.step("Проверить, что на странице плявилось поле Пароль")
    def check_field_password(self):
        return self.check_element_is_displayed(LocatorsRecoverPasswordPage.FIELD_PASSWORD)

    @allure.step("Проверить, что кнопка видимости кликабельна")
    def wait_clickable_hide_button(self):
        self.wait_for_clickable_element(LocatorsRecoverPasswordPage.HIDE_BUTTON)

    @allure.step("Клик по кнопке показать/скрыть пароль")
    def click_password_visibility_button(self):
        self.click_on_element(LocatorsRecoverPasswordPage.HIDE_BUTTON)

    @allure.step("Проверить, что поле пароль выделено")
    def check_selected_field_password(self):
        return self.check_element_is_displayed(LocatorsRecoverPasswordPage.SELECTED_FIELD_PASSWORD)
