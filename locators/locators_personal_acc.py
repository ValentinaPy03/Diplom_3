from selenium.webdriver.common.by import By


class LocatorsPersonalAcc:
    BUTTON_PERSONAL_ACC = By.LINK_TEXT, "Личный Кабинет"
    FIELD_EMAIL_LOG = By.XPATH, "//input[@name='name']"  # поле Email на форме Вход
    FIELD_PASSWORD_LOG = By.XPATH, "//input[@name='Пароль']"  # поле Пароль на форме Вход
    BUTTON_INPUT = By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']"  # кнопка Войти на
    # форме Вход
    BUTTON_PLACE_ORDER = By.XPATH, "//button[contains(text(), 'Оформить заказ')]"  # кнопка Оформить заказ
    BUTTON_HISTORY_ORDERS = By.LINK_TEXT, 'История заказов'
    LIST_ORDERS = By.XPATH, '//a[@class="Account_link__2ETsJ text text_type_main-medium text_color_inactive Account_link_active__2opc9"]'
    TITLE_DOWNLOAD = By.XPATH, '//div[@class="App_centeredComponent__tXJuB text text_type_main-large"]' # колесико Загрузка
    BUTTON_LOGOUT = By.XPATH, '//button[@class="Account_button__14Yp3 text text_type_main-medium text_color_inactive"]'
    BUTTON_SAVE = By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]'
    OVERLAY = By.XPATH, '//div[@class="Modal_modal_overlay__x2ZCr"]'