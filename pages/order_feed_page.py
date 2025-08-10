import allure
from pages.base_page import BasePageMethods
from locators.order_feed_page_locators import OrderFeedPageLocators


class OrderFeedPageMethods(BasePageMethods):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = OrderFeedPageLocators

    @allure.step("Ждем открытия страницы Список заказов")
    def wait_for_load_order_feed_page(self):
        return self.is_element_displayed(self.locators.COUNTER_TOTAL_COMPLETED_ORDERS)

    @allure.step("Получаем общее количество заказов")
    def get_quantity_total_completed_orders(self):
        return self.get_text(self.locators.COUNTER_TOTAL_COMPLETED_ORDERS)

    @allure.step("Получаем количество заказов за сегодня")
    def get_quantity_today_completed_orders(self):
        return self.get_text(self.locators.COUNTER_TODAY_COMPLETED_ORDERS)

    @allure.step("Получаем список заказов в работе")
    def get_quantity_in_progress_orders(self):
        return self.get_text(self.locators.LIST_ORDERS_IN_PROGRESS)

    @allure.step("Ждем появления заказа в списке заказов в работе")
    def wait_for_load_order_in_progress(self):
        return self.wait_for_text_to_change(self.locators.LIST_ORDERS_IN_PROGRESS, "Все текущие заказы готовы!")

    @allure.step("Ждем обновления общего количества выполненных заказов")
    def wait_for_load_total_completed_orders(self, old_text):
        return self.wait_for_text_to_change(self.locators.COUNTER_TOTAL_COMPLETED_ORDERS, old_text)

    @allure.step("Ждем обновления количества выполненных заказов за сегодня")
    def wait_for_load_today_completed_orders(self, old_text):
        return self.wait_for_text_to_change(self.locators.COUNTER_TODAY_COMPLETED_ORDERS, old_text)
