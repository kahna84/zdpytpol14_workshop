import abc


class BaseProduct(abc.ABC):

    def __init__(self, price: float, quantity: int, name: str) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return self.name


class Product(BaseProduct):
    pass
