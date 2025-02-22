import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.locators_main_page import LocatorMainPage
from pages.base_page import BasePage
from conftest import driver
from pages.personal_acc_page import PersonalAcc

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step("Дождаться загрузки главной страницы")
    def main_page_wait_loading(self):
        self.wait_for_element_hide(LocatorMainPage.OVERLAY)

    @allure.step("клик на раздел Лента заказов")
    def click_button_orders_feed(self):
        self.click_on_element(LocatorMainPage.LOGO_ORDER_FEED)

    @allure.step("Дождаться закрузки раздела Лента заказов")
    def wait_for_loading_orders_feed(self):
        self.wait_for_element(LocatorMainPage.TITLE_ORDER_FEED)

    @allure.step("проверить, что заголовок Лента заказов на странице")
    def check_title_orders_feed(self):
        return self.check_element_is_displayed(LocatorMainPage.TITLE_ORDER_FEED)

    @allure.step("клик на лого Конструктор")
    def click_button_constructor(self):
        self.click_on_element(LocatorMainPage.LOGO_CONSTRUCTOR)

    @allure.step("Дождаться закрузки раздела Конструктор")
    def wait_for_loading_constructor(self):
        self.wait_for_element(LocatorMainPage.TITLE_COLLECT_BURGER)

    @allure.step("проверить, что заголовок Соберите бургер на странице")
    def check_title_collect_burger(self):
        return self.check_element_is_displayed(LocatorMainPage.TITLE_COLLECT_BURGER)

    @allure.step('Клик на первый игредиент')
    def click_on_ingredients(self):
        self.click_on_element(LocatorMainPage.INGREDIENT)

    @allure.step("Дождаться закрузки карточки с деталями ингредиента")
    def wait_for_loading_details(self):
        self.wait_for_element(LocatorMainPage.TITLE_DETAILES_INGREDIENT)

    @allure.step("проверить, что заголовок Детали игредиента на странице")
    def check_title_details(self):
        return self.check_element_is_displayed(LocatorMainPage.TITLE_DETAILES_INGREDIENT)

    @allure.step('Клик на крестик на всплывающем окне')
    def click_on_hide_button(self):
        self.click_on_element(LocatorMainPage.BUTTON_CLOSE_DETAILES)

    @allure.step("проверить, что заголовок Детали игредиента не на странице")
    def check_title_details_disappear(self):
        if self.wait_for_element_hide(LocatorMainPage.TITLE_DETAILES_INGREDIENT):
            return True

    @allure.step('Перетащить ингредиент в корзину')
    def drag_and_drop_ingredient(self):
        self.drag_and_drop_on_element(LocatorMainPage.INGREDIENT, LocatorMainPage.BASKET)

    @allure.step('Получить значение каунтера ингредиента')
    def get_value_of_counter(self, driver):
        counter_element = WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(LocatorMainPage.COUNTER_INGREDIENTS))
        return counter_element.text

    @allure.step('Клик на кнопку Оформить заказ')
    def click_on_place_order(self):
        self.click_on_element(LocatorMainPage.BUTTON_PLACE_ORDER)

    @allure.step("Дождаться закрузки карточки с номером заказа")
    def wait_for_loading_order_number(self):
        self.wait_for_element(LocatorMainPage.TITLE_ORDER_IS_COOKING)

    @allure.step("проверить, что надпись Ваш заказ начали готовить на странице")
    def check_title_order_is_cooking(self):
        return self.check_element_is_displayed(LocatorMainPage.TITLE_ORDER_IS_COOKING)

    @allure.step("Дождаться кликабельности ингредиента")
    def wait_for_clicable_ingregient(self):
        self.wait_for_clickable_element(LocatorMainPage.INGREDIENT)

    @allure.step('Авторизироваться')
    def create_user_for_order(self, driver, email, password):
        pers_acc = PersonalAcc(driver)
        PersonalAcc.create_user_for_order(pers_acc, email=email, password=password)

    @allure.step('Оформить заказ')
    def place_order(self):
        self.drag_and_drop_ingredient()
        self.click_on_place_order()
        self.wait_for_loading_order_number()


