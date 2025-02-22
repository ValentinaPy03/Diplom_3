from selenium.webdriver.common.by import By


class LocatorsRecoverPasswordPage:
    BUTTON_INPUT = By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']"  # кнопка Войти на
    # форме Вход
    BUTTON_RECOVER_PASSWORD = By.XPATH, "//a[text()='Восстановить пароль']"  # кнопка Восстановить пароль на форме входа
    FIELD_EMAIL = By.XPATH, '//input[@class="text input__textfield text_type_main-default"]' # поле Email на форме восстановления пароля
    BUTTON_RECOVER = By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]' # кнопка Восстановить на форме Восстановления пароля
    TITLE_RECOVER_PASSWORD = By.XPATH, '//h2[text()="Восстановление пароля"]'
    FIELD_PASSWORD = By.XPATH, '//input[@name="Введите новый пароль"]' # поле Password на форме восстановления пароля
    FIELD_KEY = By.XPATH, '//input[@name="name"]' # поле Код из письма на форме восстановления пароля
    HIDE_BUTTON = By.XPATH,  '//div[@class="input__icon input__icon-action"]/*[name()="svg"]'
    SELECTED_FIELD_PASSWORD = By.XPATH, '//div[@class="input pr-6 pl-6 input_type_text input_size_default input_status_active"]'