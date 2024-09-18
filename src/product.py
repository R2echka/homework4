"""Класс продуктов"""


class Product:
    __price: float  
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
    
    @property
    def price(self):
        return self.__price
    

    @price.setter
    def price(self, price):
        if price <= 0:
            print('Цена не должна быть нулевая или отрицательная')
        else:
            self.__price = price


    @classmethod
    def new_product(cls, params: dict):
        new_prod = cls(params['name'], params['description'], params['price'], params['quantity'])
        return new_prod