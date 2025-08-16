import allure
from pages.base_page import BasePageMethods
from locators.home_page_locators import HomePageLocators
import random


class HomePageMethods(BasePageMethods):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = HomePageLocators()

    @allure.step("Ждем загрузки главной страницы")
    def wait_for_load_home_page(self):
        return self.is_element_clickable(self.locators.INGREDIENTS_BUTTONS)

    @allure.step("Нажимаем на кнопку Конструктор")
    def click_constructor_button(self):
        self.click(self.locators.CONSTRUCTOR_BUTTON)

    @allure.step("Нажимаем на кнопку Лента заказов")
    def click_order_feed_button(self):
        self.click(self.locators.ORDER_FEED_BUTTON)

    @allure.step("Ждем появления высплавающего окна с информацией об ингредиенте")
    def wait_for_popup_ingredient_window(self):
        return self.is_element_clickable(self.locators.CROSS_BUTTON_INGREDIENT_INFO)

    @allure.step("Ждем появления высплавающего окна с подтверждением заказа")
    def wait_for_popup_order_confirm_window(self):
        return self.is_element_clickable(self.locators.CROSS_BUTTON_ORDER_CONFIRM)

    @allure.step("Проверяем появление всплывающего окна с информацией об ингредиенте")
    def check_popup_ingredient_window_is_enabled(self):
        return self.is_element_displayed(self.locators.CROSS_BUTTON_INGREDIENT_INFO)

    @allure.step("Нажимаем на крестик в всплывающем окне информации об ингредиенте")
    def click_cross_button_ingredient_info(self):
        self.click(self.locators.CROSS_BUTTON_INGREDIENT_INFO)

    @allure.step("Нажимаем на крестик в всплывающем окне подтверждения заказа")
    def click_cross_button_order_confirm(self):
        self.click(self.locators.CROSS_BUTTON_ORDER_CONFIRM)

    @allure.step("Получаем количество ингредиентов с счетчика")
    def get_quantity_from_ingredient_counter(self, index):
        counters = self.find_elements(self.locators.COUNTER_ON_INGREDIENT)
        return int(counters[index].text)

    @allure.step("Выбираем случайную булку")
    def get_random_bun(self):
        bun = self.find_elements(self.locators.BUNS_BUTTONS)
        index = random.randrange(len(bun))
        return bun[index]

    @allure.step("Выбираем случайный ингредиент")
    def get_random_ingredient(self):
        ingredients = self.find_elements(self.locators.INGREDIENTS_BUTTONS)
        index = random.randrange(len(ingredients))
        return ingredients[index], index

    @allure.step("Кликаем на ингредиент")
    def click_ingredient(self, ingredient):
        self.click(ingredient)

    @allure.step("Перетаскиваем ингредиент в корзину")
    def drag_and_drop_ingredient_to_cart(self, ingredient):
        self.scroll_into_view(ingredient)
        cart = self.find_element(self.locators.CART_SECTION)
        self.dnd_element_to_target(ingredient, cart)

    @allure.step("Нажимаем на кнопку Оформить заказ")
    def click_submit_order_button(self):
        self.click(self.locators.SUBMIT_ORDER_BUTTON)

    @allure.step("Ждем появления номера созданного заказа")
    def wait_for_load_order_number(self):
        return self.wait_for_text_to_change(self.locators.ORDER_NUMBER, "9999")

    @allure.step("Получаем номер созданного заказа")
    def get_order_number(self):
        return self.get_text(self.locators.ORDER_NUMBER)

    @allure.step("Ждем закрытия оверлея")
    def wait_for_overlay_close(self):
        return self.is_element_invisible(self.locators.OVERLAY)
