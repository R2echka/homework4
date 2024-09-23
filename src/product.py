"""Класс продуктов"""


class Product:
    __price: float

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    
    def __str__(self):
        return f'{self.name}, {self.price} руб. Остаток: {self.quantity} шт.'
    
    def __add__(self, other: 'Product'):
        return self.price * self.quantity + other.price * other.quantity


    @property
    def price(self) -> float:
        """Геттер атрибута price"""
        return self.__price

    @price.setter
    def price(self, price: int) -> None:
        """Сеттер атрибута price"""
        if price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = price

    @classmethod
    def new_product(cls, params: dict) -> "Product":
        """Создаёт новый объект класса Product"""
        new_prod = cls(params["name"], params["description"], params["price"], params["quantity"])
        return new_prod
