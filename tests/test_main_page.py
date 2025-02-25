
import allure
from conftest import *
from pages.main_page import MainPage
from pages.personal_acc_page import PersonalAcc


class TestMainPage:
    @allure.title("Тест переход по клику на вкладку Лента заказов")
    def test_going_to_order_feed(self, driver):
        main_page = MainPage(driver)

        main_page.main_page_wait_loading()
        main_page.click_button_orders_feed()
        main_page.wait_for_loading_orders_feed()

        assert main_page.check_title_orders_feed()

    @allure.title("Тест переход по клику на вкладку Конструктор")
    def test_going_to_constructor(self, driver):
        main_page = MainPage(driver)

        main_page.main_page_wait_loading()
        main_page.click_button_orders_feed()
        main_page.wait_for_loading_orders_feed()
        main_page.click_button_constructor()
        main_page.wait_for_loading_constructor()

        assert main_page.check_title_collect_burger()

    @allure.title("Тест Появляется окно с деталями ингредиента при клике на ингредиент")
    def test_appears_details_by_click_on_ingredient(self, driver):
        main_page = MainPage(driver)

        main_page.main_page_wait_loading()
        main_page.wait_for_clicable_ingregient()
        main_page.click_on_ingredients()
        main_page.wait_for_loading_details()

        assert main_page.check_title_details()

    @allure.title("Тест Всплыающее окнос деталями закрывается по клику на крестик")
    def test_details_closed_by_hide_button(self, driver):
        main_page = MainPage(driver)

        main_page.main_page_wait_loading()
        main_page.wait_for_clicable_ingregient()
        main_page.click_on_ingredients()
        main_page.wait_for_loading_details()
        main_page.click_on_hide_button()

        assert main_page.check_title_details_disappear()

    @allure.title("Тест Каунтер ингредиента увеличивается при добавлении его в корзину")
    def test_drag_and_drop_ingredient_increases_counter(self, driver):
        main_page = MainPage(driver)
        main_page.main_page_wait_loading()
        main_page.drag_and_drop_ingredient()
        expected_counter_value = "2"
        actual_counter_value = main_page.get_value_of_counter(driver)

        assert expected_counter_value == actual_counter_value

    @allure.title("Авторизованный пользователь может оформить заказ")
    def test_place_order(self, driver, user_method, generate_user_data):
        main_page = MainPage(driver)
        pers_acc = PersonalAcc(driver)
        with allure.step("Создаем пользователя через API метод"):
            user_method.create_user(generate_user_data[0])
        pers_acc.create_user_for_order(generate_user_data[1], generate_user_data[2])
        main_page.drag_and_drop_ingredient()
        main_page.click_on_place_order()
        main_page.wait_for_loading_order_number()

        assert main_page.check_title_order_is_cooking()

