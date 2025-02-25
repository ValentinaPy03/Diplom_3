
import allure

from conftest import driver
from generators import generate_email_for_recover_password
from pages.recover_password_page import RecoverPasswordPage


class TestRecoverPassword:
    @allure.title("Тест переход на страницу восстановления пароля по кнопке «Восстановить пароль»")
    def test_going_on_recover_password_page(self, driver):
        recover_password = RecoverPasswordPage(driver)

        recover_password.click_button_log_on_main_page()
        recover_password.wait_for_button_input()
        recover_password.click_recover_password()
        recover_password.wait_for_title_recover_password()

        assert recover_password.check_title_recover_password()


    @allure.title("Тест переход на страницу восстановления пароля после ввода Email и клика по Восстановить")
    def test_fill_field_email_and_click_button(self, driver):
        email = generate_email_for_recover_password()
        recover_password = RecoverPasswordPage(driver)

        recover_password.click_button_log_on_main_page()
        recover_password.wait_for_button_input()
        recover_password.click_recover_password()
        recover_password.wait_for_title_recover_password()
        recover_password.fill_field_email(email)
        recover_password.click_button_recover()

        assert recover_password.check_field_password()


    @allure.title("Тест Kлик по кнопке показать/скрыть пароль делает поле активным")
    def test_click_hide_button_to_select_field_password(self, driver):
        email = generate_email_for_recover_password()
        recover_password = RecoverPasswordPage(driver)

        recover_password.click_button_log_on_main_page()
        recover_password.wait_for_button_input()
        recover_password.click_recover_password()
        recover_password.wait_for_title_recover_password()
        recover_password.fill_field_email(email)
        recover_password.click_button_recover()
        recover_password.wait_clickable_button_input()

        recover_password.click_password_visibility_button()

        assert recover_password.check_selected_field_password()

