import allure
from conftest import *
from pages.personal_acc_page import PersonalAcc


class TestPersonalAcc:

    @allure.title("Тест Переход в Личный кабинет по кнопке на глпаной странице")
    def test_going_to_pers_acc(self, driver, user_method, generate_user_data):
        personal_acc = PersonalAcc(driver)
        with allure.step("Создаем пользователя через API метод"):
            user_method.create_user(generate_user_data[0])
        personal_acc.click_personal_acc()
        personal_acc.wait_for_button_input()
        personal_acc.fill_field_email(generate_user_data[1])
        personal_acc.fill_field_password(generate_user_data[2])
        personal_acc.click_button_input()
        personal_acc.wait_for_button_place_order()
        personal_acc.wait_for_clickable_pers_acc()
        personal_acc.click_button_personal_acc()
        personal_acc.wait_for_personal_acc()

        assert personal_acc.check_button_history_orders()

    @allure.title("Тест Переход в раздел История заказов в Личном кабинете")
    def test_going_to_history_orders(self, driver, user_method, generate_user_data):
        personal_acc = PersonalAcc(driver)
        with allure.step("Создаем пользователя через API метод"):
            user_method.create_user(generate_user_data[0])
        personal_acc.click_personal_acc()
        personal_acc.wait_for_button_input()
        personal_acc.fill_field_email(generate_user_data[1])
        personal_acc.fill_field_password(generate_user_data[2])
        personal_acc.click_button_input()
        personal_acc.wait_for_button_place_order()
        personal_acc.wait_for_clickable_pers_acc()

        personal_acc.click_button_personal_acc()
        personal_acc.click_button_history_orders()
        personal_acc.wait_for_title_download_disappear()

        assert personal_acc.check_list_orders()

    @allure.title("Тест Выход из аккаунта")
    def test_going_to_pers_acc(self, driver, user_method, generate_user_data):
        personal_acc = PersonalAcc(driver)
        with allure.step("Создаем пользователя через API метод"):
            user_method.create_user(generate_user_data[0])
        personal_acc.click_personal_acc()
        personal_acc.wait_for_button_input()
        personal_acc.fill_field_email(generate_user_data[1])
        personal_acc.fill_field_password(generate_user_data[2])
        personal_acc.click_button_input()
        personal_acc.wait_for_button_place_order()
        personal_acc.wait_for_clickable_pers_acc()

        personal_acc.click_button_personal_acc()
        personal_acc.wait_for_clickable_button_logout()
        personal_acc.click_button_logout()
        personal_acc.wait_for_button_input()

        assert personal_acc.check_button_input()


