'''Класс продуктов'''
class Product:
    product_count = 0
    def __init__(self, name: str, desc: str, price: float, quantity: int):
        self.name = name
        self.desc = desc
        self.price = price
        self.quantity = quantity
        Product.product_count += 1
