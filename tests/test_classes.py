import pytest

from src.category import Category
from src.product import Product


@pytest.fixture()
def product() -> Product:
    return Product("name", "description", 15.99, 100)


@pytest.fixture()
def category(product: Product) -> Category:
    return Category("name", "description", [product])


def test_product(product: Product) -> None:
    assert product.name == "name"
    assert product.description == "description"
    assert product.price == 15.99
    assert product.quantity == 100


def test_category(category: Category) -> None:
    assert category.name == "name"
    assert category.description == "description"
    assert category.products == ["name, 15.99 руб. Остаток: 100 шт."]
    assert category.product_count == 1


def test_number_of_categories() -> None:
    assert Category.category_count == 1
    cat2 = Category("something", "description", [])
    assert Category.category_count == 2


def test_add_product(category: Category) -> None:
    prod1 = Product("name1", "-", 1600, 1)
    category.add_product(prod1)
    assert category.product_count == 2


def test_new_product() -> None:
    prod2 = Product.new_product({"name": "name1", "description": "-", "price": 43892.39, "quantity": 432})
    assert type(prod2) is Product


def test_price_setter(product: Product) -> None:
    product.price = -1
    assert product.price == 15.99
    product.price = 16
    assert product.price == 16


def test_str(product: Product, category: Category) -> None:
    assert str(product) == 'name, 15.99 руб. Остаток: 100 шт.'
    assert str(category) == 'name, количество продуктов: 1 шт.'

def test_product_add(product: Product) -> None:
    prod2 = Product.new_product({"name": "name1", "description": "-", "price": 150, "quantity": 2})
    assert product + prod2 == 1899