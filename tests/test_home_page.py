import allure
from helpers.urls import HOME_PAGE_URL, ORDER_FEED_PAGE_URL


class TestHomePage:
    @allure.title("Проверка редиректа на главную страницу при нажатии на кнопку Конструктор")
    def test_user_redirected_to_constructor_when_clicking_constructor_button(self, unregistered_user):
        unregistered_user.click_order_feed_button()
        unregistered_user.click_constructor_button()

        assert unregistered_user.get_current_url() == HOME_PAGE_URL

    @allure.title("Проверка редиректа на главную страницу при нажатии на кнопку Список заказов")
    def test_user_redirected_to_order_feed_when_clicking_order_feed_button(self, unregistered_user):
        unregistered_user.click_order_feed_button()

        assert unregistered_user.get_current_url() == ORDER_FEED_PAGE_URL

    @allure.title("Проверка появления всплывающего окна с информацией об ингредиенте при клике на ингредиент")
    def test_click_ingredient_shows_popup_ingredient_window(self, unregistered_user):
        ingredient = unregistered_user.get_random_ingredient()[0]

        unregistered_user.click_ingredient(ingredient)

        assert unregistered_user.check_popup_ingredient_window_is_enabled()

    @allure.title("Проверка закрытия всплывающего окна с информацией об ингредиенте кликом по крестику")
    def test_click_cross_close_popup_ingredient_window(self, unregistered_user):
        ingredient = unregistered_user.get_random_ingredient()[0]
        unregistered_user.click_ingredient(ingredient)
        unregistered_user.wait_for_popup_ingredient_window()

        unregistered_user.click_cross_button_ingredient_info()

        assert unregistered_user.check_popup_ingredient_window_is_enabled() == False

    @allure.title("Проверка при добавлении ингредиента в заказ счётчик этого ингредиента увеличивается")
    def test_ingredient_counter_increases_when_added_to_order(self, unregistered_user):
        ingredient, index = unregistered_user.get_random_ingredient()
        unregistered_user.drag_and_drop_ingredient_to_cart(ingredient)

        assert unregistered_user.get_quantity_from_ingredient_counter(index) > 0
