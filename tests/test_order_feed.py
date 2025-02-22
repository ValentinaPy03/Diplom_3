import time
import allure
from conftest import *
from pages.order_feed_page import OrderFeedPage


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
        with allure.step("Создаем пользователя через API метод"):
            user_method.create_user(generate_user_data[0])
        order_feed.create_user_for_order(driver, generate_user_data[1], generate_user_data[2])

        order_feed.place_order(driver)
        order_feed.wait_overlay_disappear()
        time.sleep(5)
        order_feed.click_hide_button()
        number_on_feed = order_feed.get_order_name_on_order_feed()

        order_feed.going_on_order_history(driver)
        number_on_history = order_feed.get_number_on_history()

        assert number_on_feed == number_on_history

    @allure.title('счётчик Выполнено за сегодня увеличивается при создании нвоого заказа')
    def test_counter_all_tme_increases_by_place_new_order(self, driver, user_method, generate_user_data):
        order_feed = OrderFeedPage(driver)
        with allure.step("Создаем пользователя через API метод"):
            user_method.create_user(generate_user_data[0])
        order_feed.create_user_for_order(driver, generate_user_data[1], generate_user_data[2])
        order_feed.wait_overlay_disappear()
        order_feed.click_on_logo_order_feed()
        counter_after = int(order_feed.get_value_done_all_time())

        order_feed.click_on_logo_constructor()
        order_feed.place_order(driver)
        order_feed.wait_overlay_disappear()
        order_feed.click_hide_button()

        order_feed.click_on_logo_order_feed()
        counter_before = int(order_feed.get_value_done_all_time())

        assert counter_before - counter_after == 1

    @allure.title('счётчик Выполнено за все время увеличивается при создании нвоого заказа')
    def test_counter_today_increases_by_place_new_order(self, driver, user_method, generate_user_data):
        order_feed = OrderFeedPage(driver)
        with allure.step("Создаем пользователя через API метод"):
            user_method.create_user(generate_user_data[0])
        order_feed.create_user_for_order(driver, generate_user_data[1], generate_user_data[2])
        order_feed.wait_overlay_disappear()
        order_feed.click_on_logo_order_feed()
        counter_after = int(order_feed.get_value_done_today())

        order_feed.click_on_logo_constructor()
        order_feed.place_order(driver)
        order_feed.wait_overlay_disappear()
        time.sleep(5)
        order_feed.click_hide_button()

        order_feed.click_on_logo_order_feed()
        counter_before = int(order_feed.get_value_done_today())

        assert counter_before - counter_after == 1

    @allure.title('')
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



