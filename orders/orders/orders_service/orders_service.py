# IMPLEMENT THE INTERFACE OF ORDER SERVICE CLASS

from repository.orders_repository import OrdersRepository
from orders_service.exceptions import OrderNotFoundError


class OrdersService:
    def __init__(self, orders_repository: OrdersRepository):
        # To instantiate the order service class, required orders_repository instance
        self.orders_repository = orders_repository

    def place_order(self, items):
        return self.orders_repository.add(items)

    def get_order(self, order_id):
        pass

    def update_order(self, order_id, items):
        pass

    def list_order(self, **filters):
        pass

    def pay_order(self, order_id):
        pass

    def cancel_order(self, order_id):
        pass
