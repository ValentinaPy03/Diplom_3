import time
import allure
from conftest import *
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from pages.personal_acc_page import PersonalAcc


class TestOrderFeed:
    @allure.title('По клику на заказ откроется всплывающее окно с деталями')
    def test_open_popup_details_by_click_on_order(self, driver):
        order_feed = OrderFeedPage(driver)
        order_feed.click_on_logo_order_feed()
        order_feed.wait_for_title_order_feed()
        order_feed.click_on_order()

        assert order_feed.check_popup_details()

    @allure.title('Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_user_orders_mirrored_in_feed(self, driver, user_method, generate_user_data):
        order_feed = OrderFeedPage(driver)
        main_page = MainPage(driver)
        pers_acc = PersonalAcc(driver)
        with allure.step("Создаем пользователя через API метод"):
            user_method.create_user(generate_user_data[0])
        pers_acc.create_user_for_order (generate_user_data[1], generate_user_data[2])

        main_page.place_order()
        order_feed.wait_overlay_disappear()
        order_feed.click_hide_button()
        order_feed.wait_for_clickable_logo_feed()
        number_on_feed = order_feed.get_order_name_on_order_feed()

        order_feed.going_on_order_history(driver)
        number_on_history = order_feed.get_number_on_history()

        assert number_on_feed == number_on_history

    @pytest.mark.parametrize(
        "get_counter_method",
        [
            "get_value_done_all_time",
            "get_value_done_today"
        ],
    )
    @allure.title('счётчик Выполнено за сегодня/за все время увеличивается при создании нвоого заказа')
    def test_counter_all_tme_increases_by_place_new_order(self, driver, user_method, generate_user_data, get_counter_method):
        order_feed = OrderFeedPage(driver)
        with allure.step("Создаем пользователя через API метод"):
            user_method.create_user(generate_user_data[0])
        order_feed.create_user_for_order(driver, generate_user_data[1], generate_user_data[2])
        order_feed.wait_overlay_disappear()
        order_feed.click_on_logo_order_feed()

        get_counter = getattr(order_feed, get_counter_method)
        counter_after = int(get_counter())

        order_feed.click_on_logo_constructor()
        order_feed.place_order(driver)
        order_feed.wait_overlay_disappear()
        order_feed.click_hide_button()

        order_feed.click_on_logo_order_feed()
        counter_before = int(get_counter())

        assert counter_before - counter_after == 1

    @allure.title('Тест Номер заказа появляется в списке В процессе')
    def test_order_number_appear_in_list_in_process(self, driver, user_method, generate_user_data):
        order_feed = OrderFeedPage(driver)
        with allure.step("Создаем пользователя через API метод"):
            user_method.create_user(generate_user_data[0])
        order_feed.create_user_for_order(driver, generate_user_data[1], generate_user_data[2])
        order_feed.place_order(driver)
        order_feed.wait_overlay_disappear()
        number_order = f'0{order_feed.get_order_number()}'
        order_feed.click_hide_button()

        order_feed.click_on_logo_order_feed()
        order_feed.wait_for_title_order_feed()
        number_in_process = order_feed.get_number_order_in_process()

        assert number_order == number_in_process



