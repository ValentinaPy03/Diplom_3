import allure

from locators.locators_main_page import LocatorMainPage
from locators.locators_personal_acc import LocatorsPersonalAcc
from locators.locators_recover_password_page import LocatorsRecoverPasswordPage
from pages.base_page import BasePage
from conftest import driver


class PersonalAcc(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step("Клик на кнопке Личный кабинет на главной странице")
    def click_personal_acc(self):
        self.click_on_element(LocatorMainPage.BUTTON_PERSONAL_ACC)

    @allure.step("Дождать загрузки страницы регистрации")
    def wait_for_button_input(self):
        self.wait_for_element(LocatorsRecoverPasswordPage.BUTTON_INPUT)

    @allure.step("Заполнить поле Email")
    def fill_field_email(self, email):
        self.send_keys_to_input(LocatorsPersonalAcc.FIELD_EMAIL_LOG, email)

    @allure.step("Заполнить поле Пароль")
    def fill_field_password(self, password):
        self.send_keys_to_input(LocatorsPersonalAcc.FIELD_PASSWORD_LOG, password)

    @allure.step("Клик на кнопку Вход")
    def click_button_input(self):
        self.click_on_element(LocatorsPersonalAcc.BUTTON_INPUT)

    @allure.step("Дождать загрузки главной страницы (кнопки Оформить заказ)")
    def wait_for_button_place_order(self):
        self.wait_for_element(LocatorsPersonalAcc.BUTTON_PLACE_ORDER)

    def wait_for_clickable_button_place_order(self):
        self.wait_for_clickable_element(LocatorsPersonalAcc.BUTTON_PLACE_ORDER)

    def create_user_for_order(self, email, password):
        self.click_personal_acc()
        self.wait_for_button_input()
        self.fill_field_email(email)
        self.fill_field_password(password)
        self.click_button_input()
        self.wait_for_button_place_order()

    @allure.step("Клик на кнопке Личный кабинет на главной странице при уже авторизованном пользователе")
    def click_button_personal_acc(self):
        self.click_on_element(LocatorsPersonalAcc.BUTTON_PERSONAL_ACC)

    @allure.step("Дождать загрузки страницы Личного кабинета")
    def wait_for_personal_acc(self):
        self.wait_for_element(LocatorsPersonalAcc.BUTTON_HISTORY_ORDERS)

    @allure.step("Проверить, что кнопка История заказов есть на странице")
    def check_button_history_orders(self):
        return self.check_element_is_displayed(LocatorsPersonalAcc.BUTTON_HISTORY_ORDERS)

    @allure.step("Клик на кнопку История заказов")
    def click_button_history_orders(self):
        self.click_on_element(LocatorsPersonalAcc.BUTTON_HISTORY_ORDERS)

    @allure.step("Дождаться пока пропадет надпись Загрузка")
    def wait_for_title_download_disappear(self):
        self.wait_for_not_element(LocatorsPersonalAcc.TITLE_DOWNLOAD)

    @allure.step('Перейти в историю заказов')
    def going_to_history_order(self):
        self.click_button_personal_acc()
        self.wait_for_personal_acc()
        self.click_button_history_orders()
        self.wait_for_title_download_disappear()

    @allure.step("Проверить, что появилась история заказов")
    def check_list_orders(self):
        return self.check_element_is_displayed(LocatorsPersonalAcc.LIST_ORDERS)

    @allure.step("Клик на кнопку Выход")
    def click_button_logout(self):
        self.click_on_element(LocatorsPersonalAcc.BUTTON_LOGOUT)

    def wait_for_clickable_button_logout(self):
        self.wait_for_clickable_element(LocatorsPersonalAcc.BUTTON_LOGOUT)

    @allure.step("Проверить, что появилась кнопка Войти")
    def check_button_input(self):
        return self.check_element_is_displayed(LocatorsPersonalAcc.BUTTON_INPUT)

    @allure.step("Дождаться кликабельности ЛК")
    def wait_for_clickable_pers_acc(self):
        self.wait_for_clickable_element(LocatorsPersonalAcc.BUTTON_PERSONAL_ACC)

    @allure.step("Дождаться загрузки главной страницы")
    def main_page_wait_loading(self):
        self.wait_for_element_hide(LocatorsPersonalAcc.OVERLAY)









