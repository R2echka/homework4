import pytest

from src.category import Category
from src.product import Product


@pytest.fixture()
def product() -> Product:
    return Product("name", "description", 15.99, 100)


@pytest.fixture()
def category() -> Category:
    return Category("name", "description", [product])


def test_product(product: Product) -> None:
    assert product.name == "name"
    assert product.desc == "description"
    assert product.price == 15.99
    assert product.quantity == 100


def test_category(category: Category) -> None:
    assert category.name == "name"
    assert category.desc == "description"
    assert category.list == [product]


def test_number_of_categories() -> None:
    assert Category.category_count == 1


def test_number_of_products() -> None:
    assert Product.product_count == 1