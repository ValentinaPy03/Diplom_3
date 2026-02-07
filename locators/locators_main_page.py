from selenium.webdriver.common.by import By


class LocatorMainPage:
    BUTTON_PERSONAL_ACC = By.LINK_TEXT, "Личный Кабинет"  # кнопка "Личный кабинет" на главном экране
    BUTTON_LOG_IN_ACCOUNT = By.XPATH, "//button[text()='Войти в аккаунт']"  # кнопка Войти в аккаунт на главном экране
    LOGO_CONSTRUCTOR = By.LINK_TEXT, "Конструктор"  # кнопка Конструктор
    LOGO_ORDER_FEED = By.LINK_TEXT, "Лента Заказов"  # кнопка Лента заказов
    TITLE_ORDER_FEED = By.XPATH, '//h1[text()="Лента заказов"]'
    TITLE_COLLECT_BURGER = By.XPATH, '//h1[text()="Соберите бургер"]'
    INGREDIENT = By.XPATH, ".//a[contains(@href, '/ingredient/') and @draggable='true'][1]"
    COUNTER_INGREDIENTS = By.XPATH, ('//a[@href="/ingredient/61c0c5a71d1f82001bdaaa6d"]/div[@class="counter_counter__ZNLkj counter_default__28sqi"]/p')
    TITLE_DETAILES_INGREDIENT = By.XPATH, '//h2[text()="Детали ингредиента"]' #Заголовок окна с деталями ингредиента
    BUTTON_CLOSE_DETAILES = By.XPATH, '//section[@class="Modal_modal_opened__3ISw4 Modal_modal__P3_V5"]/div/button' # Крестик на форме с деталями
    # ингредиента
    BUTTON_PLACE_ORDER = By.XPATH, "//button[contains(text(), 'Оформить заказ')]"  # кнопка Оформить заказ
    BASKET = By.XPATH, ".//ul[contains(@class, 'BurgerConstructor_basket')]"
    TITLE_ORDER_IS_COOKING = By.XPATH, '//p[@class="undefined text text_type_main-small mb-2"]'
    OVERLAY = By.XPATH, './/div[@class="Modal_modal_overlay__x2ZCr"]/parent::div'

