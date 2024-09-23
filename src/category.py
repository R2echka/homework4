# import os, sys
# sys.path.append(os.getcwd())
from src.product import Product

"""Класс категорий"""


class Category:
    __products: list
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.__products = products
        self.product_count += len(products)
        Category.category_count += 1

    def __str__(self) -> str:
        return f"{self.name}, количество продуктов: {self.product_count} шт."

    def add_product(self, product: Product) -> None:
        """Добавляет новый объект в список атрибута __products"""
        self.__products.append(product)
        self.product_count += 1

    @property
    def products(self) -> list:
        """Публичная версия атрибута __products, выдающая список строк"""
        product_list = []
        for product in self.__products:
            product_list.append(str(product))
        return product_list
