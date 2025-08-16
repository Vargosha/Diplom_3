class HomePageLocators:
    CONSTRUCTOR_BUTTON = ("xpath", ".//p[text() = 'Конструктор']") # Кнопка Конструктор
    ORDER_FEED_BUTTON = ("xpath", ".//p[text() = 'Лента Заказов']") # Кнопка Лента Заказов
    INGREDIENTS_BUTTONS = ("xpath", "(.//div[@class = 'counter_counter__ZNLkj counter_default__28sqi'])") # Кнопки ингредиентов
    BUNS_BUTTONS = ("xpath", ".//p[contains(text(), 'булка')]") # Кнопки булок
    CROSS_BUTTON_INGREDIENT_INFO = ("xpath", ".//section[@class = 'Modal_modal_opened__3ISw4 Modal_modal__P3_V5']//button") # Кнопка Крестик для закрытия окна информации об ингредиенте
    COUNTER_ON_INGREDIENT = ("xpath", "(.//p[@class = 'counter_counter__num__3nue1'])") # Счетчик на ингредиенте
    CART_SECTION = ("xpath", ".//section[@class = 'BurgerConstructor_basket__29Cd7 mt-25 ']") # Секция корзины
    SUBMIT_ORDER_BUTTON = ("xpath", ".//button[text() = 'Оформить заказ']") # Кнопка Оформить заказ
    CROSS_BUTTON_ORDER_CONFIRM = ("xpath", ".//section[@class = 'Modal_modal_opened__3ISw4 Modal_modal__P3_V5']//button") # Кнопка Крестик для закрытия окна оформленного заказа
    ORDER_NUMBER = ("xpath", ".//h2[@class = 'Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8']") # Номер созданного заказа
    OVERLAY = ("xpath", ".//section//div[@class='Modal_modal_overlay__x2ZCr']") # Оверлей
