import allure

from locators.locators_main_page import LocatorMainPage
from locators.locators_order_feed import LocatorsOrderFeed
from pages.base_page import BasePage
from pages.main_page import MainPage
from pages.personal_acc_page import PersonalAcc


class OrderFeedPage(BasePage):

    @allure.title('Дождаться кликабельности лого Лента заказов')
    def wait_for_clickable_logo_feed(self):
        self.wait_for_clickable_element(LocatorsOrderFeed.LOGO_ORDER_FEED)

    @allure.step('Клик на лого Лента заказов')
    def click_on_logo_order_feed(self):
        self.click_on_element(LocatorsOrderFeed.LOGO_ORDER_FEED)

    @allure.step('Дождаться появления заголока Лента заказов')
    def wait_for_title_order_feed(self):
        self.wait_for_element(LocatorsOrderFeed.TITLE_ORDER_FEED)

    @allure.step('Клик на первый в списке заказ')
    def click_on_order(self):
        self.click_on_element(LocatorsOrderFeed.ORDER_IN_LIST)

    @allure.step('Проверить, что окно с деталями появилось')
    def check_popup_details(self):
        return self.check_element_is_displayed(LocatorsOrderFeed.POP_UP_DETAILS_ORDER)

    # @allure.step('Авторизоваться')
    # def create_user_for_order(self, driver, email, password):
    #     pers_acc = PersonalAcc(driver)
    #     PersonalAcc.create_user_for_order(pers_acc, email, password)


    @allure.step('Получить номер заказа')
    def get_order_number(self):
        value = self.get_text_on_element(LocatorsOrderFeed.ORDER_NUMBER)
        return value

    @allure.step("Дождаться пока пропадет оверлей")
    def wait_overlay_disappear(self):
        self.wait_for_element_hide(LocatorsOrderFeed.OVERLAY)

    @allure.step('Клик на крестик')
    def click_hide_button(self):
        self.click_on_element(LocatorsOrderFeed.HIDE_BUTTON)

    @allure.step('Клик на крестик')
    def click_done_order_hide_button(self):
        self.click_on_element(LocatorsOrderFeed.HIDE_BUTTON_DONE_ORDER)

    @allure.step('Получить номер заказа из списка в ленте заказов')
    def get_order_name_on_order_feed(self):
        self.click_on_logo_order_feed()
        self.wait_for_title_order_feed()
        self.click_on_order()
        number = self.get_text_on_element(LocatorsOrderFeed.NAME_ORDER_IN_ORDER_FEED)
        self.click_done_order_hide_button()
        return number

    @allure.step('Получить номер заказа из истории заказа')
    def going_on_order_history(self, driver):
        pers_acc = PersonalAcc(driver)
        PersonalAcc.going_to_history_order(pers_acc)

    def get_number_on_history(self):
        number = self.get_text_on_element(LocatorsOrderFeed.NAME_ORDER_IN_HISTORY_ORDERS)
        return number


    @allure.step('Получить значение Выполнено за все время')
    def get_value_done_all_time(self):
        value = self.get_text_on_element(LocatorsOrderFeed.TITLE_ALL_TIME)
        return value

    @allure.step('Клик на лого Конструктор')
    def click_on_logo_constructor(self):
        self.click_on_element(LocatorsOrderFeed.LOGO_CONSTRUCTOR)

    @allure.step('Получить значение Выполнено за сегодня')
    def get_value_done_today(self):
        value = self.get_text_on_element(LocatorsOrderFeed.TITLE_TODAY)
        return value

    @allure.step('Получить значение Выполнено за сегодня')
    def get_number_order_in_process(self):
        value = self.get_text_on_element(LocatorsOrderFeed.NUMBER_IN_PROCESS)
        return value




