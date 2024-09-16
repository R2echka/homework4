'''Класс продуктов'''
class Product:
    def __init__(self, name: str, desc: str, price: float, quantity: int):
        self.name = name
        self.desc = desc
        self.price = price
        self.quantity = quantity
