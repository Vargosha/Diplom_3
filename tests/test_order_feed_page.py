import allure
from pages.order_feed_page import OrderFeedPageMethods


class TestOrderFeedPage:
    @allure.title("Проверка после оформления заказа его номер появляется в разделе «В работе»")
    def test_order_appears_in_progress_after_creation_order(self, registered_user, create_order):
        homepage = registered_user
        order_feed_page = OrderFeedPageMethods(homepage.driver)
        order_number = create_order

        homepage.click_order_feed_button()
        order_feed_page.wait_for_load_order_feed_page()

        order_feed_page.wait_for_load_order_in_progress()
        orders_list = order_feed_page.get_quantity_in_progress_orders()

        assert order_number in orders_list

    @allure.title("Проверка при создании нового заказа счётчик «Выполнено за всё время» увеличивается")
    def test_total_completed_orders_counter_increases_after_creation_order(self, registered_user, get_orders_quantity, create_order):
        homepage = registered_user
        order_feed_page = OrderFeedPageMethods(homepage.driver)
        total_orders_before = get_orders_quantity[0]

        registered_user.click_order_feed_button()
        order_feed_page.wait_for_load_order_feed_page()

        order_feed_page.wait_for_load_total_completed_orders(total_orders_before)
        total_orders_after = order_feed_page.get_quantity_total_completed_orders()

        assert int(total_orders_after) == int(total_orders_before) + 1


    @allure.title("Проверка при создании нового заказа счётчик «Выполнено за сегодня» увеличивается")
    def test_today_completed_orders_counter_increases_after_creation_order(self, registered_user, get_orders_quantity, create_order):
        homepage = registered_user
        order_feed_page = OrderFeedPageMethods(homepage.driver)
        today_orders_before = get_orders_quantity[1]

        registered_user.click_order_feed_button()
        order_feed_page.wait_for_load_order_feed_page()

        order_feed_page.wait_for_load_today_completed_orders(today_orders_before)
        today_orders_after = order_feed_page.get_quantity_today_completed_orders()

        assert int(today_orders_after) == int(today_orders_before) + 1
