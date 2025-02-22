from selenium.webdriver.common.by import By


class LocatorsOrderFeed:
    LOGO_ORDER_FEED = By.LINK_TEXT, "Лента Заказов"  # кнопка Лента заказов
    TITLE_ORDER_FEED = By.XPATH, '//h1[text()="Лента заказов"]'
    ORDER_IN_LIST = By.XPATH, '//ul[@class="OrderFeed_list__OLh59"]/li' # Первый заказ в списке заказов
    POP_UP_DETAILS_ORDER = By.XPATH, '//section[@class="Modal_modal_opened__3ISw4 Modal_modal__P3_V5"]/div[@class="Modal_modal__container__Wo2l_"]' # всплывающее окно с деталями
    NAME_ORDER_IN_HISTORY_ORDERS = By.XPATH, '//a[@class="OrderHistory_link__1iNby"]/h2'
    NAME_ORDER_IN_ORDER_FEED = By.XPATH, '//div[@class="Modal_orderBox__1xWdi Modal_modal__contentBox__sCy8X p-10"]/h2'
    TITLE_ALL_TIME = By.XPATH, '//p[@class="OrderFeed_number__2MbrQ text text_type_digits-large"]'
    TITLE_TODAY = By.XPATH, '//div[@class="OrderFeed_ordersData__1L6Iv"]/div[3]/p[@class="OrderFeed_number__2MbrQ text text_type_digits-large"]'
    TITLE_IN_PROCESS = By.XPATH, '//div[@class="OrderFeed_orderStatusBox__1d4q2 mb-15"]/p[@class="text text_type_main-medium"][2]'
    OVERLAY = By.XPATH, './/div[@class="Modal_modal_overlay__x2ZCr"]/parent::div'
    HIDE_BUTTON =By.XPATH, '//button[@class="Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK"]'
    HIDE_BUTTON_DONE_ORDER = By.XPATH, '//section[@class="Modal_modal_opened__3ISw4 Modal_modal__P3_V5"]/div/button'
    LOGO_CONSTRUCTOR = By.LINK_TEXT, "Конструктор"  # кнопка Конструктор
    NUMBER_IN_PROCESS = By.XPATH, '//ul[@class="OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi"]/li[@class="text text_type_digits-default mb-2"]'
    ORDER_NUMBER = By.XPATH, '//h2[@class="Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8"]'