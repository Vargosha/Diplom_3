class OrderFeedPageLocators:
    COUNTER_TOTAL_COMPLETED_ORDERS = ("xpath", "(.//p[@class = 'OrderFeed_number__2MbrQ text text_type_digits-large'])[1]") # Счетчик заказов Выполненных за все время
    COUNTER_TODAY_COMPLETED_ORDERS = ("xpath", "(.//p[@class = 'OrderFeed_number__2MbrQ text text_type_digits-large'])[2]") # Счетчик заказов Выполненных за сегодня
    LIST_ORDERS_IN_PROGRESS = ("xpath", ".//ul[@class = 'OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi']/li") # Список заказов в работе
