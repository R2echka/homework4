'''Класс категорий'''
class Category:
    category_count = 0
    product_count = 0
    def __init__(self, name: str, desc: str, list: list):
        self.name = name
        self.desc = desc
        self.list = list
        Category.category_count += 1
        self.product_count += len(list)
